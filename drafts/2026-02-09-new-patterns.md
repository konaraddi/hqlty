# New Antipattern Candidates - Digest 2026-02-09

Analyzed 100 scored HN comments from the 2026-02-09 digest against 25 existing patterns.

---

## Clearly New Candidates

### 1. fallacy-labeling

**Description:** Dismissing someone's argument by slapping a formal logical fallacy label on it rather than engaging with the substance. Treats conversation like a debate competition to be scored.

**Examples from digest:**

- **Comment #9** (Claude's C Compiler thread): Parent wrote a nuanced, balanced take laying out both sides of the LLM coding debate. Reply: *"Are you trying to demonstrate a textbook example of straw man argument?"* - Reduces a detailed comment to a fallacy label without explaining what was actually straw-manned.

- This pattern is extremely common in online discourse beyond this digest. Variants include: "That's a textbook ad hominem," "Classic whataboutism," "Nice slippery slope fallacy."

**Why it's unproductive:** Naming a fallacy signals logical sophistication but avoids the work of actually engaging. It treats the other person as a student to be graded rather than a participant to be understood. Most of the time, the label doesn't even apply correctly, it just sounds authoritative enough to shut things down.

**Overlap analysis:** Related to pedantic-deflection (deflecting from substance) and semantic-derailment (focusing on form over content), but distinct in mechanism. Those patterns nitpick words or technicalities. This one weaponizes formal logic terminology to dismiss entire arguments. The "I'm grading your reasoning" posture is structurally different from "let me quibble about your word choice."

**Clarifying questions:**
1. Is this distinct enough from pedantic-deflection, or is it just a subtype? (I think yes, because the mechanism and tone are different: academic authority vs. nitpicking.)
2. Does this generalize beyond tech/HN discourse? (Yes, very common in political, philosophical, and social media discussions.)
3. Is the name "fallacy-labeling" neutral enough, or does it sound like it's dismissing actual fallacy identification? (Need to be careful: sometimes pointing out a genuine fallacy is fine. The antipattern is using it as a thought-terminator.)

---

### 2. future-deferral

**Description:** Refusing to engage with a current argument by deferring to future validation. Treats the present discussion as pointless because "time will tell."

**Examples from digest:**

- **Comment #11** (Claude's C Compiler thread): Parent explains that different technologies have different demonstrated growth rates. Reply: *"Well let's check again in two years then."* - Waves away current evidence by punting to an undefined future checkpoint.

- **Comment #10** is related but uses a slightly different mechanism: *"Just a couple more trillion and 6 more months!"* - Mocks the "future will prove us right" stance, but itself avoids engaging with present evidence.

**Why it's unproductive:** It sounds patient and open-minded ("I'm willing to wait and see") but actually abandons the conversation. It dismisses current evidence, reasoning, and data as irrelevant because the real answer is in the future. The other person has no way to respond since you've moved the finish line to a place nobody can reach yet.

**Overlap analysis:** A temporal mirror of hindsight-dismissal. Hindsight-dismissal says "this was always obvious" (dismissing via the past). Future-deferral says "we'll know eventually" (dismissing via the future). Both avoid engaging with present evidence, but through opposite temporal moves. Also related to performative-defeatism (giving up on current discussion) but distinct: defeatism declares futility, while future-deferral declares prematurity.

**Clarifying questions:**
1. Is the "let's check in two years" move common enough outside tech/AI discourse? (Yes: politics, climate debates, economic predictions, sports predictions.)
2. How do we distinguish this from genuinely reasonable "wait and see" positions? (The antipattern version avoids engaging with any current evidence. A reasonable version would say "I see your points, but I think the data will look different in two years because X.")
3. Is "future-deferral" the right name, or would something like "time-will-tell dismissal" be clearer?

---

### 3. silver-bullet-dismissal

**Description:** Responding to a nuanced concern with a one-line "just use X" solution, dismissing the complexity of the problem. Implies the concern is invalid because a simple fix supposedly exists.

**Examples from digest:**

- **Comment #27** (AI coding thread): Parent raises a nuanced concern that AI doesn't have a truly global view of codebases and slowly degrades structure. Reply: *"AGENTS.md is for that global view."* - Reduces an architectural concern about AI limitations to a config file recommendation.

