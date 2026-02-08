# Skill Spec: Semantic Lineage Tracing

**Status:** Initial capture
**Version:** 0.1
**Date:** 2026-02-07

---

## Purpose

Traverse large documents or transcripts chronologically and trace the lineage of semantic meaning—how concepts emerge, evolve, pivot, and crystallize over time.

---

## The Problem It Solves

Large bodies of work (conversation histories, project logs, design documents) contain embedded narrative arcs that aren't visible from any single point. Meaning develops across time. Decisions reference earlier decisions. Pivots happen gradually then suddenly.

Without a systematic way to trace this lineage, you either:
- Lose the evolution (only see final state)
- Drown in the volume (can't hold it all in memory)
- Miss the pivots (they're obvious only in retrospect)

---

## Core Capability

Given a large chronological corpus:

1. **Chunk and traverse** — Read in manageable pieces, carry forward running context
2. **Track emergence** — Note when concepts first appear, what triggers them
3. **Map evolution** — How does concept X at time T1 become concept Y at time T2?
4. **Identify crystallization** — Where does fuzzy thinking become locked-in decision?
5. **Surface pivots** — What changed? Why? What was the trigger?

---

## Potential Outputs

*(To be refined)*

- **Semantic timeline** — Chronological list of concept states with transitions
- **Pivot map** — Key moments where direction changed, with before/after
- **Lineage tree** — How one concept spawned or transformed into others
- **Quote extraction** — Verbatim moments of crystallization
- **Summary arc** — The narrative spine without the detail

---

## Potential Inputs

- Timeline JSON (conversation exports)
- Markdown transcripts
- Git commit histories with messages
- Any chronologically-ordered text corpus

---

## Implementation Questions

*(To be answered through use)*

- Chunk size? How much context can be carried forward?
- Output format? Markdown? JSON? Both?
- Interactive or batch? Pause for human input or run through?
- How to handle multi-threaded conversations (parallel topics)?
- Integration with Savepoint Protocol's existing extraction tools?

---

## Relationship to Other Tools

- **Savepoint creation** captures raw material during work
- **Semantic lineage tracing** processes that material after the fact
- **Case study synthesis** is one application (others: architecture tracing, bug hunting, decision archaeology)

---

## Origin

This skill emerged from the case study generation work (2026-02-07). The failed system tried to extract meaning through regex and classification. The working approach was to read chronologically and let the arc emerge. That capability—systematic chronological reading with semantic tracking—is general purpose.

---

*Initial capture. To be refined through application.*
