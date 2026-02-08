---
title: hqlty
layout: layout.11ty.js
eleventyExcludeFromCollections: true
---

A reference for discourse antipatterns: the subtle conversation moves that sound reasonable but derail productive discussion.

## What This Is

This is a collection of common patterns that happen in online conversations. These aren't insults or trolling. They're moves that feel natural in the moment but tend to make discussions less productive. Most people don't realize they're doing them.

Each pattern includes:
- Examples of what it looks like
- Why it tends to backfire
- Better alternatives that keep conversations on track

The goal isn't to win arguments or prove anyone wrong. It's to help make online spaces a bit more pleasant and productive for everyone.

## Patterns

{% for pattern in collections.patterns | sort(false, false, 'data.title') -%}
- [{{ pattern.data.title }}]({{ pattern.url }})
{% endfor %}

## How to Use These

If you see one of these patterns in a discussion (including your own comments), these pages can help redirect things constructively.

**When linking to a pattern:**
- Stay respectful and assume good intent
- Focus on the conversation pattern, not the person
- Pair it with engagement on the actual topic
- Remember that you're trying to improve the discussion, not score points

**Example:** Instead of just dropping a link, you might say: "I think we might be talking past each other here. [This pattern](link) describes what I'm seeing. On the actual question about X, I think..."

The point is to get conversations back on track, not to lecture people about how they communicate.

## Contributing

See something that could be better? This is an open project. Patterns should be common, recognizable, and have clear constructive alternatives.