- **Comment #30** (AI coding thread): Parent describes a specific, detailed failure (AI tool couldn't debug a 12-line rate limiter, missed a mutex three times). Reply: *"Try again with gpt-5.3-codex xhigh."* - Responds to a specific failure report by suggesting a different model version, ignoring the substance of what went wrong.

**Why it's unproductive:** It sounds helpful on the surface ("here's a solution!") but treats complex problems as if they have trivial fixes. The person raising the concern already understands the space well enough to articulate a nuanced problem; a one-line tool recommendation doesn't address it. It signals "you just haven't found the right button to press" rather than engaging with the underlying complexity.

**Overlap analysis:** Not well-covered by existing patterns. Achievement-minimization minimizes accomplishments ("it's just X"), while silver-bullet-dismissal minimizes *problems* ("just do Y"). Research-dismissal shifts the burden without offering solutions. This pattern *offers* a solution but in a way that dismisses the concern's depth.

**Clarifying questions:**
1. Is this distinct enough from a helpful but misguided suggestion? (The antipattern is the dismissive framing, not the suggestion itself. "Have you tried X? Though I realize the deeper issue might be..." is fine.)
2. Does this generalize? (Extremely common: "just use Kubernetes," "just write tests," "just talk to your landlord," "just eat healthier.")
3. Is "silver-bullet-dismissal" too jargon-y? Alternatives: "easy-fix-dismissal," "just-use-X."

---

### 4. diy-dismissal

**Description:** Dismissing someone's critique, preferences, or suggestions by telling them to build/make it themselves. Frames expressing an opinion as illegitimate unless you're personally implementing the solution.

**Examples from digest:**

- **Comment #68** (Art of Roads in Games thread): Parent suggests city-builder games could explore alternatives to car-centric design. Reply: *"That's because SimCity is not a tool for preaching your personal opinions... If you want to make your perfect city builder, go ahead, it's easier than ever now for somebody to create a game. Just don't expect everybody else to share your view of 'aspirational'."* - Frames expressing game design preferences as "preaching" and tells the person to make their own game.

**Why it's unproductive:** It sounds empowering ("go build what you want!") but is actually a conversation-ender. It sets an impossibly high bar for participation: you can't have opinions about products unless you're willing to build a competing one. It reframes legitimate discussion of preferences and design trade-offs as entitlement. By this logic, you can't critique a movie unless you're a director, or discuss city planning unless you're a civil engineer.

**Overlap analysis:** Not covered by existing patterns. Elitist-dismissal looks down on users for liking something. Purity-gatekeeping dismisses tools as not "real" enough. DIY-dismissal is different: it dismisses the act of having an opinion by demanding the critic become a creator. The "make it yourself" move is structurally unique.

**Clarifying questions:**
1. Is this common enough to warrant its own pattern? (Very common in open source, gaming, product feedback, politics: "If you don't like the country, leave" is a variant.)
2. How do we distinguish it from genuinely encouraging someone to contribute? (The antipattern version uses it to shut down discussion, not to invite collaboration.)
3. Is "diy-dismissal" the right name? Could also be "build-it-yourself dismissal" or "creator-gatekeeping."

---

### 5. failed-prediction-gotcha

**Description:** Using a past failed prediction (often by someone else or by a field generally) as a gotcha to dismiss current claims. Treats any previous error as permanently discrediting all future claims from the same domain.

**Examples from digest:**

- **Comment #58** (Claude's C Compiler thread): Parent says "the speed of progress can never catch the speed of a moving goalpost!" Comment: *"How do you like those coast-to-coast self drives since the end of 2017?"* - Invokes Elon Musk's failed self-driving timeline to dismiss claims about AI coding progress, even though these are different technologies with different trajectories.

- **Comment #50** uses a related move: *"The problem is that it is absolutely indiscernible from the Theranos conversation as well..."* - Compares AI hype to a notorious fraud case to dismiss current claims by association.

**Why it's unproductive:** It sounds like healthy skepticism ("we've been burned before") but treats entire fields as permanently discredited by any past error. A failed prediction about self-driving cars in 2017 doesn't tell us anything specific about compiler generation in 2026. It shortcuts the work of evaluating current evidence by pointing to a different claim that didn't pan out.

