# Colophon Note: Case Study System Failure

**Date:** February 6-7, 2026
**Status:** Abandoned
**Lesson:** Over-engineering destroys signal

---

## What Was Attempted

A multi-stage automated pipeline to generate case studies from 3+ years of AI conversation exports (Claude, ChatGPT, Gemini):

1. **Ingest Phase** — Parse JSON exports from 3 platforms
2. **Semantic Indexing** — Regex pattern matching to detect project mentions
3. **Moment Extraction** — Classify conversation snippets into "moment types" (genesis, pivot, problem, etc.)
4. **Skeleton Building** — Assemble narrative skeletons from classified moments
5. **Voice Blending** — Algorithmically extract "personal voice patterns" and blend with Master Builder principles
6. **Prose Generation** — LLM generates case study prose from skeletons
7. **Guardrails** — Validation checks for specificity and texture

20 Python scripts. 52 passing tests. 265MB of skeleton JSON files.

---

## Why It Failed

The system produced flat, generic, often incorrect case studies despite extensive planning and "successful" test coverage.

**Root cause:** Each processing layer stripped context and texture from the source material. By the time content reached prose generation, the LLM was working from thin abstractions — classified "moment types" and extracted "snippets" — not the actual rich conversations.

**Specific failures:**

- **Regex "semantic matching"** misclassified content and missed important material
- **"Moment type" classification** reduced nuanced thinking to generic categories
- **Snippet extraction** lost the surrounding context that gave quotes meaning
- **"Voice blending"** is conceptually flawed — you can't algorithmically extract and recombine someone's voice
- **LLM prose generation from skeletons** had nothing real to work with

The more processing layers, the worse the output. The pipeline optimized for structure over substance.

---

## What Actually Works

The raw timeline JSONs (conversations organized by project, chronologically) are valuable. They contain actual thinking, actual pivots, actual voice.

The job isn't extraction and generation — it's **curation and light editing**:

1. Human reads the timeline for a project
2. Human identifies key passages
3. Human writes the case study using actual quotes
4. The voice is already there; it doesn't need to be "extracted" or "blended"

One manually curated document (`EXTRACTION_MINING_RESULTS.md` — 42 hand-selected quotes with context) is worth more than 265MB of algorithmically processed skeletons.

---

## What Was Kept

- `docs/extraction-output/*.json` — Timeline JSONs (valuable raw material)
- `docs/EXTRACTION_MINING_RESULTS.md` — 42 curated quotes (actually useful)
- `docs/voice-protocol.md` — Master Builder voice guidance
- `docs/NARRATIVE-ARCHITECTURE.md` — Site structure
- `docs/mainfest.json` — Project definitions

---

## What Was Deleted

- 20 Python scripts in `scripts/`
- Test files for those scripts
- `docs/case-study-skeletons/` — 265MB of processed garbage
- `docs/case-study-prose/` — Generated garbage
- Implementation plans for the failed system
- "Completion reports" claiming success

---

## The Lesson

Sophisticated pipelines that process rich source material through multiple abstraction layers destroy the signal they're meant to preserve.

The conversations already contained everything needed. The system's job was to make them accessible, not to transform them into something else.

Simpler is better. Human curation beats algorithmic extraction. Trust the source material.

---

*For the colophon: This failure is part of the site's own design history. The methodology that works for case studies (first principles, constraint-driven, human judgment) is the same methodology the failed system ignored.*
