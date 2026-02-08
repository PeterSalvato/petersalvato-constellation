# Case Study: Savepoint Protocol

## The Constraint

How do you preserve the thinking behind decisions when the tools you use to think forget everything?

---

## The Problem (March 2025)

Marathon brainstorming sessions with Claude. Hours of ideation, naming, refinement. Then the conversation ends and it's gone. The next session starts fresh. No memory of the phrases that felt right, the decisions that were made, the reasoning that led there.

> "We wind up with these marathon sessions and your memory limitations cause us to lose things."

The issue wasn't just Claude's context window. It was the fundamental problem of working across many conversations, many projects, many months. Context leaks. Decisions evaporate. You can't remember why you made a choice, only that you made it.

For someone with ADHD, this compounds. Executive dysfunction means the cognitive load of reconstructing context can prevent starting at all.

---

## The Genesis: From Capture to Protocol (March–April 2025)

It started as a simple question: "Would it make sense for me to pull out save points from the various conversations that we workshop in this project?"

The first draft was basic: structured checkpoints, timestamped reflections, markdown files in a `.savepoints/` folder. Version control for your brain.

But the problem kept revealing itself as deeper. It wasn't just about capturing decisions. It was about:
- Preserving the *reasoning* behind decisions
- Tracking how ideas evolve across conversations
- Making the captured knowledge traversable, not just stored
- Protecting semantic integrity—preventing revisionist edits without audit trail

April 2025: 140 conversations in a single month. The protocol crystallized under pressure.

---

## The Technical Solution: v3.0 Syntax

The protocol evolved through three major versions, arriving at a formal syntax:

```
savepoint
  protocol_version:3.0
  category:[domain_context]
  function:[role or purpose]
  importance:[optional]
  confidence:[optional]
  timestamp:[ISO 8601 format]
  # [semantic content of the Savepoint]
/
```

The content block is the core: a single-line, semantically atomic statement that can stand alone as a searchable anchor. Not a summary. The actual decision, phrased as a durable artifact.

The infrastructure: a pip-installable Python CLI that processes ChatGPT exports, splits conversations into individual files, generates semantic filenames, and groups related conversations into combined documents for traversal.

---

## The Positioning: What Savepoint Is Not

A comparison to Zettelkasten clarified the difference:

| Zettelkasten | Savepoint Protocol |
|--------------|-------------------|
| Idea proliferation | Authorship integrity |
| Atomic notes, flat linking | Recursive versioning, temporal hierarchy |
| Fluid remixing | Protected semantic boundaries |
| Emergent structure | Explicit decision lineage |
| "What did I think?" | "Why did I decide?" |

Savepoint is not a note-taking system. It's cognitive version control. The difference matters: Zettelkasten helps you develop ideas. Savepoint helps you not lose the decisions you've already made.

---

## The Three Altitudes

Savepoint occupies the middle position in a triangulated competency map:

**Ground Level (Encore):** Operational anchor. Proves the grit to impose order on hostile, constrained environments.

**System Level (Savepoint):** Technical engine. Proves full-stack capability when constraints are removed. "The concept car—pure performance."

**Meta Level (Aetherwright):** Conceptual north star. Proves the ability to design ontologies before a single line of code is written.

Together, they answer a fundamental question: this person can dream in systems (Aetherwright), build the engine (Savepoint), and survive the reality (Encore).

---

## What It Proves

Savepoint Protocol demonstrates that:

1. **Cognitive tools can be formalized.** The messy process of thinking across conversations can be structured without killing it.

2. **Version control applies to more than code.** The same principles that make git valuable—audit trails, branching, explicit commits—apply to decisions and reasoning.

3. **Neurodivergent operators need different infrastructure.** Tools designed for neurotypical workflows fail under executive dysfunction. Savepoint is built for brains that leak context.

4. **The gap between thinking and shipping is bridgeable.** When the reasoning survives, the implementation can be bold. You can make aggressive decisions when the fallback is documented.

---

## Current State

v3.0 — Open source. CLI tool operational. Syntax finalized.

The protocol now underpins how all major projects are developed. Every significant decision gets a savepoint. Every creative session ends with captured context. The marathon conversations still happen, but what they produce doesn't evaporate.

> "Decisions stay bold when the fallback is documented."

---

*Generated: 2026-02-07*
*Method: Sequential reading of 548 conversations over 17 months*