**Overlap analysis:** Not well-covered. Hindsight-dismissal says "this was always obvious." Failed-prediction-gotcha says "they were wrong before, so they're wrong now." History-lesson says "you need to learn history" but doesn't offer specific past failures. This pattern is specifically about wielding a *concrete* past failure as a trump card.

**Clarifying questions:**
1. Is this distinct enough from general skepticism? (The antipattern is the specificity: citing a particular failed prediction as if it invalidates a different claim.)
2. Does it generalize? (Very common: AI, crypto, climate tech, fusion energy, space exploration all have "but they promised X by year Y" gotchas.)
3. When is referencing past predictions legitimate vs. antipattern? (Legitimate: "This field has a pattern of overpromising, so let's look at the evidence carefully." Antipattern: using a specific failed prediction as a mic drop to avoid current discussion.)

---

### 6. sinister-analogy

**Description:** Responding to a neutral or positive observation by invoking an extreme negative historical parallel (fraud, tyranny, disaster) to cast the original point in a dark light without making a substantive argument.

**Examples from digest:**

- **Comment #43** (GitHub Agentic Workflows thread): Parent makes a neutral observation: "This is how humans always worked. Even Einstein had his wife, Marcel Grossmann and Hilbert, among others." Reply: *"And Stalin had Lysenko."* - Responds to a point about collaboration with a reference to state-sponsored pseudoscience, implying dark parallels without explaining the connection.

- **Comment #50** (Claude's C Compiler thread): Parent compares AI progress to SpaceX's trajectory. Reply: *"The problem is that it is absolutely indiscernible from the Theranos conversation as well... For one grifter that happen to succeed at delivering his grandiose promises (Elon), how many grifters will fail?"* - Equates AI development with notorious fraud.

**Why it's unproductive:** It sounds historically aware and cautious ("remember what happened when...") but poisons the well rather than making a specific argument. Drawing a line from "Einstein had collaborators" to "Stalin had Lysenko" isn't an argument; it's guilt by the thinnest possible association. It forces the other person to defend against an extreme comparison they never invited.

**Overlap analysis:** Related to sci-fi-dismissal (reducing discussion to fictional references) but uses real historical atrocities/frauds instead of pop culture. The mechanism is similar (invoking a loaded reference to shut down discussion) but the tone is different: sci-fi-dismissal is flippant, sinister-analogy is ominous. Also related to opportunistic-pivot (forcing a connection to an unrelated topic) but the pivot is specifically toward something dark.

**Clarifying questions:**
1. Is this distinct enough from opportunistic-pivot? (I think yes: the defining feature is the darkness/extremity of the analogy, not just the pivot.)
2. Is "sinister-analogy" too judgmental as a name? Alternatives: "dark-parallel," "extreme-analogy," "guilt-by-history."
3. When is a historical comparison legitimate vs. antipattern? (Legitimate: drawing specific, proportionate parallels with explained connections. Antipattern: dropping a dark reference without explanation and letting the negative association do the work.)

---

## Borderline Candidates

### 7. catchphrase-reduction

**Description:** Reducing a nuanced argument to a mocking catchphrase or meme, treating all claims as identical to the most naive version.

**Example from digest:**

- **Comment #10**: *"Just a couple more trillion and 6 more months!"* - Reduces any discussion of AI progress to a mocking catchphrase about hype cycles.

**Overlap analysis:** Very close to strawman-mockery (creating a simplified version to mock) and related to sci-fi-dismissal (reductive references). The catchphrase format is a stylistic variation rather than a structurally distinct pattern. A catchphrase like "just six more months!" could easily be restated as strawman-mockery: "Meanwhile AI researchers think they're always two years away."

**Verdict:** Probably a variant of strawman-mockery rather than a new pattern. Could be noted as an additional example form within that existing pattern.

**Clarifying questions:**
1. Is the "catchphrase" format common enough and distinct enough to warrant its own entry?
2. Could this be folded into strawman-mockery as a subtype?

---

### 8. stereotype-dismissal

**Description:** Using a professional or group stereotype to categorize and dismiss someone's work rather than engaging with it specifically.

**Example from digest:**

- **Comment #92** (Vouch thread): *"This looks like a fairly typical engineer's solution to a complex social problem"* - Categories the work as stereotypically "engineer-brained" without engaging with its specifics.

