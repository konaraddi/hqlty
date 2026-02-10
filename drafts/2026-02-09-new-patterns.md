# New Antipattern Candidates from 2026-02-09 Digest

Reviewed 100 HN comments. After batch analysis and de-duplication against the 25 existing patterns, the following **10 candidate patterns** emerged as genuinely new.

---

## 1. Temporal Deferral

**What it looks like:** Instead of engaging with the current argument, someone suggests checking back later when more evidence exists.

**Examples from digest:**
- "Well let's check again in two years then." (#11)
- "Just a couple more trillion and 6 more months!" (#10 - sarcastic variant)

**Why it might be an antipattern:** Avoids engaging with the present evidence by pushing the debate into an indefinite future. Neither side learns anything. The conversation just... stops.

**Why it's better:** Forces people to actually state what evidence would change their mind, rather than deferring indefinitely.

**Overlap check:** Not covered by existing patterns. Closest is performative-defeatism, but that declares futility rather than deferring to future evidence.

**Clarifying questions for review:**
- Does this happen frequently enough outside of tech/AI debates to be universal?
- Is the sarcastic variant ("just 6 more months!") a separate pattern or the same one?
- Should this cover both the sincere "let's wait and see" and the sarcastic "sure, any day now" versions?

---

## 2. Goalpost Shifting

**What it looks like:** After someone demonstrates achievement at a stated bar, moving the bar to something higher without acknowledging the original accomplishment.

**Examples from digest:**
- Parent shows LLMs beat average chess.com players. Reply: "That's not even close to dominating in chess." (#39)
- "Anti-LLM: isn't all this intelligence supposed to give us something better than what we already have?" (#52)
- Parent describes 10-20x coding speed. Reply: "Okay but again what multiplier of features have you actually shipped." (#32)

**Why it might be an antipattern:** Makes it impossible to ever satisfy the critic. Each demonstrated achievement is met with a new, higher bar that was never the original standard.

**Overlap check:** Related to achievement-minimization but distinct. Achievement-minimization diminishes what was done ("that's just X"). Goalpost shifting acknowledges what was done but instantly demands something bigger.

**Clarifying questions for review:**
- Is this distinct enough from achievement-minimization to be its own pattern?
- The "what have you actually shipped" variant feels slightly different (demanding proof vs. raising the bar). Same pattern or separate?

---

## 3. Past-Failure Poisoning

**What it looks like:** Invoking a past failed prediction or a known fraud to discredit current claims, without examining whether the current situation differs.

**Examples from digest:**
- "How do you like those coast-to-coast self drives since the end of 2017?" (#58)
- "The problem is that it is absolutely indiscernible from the Theranos conversation as well... For one grifter that happen to succeed... how many grifters will fail?" (#50)

**Why it might be an antipattern:** Guilt by association. Past failures don't prove current claims are wrong. It treats all optimism as the same kind of hype, regardless of actual evidence.

**Overlap check:** Not covered. Closest might be hindsight-dismissal, but that's about dismissing confirmed findings as obvious. This is about using historical failures to preemptively discredit.

**Clarifying questions for review:**
- Is the "Theranos comparison" a sub-type of this, or its own thing (fraud-association)?
- Should the pattern name be more neutral? "Past-failure poisoning" implies the person is wrong to bring it up, but sometimes past failures ARE relevant.
- How to distinguish this from a legitimate "pattern-matching to past failures" argument?

---

## 4. Pathologizing Disagreement

**What it looks like:** Treating someone's position as a symptom of mental illness, delusion, or cognitive impairment rather than engaging with it.

**Examples from digest:**
- "Is this what AI psychosis looks like? How can anyone that is a half decent programmer actually believe that..." (#59)

**Why it might be an antipattern:** Moves from "I disagree with your argument" to "there's something wrong with you for believing this." Destroys any possibility of productive exchange.

**Overlap check:** Related to motivation-diagnosis (which reduces positions to character flaws), but this goes further by implying actual mental deficiency. Could be a more extreme variant.

**Clarifying questions for review:**
- Is this common enough to be its own pattern, or is it just an extreme form of motivation-diagnosis?
- Only one example in this digest. Should we wait to see if more surface?
- The combination of "psychosis" + "half decent programmer" does two things at once (pathologize + gatekeep). Should we separate those?

---

## 5. Knowledge-Gatekeeping Dismissal

**What it looks like:** Dismissing someone's argument as uninformed and telling them to "go read about it," without actually providing the counter-argument or specific sources.

**Examples from digest:**
- "That's a deeply oversimplified understanding of Taiwan and reunification. There's so much good reading on the topic out there and it's really worth even just skimming the surface of it." (#98)

**Why it might be an antipattern:** Signals superior knowledge without demonstrating it. The person avoids the vulnerability of actually making an argument while positioning themselves as the expert. Leaves the other person with nothing concrete to respond to.

**Overlap check:** Related to elitist-dismissal and preemptive-condescension, but distinct. Those are about tone and framing. This is specifically about claiming expertise while refusing to share it.

**Clarifying questions for review:**
- Is "go educate yourself" common enough in HN-style discourse to warrant its own pattern? (It's very common on Twitter/Reddit.)
- Overlap with condescending-reveal? The reveal at least shares the information. This withholds it.
- Only one clear example in this digest. Wait for more?

---

## 6. Cynical Attribution

**What it looks like:** Reframing a technical observation or neutral design choice as evidence of intentional malice or conspiracy, without evidence.

**Examples from digest:**
- "That sounds like a feature, not a bug, given where Google's revenue comes from." (#25)
- "They were aware of the problem and they covered it up, rather than try to show better ways of living. It's unintentional propaganda." (#75)

**Why it might be an antipattern:** Assumes the worst intent and redirects the conversation from "what happened" to "who's to blame." Treats speculation about motives as established fact.

**Overlap check:** Related to motivation-diagnosis, but that pattern is about diagnosing individual commenters' motives. This is about attributing institutional or organizational malice to explain technical/design decisions.

**Clarifying questions for review:**
- Is "Hanlon's razor violation" a better frame? (Never attribute to malice what can be explained by incompetence/constraints.)
- Where's the line between healthy skepticism about corporate motives and this antipattern?
- The "feature not a bug" phrasing is extremely common. Is the pattern the cynicism, or the specific move of reframing neutrality as malice?

---

## 7. Parody Dismissal

**What it looks like:** Using a humorous template, copypasta, or elaborate parody format to dismiss an idea, making rejection entertaining enough that it avoids scrutiny.

**Examples from digest:**
- The long Usenet-style "Your solution advocates a..." checklist (#89)

**Why it might be an antipattern:** The humor and format create social proof for rejection without requiring actual reasoning. It's easy to check boxes on a template; it's harder to engage with the specific idea's merits.

**Overlap check:** Not covered. Closest is strawman-mockery, but that creates a fictional naive person. This uses a recognized comedic format as the vehicle.

**Clarifying questions for review:**
- Is this common enough outside of HN/tech culture?
- The specific example (#89) is actually quite thoughtful in its checkbox selections. Is this an antipattern even when done well?
- Should this be limited to templates/copypasta, or include any humor-as-dismissal?

---

## 8. Version Deflection

**What it looks like:** When someone reports a concrete limitation or failure, dismissing it by suggesting a newer version/model/product will fix it.

**Examples from digest:**
- Parent describes AI failing at a 12-line rate limiter. Reply: "Try again with gpt-5.3-codex xhigh." (#30)

**Why it might be an antipattern:** Avoids engaging with the actual reported problem. Turns every criticism into a product recommendation. Implies the person's experience is invalid because they used the "wrong" tool.

**Overlap check:** Not directly covered. Could overlap with temporal-deferral (both punt to the future), but this is specifically about suggesting a newer product/version rather than waiting for evidence.

**Clarifying questions for review:**
- Is this specific to AI/tech discourse or does it generalize? ("Try the new iPhone," "Have you tried the latest update?")
- Overlap with temporal-deferral? Both avoid the present. This one offers a concrete "fix" though.
- Only one clear example. Wait for more?

---

## 9. Categorical Dismissal

**What it looks like:** Dismissing an idea by stereotyping the type of person who created it, treating the category as a sufficient refutation.

**Examples from digest:**
- "This looks like a fairly typical engineer's solution to a complex social problem: it doesn't really solve the problem..." (#92)
- "You guys simply can't help yourselves." (#95)

**Why it might be an antipattern:** Substitutes engagement with categorization. Once you've labeled something a "typical engineer's solution" or grouped people into "you guys," you've signaled that the idea doesn't need individual analysis.

**Overlap check:** Related to motivation-diagnosis and elitist-dismissal, but this is specifically about dismissing via category membership rather than individual motives or sophistication level.

**Clarifying questions for review:**
- Is this distinct enough from elitist-dismissal? Elitist-dismissal is about "the masses." This is about professional/identity categories.
- "Typical engineer's solution" is genuinely common in HN discourse. Worth capturing?
- Does this need a better name? "Categorical dismissal" is a bit academic.

---

## 10. Cryptic One-Liner

**What it looks like:** Responding with a brief, opaque, intellectually-coded statement that sounds clever but doesn't actually engage with the argument.

**Examples from digest:**
- "Induction always sneaks in!" (#28)
- "And Stalin had Lysenko." (#43)

**Why it might be an antipattern:** Requires the reader to do all the interpretive work. The commenter gets to appear smart without the risk of being wrong about anything specific. If challenged, they can always say "that's not what I meant."

**Overlap check:** Not clearly covered. Pedantic-deflection is about nitpicking details. This is about performing intelligence through brevity and obscurity.

**Clarifying questions for review:**
- Is brevity itself the problem, or the obscurity? A short, clear response isn't an antipattern.
- The two examples feel different: "Induction always sneaks in" is genuine philosophical shorthand; "And Stalin had Lysenko" is a dark analogy. Same pattern?
- Is this too broad? Many HN comments are terse. Where's the line?

---

## Patterns Considered but Rejected

These came up in analysis but overlap too much with existing patterns or aren't clearly antipatterns:

| Candidate | Why Rejected |
|-----------|-------------|
| Mirror-accusation ("no u") | Too basic/universal. Also partially covered by strawman-mockery dynamics. |
| Bare assertion | Unsubstantiated claims are a problem but not really a "pattern" with structure. |
| Reassurance-dismissal ("You are 100% in control") | Only one example. Could be a variant of condescending-reveal. |
| Exclusivity-nostalgia ("no normies") | Variant of purity-gatekeeping. |
| Contested-as-settled | Common but hard to distinguish from "having a strong opinion." |
| Sarcastic pile-on | Sarcasm is a tone, not a structural pattern. The underlying move is usually one of the above. |
| Norm-rejection deflection | Too niche (one example). |

---

## Summary: Strongest Candidates

If I had to pick the top 5 most worth writing up based on frequency, distinctness from existing patterns, and universality:

1. **Goalpost Shifting** - Very common, clearly distinct from achievement-minimization
2. **Past-Failure Poisoning** - Common in any tech/political debate
3. **Temporal Deferral** - Universal pattern, seen in many domains
4. **Cynical Attribution** - Very common online, distinct from motivation-diagnosis
5. **Knowledge-Gatekeeping Dismissal** - Extremely common on social media
