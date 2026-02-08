#!/usr/bin/env python3
"""
Fetch Hacker News comments and score them as potential discourse antipattern candidates.

Uses heuristics (thread death, flagged status, escalation keywords, etc.) to identify
comments that may represent antipatterns. Outputs a markdown digest of the top candidates.

No external dependencies required -- uses only Python stdlib.
"""

import json
import re
import sys
import os
import html
import time
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

HN_API = "https://hacker-news.firebaseio.com/v0"
MAX_COMMENTS_OUTPUT = 100
MAX_STORIES = 30
MAX_COMMENTS_PER_STORY = 150
REQUEST_TIMEOUT = 10

# Patterns that suggest escalation or dismissiveness
ESCALATION_KEYWORDS = [
    r"\bobviously\b",
    r"\bclearly you\b",
    r"\bthat'?s not what i said\b",
    r"\byou clearly\b",
    r"\byou obviously\b",
    r"\byou don'?t understand\b",
    r"\byou'?re missing the point\b",
    r"\bstrawman\b",
    r"\bstraw man\b",
    r"\bmoving the goalposts?\b",
    r"\bgaslighting\b",
    r"\bin bad faith\b",
    r"\bbad faith\b",
    r"\bnice try\b",
    r"\bwell actually\b",
    r"\bwell,? duh\b",
    r"\bimagine thinking\b",
    r"\btell me you\b",
    r"\bdo your (own )?research\b",
    r"\bi can'?t even\b",
    r"\bwhoosh\b",
    r"\br/whoosh\b",
    r"\byou people\b",
    r"\btypical\b",
    r"\bof course you\b",
    r"\bnot surprised\b",
    r"\bwhat a surprise\b",
    r"\bkeep telling yourself\b",
    r"\bwhatever you say\b",
    r"\bsure,? buddy\b",
    r"\bok,? buddy\b",
    r"\bsweet summer child\b",
    r"\bbless your heart\b",
    r"\bthat'?s adorable\b",
    r"\boh honey\b",
]

ESCALATION_PATTERNS = [re.compile(p, re.IGNORECASE) for p in ESCALATION_KEYWORDS]

# Regex to detect links (http/https URLs, markdown links, bare domains)
LINK_PATTERN = re.compile(
    r"https?://|www\.|\.com/|\.org/|\.net/|\[.*?\]\(.*?\)|<a\s+href",
    re.IGNORECASE,
)


def fetch_json(url, retries=3):
    """Fetch JSON from a URL with retries and exponential backoff."""
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "hqlty-antipattern-digest/1.0"})
            with urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (URLError, HTTPError, TimeoutError) as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                return None


def strip_html(text):
    """Strip HTML tags and decode entities from HN comment text."""
    if not text:
        return ""
    # HN uses <p> for paragraphs
    text = text.replace("<p>", "\n\n")
    # Remove all other HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Decode HTML entities
    text = html.unescape(text)
    return text.strip()


def has_links(text):
    """Check if text contains any links."""
    return bool(LINK_PATTERN.search(text or ""))


def count_escalation_matches(text):
    """Count how many escalation keyword patterns match in the text."""
    if not text:
        return 0
    count = 0
    for pattern in ESCALATION_PATTERNS:
        if pattern.search(text):
            count += 1
    return count


def has_quote_then_attack(text):
    """Check if comment quotes someone then responds dismissively."""
    if not text:
        return False
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith(">") and i + 1 < len(lines):
            next_line = lines[i + 1].lower()
            for pattern in ESCALATION_PATTERNS:
                if pattern.search(next_line):
                    return True
    return False


def fetch_item(item_id):
    """Fetch a single HN item."""
    return fetch_json(f"{HN_API}/item/{item_id}.json")


def fetch_comment_tree(story_item):
    """Fetch comments for a story, returning a flat list of comment items."""
    kid_ids = story_item.get("kids", [])
    if not kid_ids:
        return []

    comments = []
    queue = list(kid_ids)
    # Track depth for each comment
    depth = {kid_id: 1 for kid_id in kid_ids}

    with ThreadPoolExecutor(max_workers=10) as executor:
        while queue and len(comments) < MAX_COMMENTS_PER_STORY:
            batch = queue[: min(50, MAX_COMMENTS_PER_STORY - len(comments))]
            queue = queue[len(batch) :]

            futures = {executor.submit(fetch_item, cid): cid for cid in batch}
            for future in as_completed(futures):
                item = future.result()
                if item and item.get("type") == "comment" and not item.get("deleted"):
                    item["_depth"] = depth.get(item["id"], 1)
                    item["_story_id"] = story_item["id"]
                    item["_story_title"] = story_item.get("title", "")
                    comments.append(item)

                    # Queue children if we haven't hit the limit
                    child_ids = item.get("kids", [])
                    for cid in child_ids:
                        depth[cid] = item["_depth"] + 1
                    if len(comments) + len(queue) < MAX_COMMENTS_PER_STORY:
                        queue.extend(child_ids)

    return comments