**Overlap analysis:** Related to motivation-diagnosis (reducing to character flaws) and elitist-dismissal (looking down on a group). The distinction is that stereotype-dismissal uses *group identity* ("typical engineer") rather than individual motive ("you're lazy") or taste ("the masses have no taste"). But the overlap is significant: "typical engineer's solution" implies a motivation (engineers default to technical solutions because that's what they know), which is close to motivation-diagnosis.

**Verdict:** Arguably covered by the combination of motivation-diagnosis and elitist-dismissal. Would need more examples to justify as standalone.

**Clarifying questions:**
1. Is "typical X's approach" frequent enough as a standalone pattern? (Common: "typical academic answer," "typical MBA thinking," "typical Reddit response.")
2. Could this be documented as an additional example within motivation-diagnosis?

---

## Rejected Candidates

### buzzword-handwave
**Comment #24**: *"I mean I don't think that's exactly true in the age of LLMs."*
**Why rejected:** Only one weak example. The pattern (vaguely invoking a technology trend to dismiss a specific point) is real but doesn't have enough instances in this digest to assess. The example is also quite mild and could just be a poorly-articulated disagreement rather than a structural antipattern.

### control-deflection
**Comment #42**: *"You are 100% in control."*
**Why rejected:** Only one example. The pattern (dismissing systemic concerns by asserting individual agency) is interesting but overlaps significantly with silver-bullet-dismissal ("just do X"). Telling someone "you're in control" when they raise a systemic problem is essentially offering a non-solution. Could be folded under silver-bullet-dismissal as a variant.

### cryptic-deflection
**Comment #28**: *"Induction always sneaks in!"*
**Why rejected:** Too niche. Responding with cryptic philosophical one-liners is more of a communication failure than a structural antipattern. It's not a move people consciously or unconsciously deploy to derail; it's more likely someone being unclear.

### norm-rejection
**Comment #38**: *"Not from the article. Comments don't have to work this way."*
**Why rejected:** Overlaps with meta-grievance-deflection (turning discussion into complaints about how discussion should work). The comment is making a meta-argument about conversational norms rather than a structurally distinct move.

### partisan-attribution
**Comment #3**: *"Which, I've heard, is typical of partisans."*
**Why rejected:** Already covered by motivation-diagnosis. Attributing someone's position to their identity/group membership is a direct instance of diagnosing motivation.

### goalpost-observation
**Comment #39**: *"That's not even close to dominating in chess."*
**Why rejected:** Already covered by precision-deflection and semantic-derailment. Quibbling with the degree of a claim ("beating average players" vs. "dominating") is standard semantic nitpicking.

### in-group-exclusion
**Comment #33**: *"To use internet lingo, no normies."*
**Why rejected:** Already covered by elitist-dismissal and purity-gatekeeping. Using in-group language to dismiss outsiders is a form of framing users as unsophisticated.

---

## Summary Table

| Rank | Candidate | Distinctness | Universality | Examples in Digest | Verdict |
|------|-----------|-------------|-------------|-------------------|---------|
| 1 | **fallacy-labeling** | High (unique mechanism: formal logic as weapon) | Very high (politics, philosophy, social media) | 1 clear | Clearly new |
| 2 | **diy-dismissal** | High (not covered by any existing pattern) | Very high (open source, gaming, products, politics) | 1 clear | Clearly new |
| 3 | **failed-prediction-gotcha** | High (concrete past failures as trump cards) | Very high (AI, crypto, climate, energy, space) | 2 | Clearly new |
| 4 | **future-deferral** | High (temporal mirror of hindsight-dismissal) | High (predictions, politics, tech, sports) | 1-2 | Clearly new |
| 5 | **silver-bullet-dismissal** | Medium-high (minimizes problems, not achievements) | Very high ("just use X" is everywhere) | 2 clear | Clearly new |
| 6 | **sinister-analogy** | Medium-high (dark variant of opportunistic-pivot) | High (any ideological debate) | 2 | Clearly new |
| 7 | catchphrase-reduction | Low (variant of strawman-mockery) | Medium (mostly tech/AI discourse) | 1 | Borderline |
| 8 | stereotype-dismissal | Low (overlaps motivation-diagnosis) | Medium-high ("typical X" is common) | 1 | Borderline |
