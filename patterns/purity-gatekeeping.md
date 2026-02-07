---
slug: purity-gatekeeping
title: Purity Gatekeeping
---

## The Pattern

Dismissing technical choices or tools as inadequate because they use higher-level abstractions rather than lower-level fundamentals.

"Real developers don't need frameworks for that."

"If people actually understood JavaScript, they wouldn't need React."

"Using Tailwind just means someone never learned proper CSS."

"Electron apps are bloated. Native or nothing."

### Why It's Unproductive

Treats modern abstractions as shortcuts for the incompetent rather than legitimate trade-offs. It's tempting because advocating for fundamentals feels like defending craft and expertise, but it conflates yesterday's abstractions with timeless principles while ignoring business context and evolving needs. Shuts down discussion of actual trade-offs like development speed, team skills, or maintenance costs.

## The Better Move

"What drove the decision to use that stack over alternatives?"

"Curious about the trade-offs here. How did performance compare to native?"

"I've found value in lower-level approaches, but I can see why teams choose this for faster iteration."

"Different abstractions make sense for different constraints. What were the biggest factors?"

### Why It's Better

Acknowledges that tool choices involve trade-offs rather than skill deficits. Opens discussion about actual constraints and goals instead of asserting a single correct approach.

---

## Example in Context

**Original**: "We shipped the desktop app using Electron to reuse our web codebase and move faster."

**Antipattern**: "Electron apps are bloated garbage. Real developers build native apps that don't eat 500MB of RAM."

**Better**: "What drove the decision to use Electron over native? I'm curious how you weighed bundle size and performance against development speed."
