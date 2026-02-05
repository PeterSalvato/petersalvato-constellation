# Colophon: How This Site Was Built

**Status:** Working document. Updated as execution proceeds.
**Last Updated:** 2026-02-05 (Planning phase)
**Next Update:** When Phase 2 rebuild execution begins

---

## The Problem This Site Solves

The gap between what was visible (142K characters) and what was actually thought (67M+ characters of ideation across 3+ years) was catastrophic. The site showed outcomes. It didn't show methodology. It competed on delivery, not on thinking.

This reconstruction rebuilds the site to show both: the work AND the process that created it.

---

## The Approach: Systems, Not Templates

Instead of forcing all projects through a narrative template, each case study follows its actual shape:

**Three-Part Structure (Applied to Each System)**
1. **Here is the system** — What it actually is
2. **Here is why I needed to make it** — The constraint or problem it solved
3. **Here is how I did** — Chronological story from extraction timeline

This structure works because it's not a template. It's a principle: mission-first, extraction-informed, narrative-true.

---

## The Specialist Architecture

Five specialized agents handle distinct work, preventing generalist failure:

### 1. Manifest Context Specialist
**What it does:** Extracts mission, constraint, and coherence principle from manifest.json

**Why it matters:** Previous attempt failed because extraction content (louder, more detailed) drowned out manifest intent. Context specialist ensures mission is primary source.

**Output:** One-page spec per project (mission, why, defense-against-drift)

### 2. Privacy & Security Specialist
**What it does:** Screens extraction timelines for personal data, sensitive info, family details, real names/locations

**Why it matters:** Site should show thinking, not expose private conversations or data

**Output:** Sanitized timeline + redaction report. Final gate before anything public.

### 3. Timeline Narrator Specialist
**What it does:** Reads extraction timeline chronologically, identifies narrative arc

**Why it matters:** Extraction content is raw. Needs to be shaped into a story that flows naturally

**Output:** Structured outline showing how/why/what-survived arc

### 4. Master Builder Copywriter Specialist
**What it does:** Writes case study in Master Builder voice using context spec + timeline outline

**Why it matters:** Voice consistency is critical. Single consistent voice across all projects

**Output:** Finished case study markdown, ready for publication

### 5. Alignment Verifier Specialist
**What it does:** Reads finished copy against manifest. Checks for generic process language instead of specific system explanation

**Why it matters:** Quality gate to catch misalignment before publication

**Output:** Approval or "rewrite section X because this sounds generic"

### 6. Process Capture Agent (New)
**What it does:** Observes specialist work, documents what actually happened vs. what was planned

**Why it matters:** Keeps Colophon honest and contemporaneous

**Output:** Running log of decisions, blockers, discoveries, actual workflow

---

## The Workflow (No Public Commits Until Privacy Approval)

All work stays local. Only finished, privacy-approved case studies go to public repo.

```
LOCAL WORKING DIRECTORY
├─ Manifest Context Specialist → docs/working/context-[project].md
├─ Privacy & Security Specialist → docs/working/sanitized-[project].md
├─ Timeline Narrator Specialist → docs/working/outline-[project].md
├─ Master Builder Copywriter → docs/working/draft-[project].md
├─ Alignment Verifier → docs/working/verified-[project].md
├─ Process Capture Agent → docs/working/process-log-[project].md
└─ Privacy Specialist FINAL GATE
   └─ If approved: Single commit to public repo (case study only)
```

---

## What We Learned (Phase 1 Failure)

**The Mistake:** Built an entire Phase 2 (multi-layer architecture, 5 process archives, 21 timeline pages, all new templates) based on extraction content patterns, completely ignoring the manifest.

**The Result:** Case studies didn't match what each project actually is. Got pushed to GitHub. Wrong.

**The Lesson:** Extraction content is *evidence*, not *intent*. Manifest is intent. Must be primary.

**How We Fixed It:** Designed specialist agents where each one owns a single piece of the problem. No generalist making all decisions.

---

## What's Different This Time

1. **Manifest-first, not extraction-first** — Mission anchors narrative
2. **Privacy gate before public** — No sensitive data in repo
3. **Specialists, not generalists** — Each agent owns one piece
4. **Process captured in real-time** — Colophon updates as work happens
5. **Enforcement gates between stages** — Can't skip steps, can't do it all yourself

---

## Questions This Rebuild Will Answer

- Can a specialist architecture actually prevent the mistakes a generalist makes?
- Will manifest-first narrative avoid extraction-driven generic language?
- Can Privacy Specialist catch what shouldn't be public?
- Will Process Capture Agent keep methodology honest?
- What fails? What works? What did we not anticipate?

---

## The Real Work Ahead

8 core projects to rebuild:
- Tier 1: Savepoint Protocol, Order of the Aetherwright
- Tier 2: Aiden Jae, Encore, Modernist Homestead
- Tier 3: Echo & Bone, MathOnTape, Photogeography

Each one: manifest-first, timeline-sourced, privacy-gated, specialist-built.

---

## Process Log

### 2026-02-05 (Planning)
- Identified failure: Phase 2 pushed to GitHub with misaligned narratives
- Root cause: Extraction content was primary, manifest was secondary
- Solution designed: 6-specialist architecture with manifest-first principle
- Colophon approach: Working document updated as execution proceeds
- Privacy protection: No extraction timelines in public repo, all work local
- Next: Design Process Capture Agent prompts