def score_comment(comment):
    """
    Score a comment for antipattern potential. Higher = more likely to be interesting.

    Returns (score, reasons) tuple.
    """
    score = 0
    reasons = []
    text = strip_html(comment.get("text", ""))

    # Skip empty or very short comments
    if len(text) < 20:
        return 0, []

    # Skip comments with links
    if has_links(text) or has_links(comment.get("text", "")):
        return 0, []

    # Dead/flagged comments (strong signal)
    if comment.get("dead"):
        score += 5
        reasons.append("flagged/dead")

    # Escalation keywords
    keyword_count = count_escalation_matches(text)
    if keyword_count > 0:
        score += keyword_count * 2
        reasons.append(f"{keyword_count} escalation keyword(s)")

    # Quote-then-attack pattern
    if has_quote_then_attack(text):
        score += 3
        reasons.append("quote-then-attack")

    # Thread killer: deep in thread and has no children
    kids = comment.get("kids", [])
    depth = comment.get("_depth", 1)
    if not kids and depth >= 3:
        score += 2
        reasons.append(f"thread death at depth {depth}")

    # High reply count relative to depth (contentious)
    if len(kids) >= 5:
        score += 2
        reasons.append(f"{len(kids)} direct replies")

    # Length heuristic: very short replies in deep threads are often dismissive
    if len(text) < 80 and depth >= 2:
        score += 1
        reasons.append("short reply in thread")

    return score, reasons


def format_digest(scored_comments, date_str):
    """Format scored comments into a markdown digest."""
    lines = [
        f"# HN Antipattern Digest - {date_str}",
        "",
        f"Top {len(scored_comments)} candidate comments scored by heuristics.",
        "Review these for potential new antipatterns or examples of existing ones.",
        "",
        "---",
        "",
    ]

    for i, (score, reasons, comment) in enumerate(scored_comments, 1):
        text = strip_html(comment.get("text", ""))
        author = comment.get("by", "[deleted]")
        story_title = comment.get("_story_title", "Unknown")
        depth = comment.get("_depth", 0)
        hn_url = f"https://news.ycombinator.com/item?id={comment['id']}"
        reason_str = ", ".join(reasons)

        lines.append(f"### #{i} (score: {score})")
        lines.append("")
        lines.append(f"**Story**: {story_title}")
        lines.append(f"**Author**: {author} | **Depth**: {depth} | **Signals**: {reason_str}")
        lines.append(f"**Link**: {hn_url}")
        lines.append("")
        lines.append("> " + text.replace("\n", "\n> "))
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    print("Fetching top stories from HN...", file=sys.stderr)
    story_ids = fetch_json(f"{HN_API}/topstories.json")
    if not story_ids:
        print("Failed to fetch top stories.", file=sys.stderr)
        sys.exit(1)

    story_ids = story_ids[:MAX_STORIES]

    # Fetch story items
    print(f"Fetching {len(story_ids)} stories...", file=sys.stderr)
    stories = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_item, sid): sid for sid in story_ids}
        for future in as_completed(futures):
            item = future.result()
            if item and item.get("kids"):
                stories.append(item)

    print(f"Found {len(stories)} stories with comments.", file=sys.stderr)

    # Fetch and score comments from each story
    all_scored = []
    for i, story in enumerate(stories):
        print(
            f"  [{i+1}/{len(stories)}] Fetching comments for: {story.get('title', '?')[:60]}",
            file=sys.stderr,
        )
        comments = fetch_comment_tree(story)

        for comment in comments:
            score, reasons = score_comment(comment)
            if score > 0:
                all_scored.append((score, reasons, comment))

    # Sort by score descending, take top N
    all_scored.sort(key=lambda x: x[0], reverse=True)
    top = all_scored[:MAX_COMMENTS_OUTPUT]

    print(f"\nScored {len(all_scored)} candidates, outputting top {len(top)}.", file=sys.stderr)

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    digest = format_digest(top, date_str)

    # Write to digests directory
    digest_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "digests")
    os.makedirs(digest_dir, exist_ok=True)
    digest_path = os.path.join(digest_dir, f"{date_str}.md")

    with open(digest_path, "w") as f:
        f.write(digest)

    print(f"Digest written to {digest_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
