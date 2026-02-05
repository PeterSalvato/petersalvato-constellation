# Complete Site Rebuild Plan: Manifest-First, Specialist-Driven

**Status:** Ready for execution when tokens refresh
**Start Date:** Week of 2026-02-10 (next available tokens)
**Duration:** 2-3 weeks execution + ongoing Process Capture
**Deliverable:** 8 rebuilt case studies + Living Colophon document

---

## What Failed Last Time

**Phase 2 pushed to GitHub with completely misaligned narratives:**
- Case studies built from extraction content patterns, not manifest missions
- Ignored manifest.json as authoritative source
- 5 process archives + 21 timeline pages + new templates all technically sound but contextually wrong
- Privacy issue: GitHub token exposed in extraction timeline (now redacted)

**Root Cause:** Extraction content was louder/more detailed than manifest intent. Generalist execution failed.

**Solution:** Specialist agents, manifest-first principle, privacy gates, process capture.

---

## The Six-Specialist Architecture

### 1. Manifest Context Specialist

**Purpose:** Extract mission and intent from manifest.json

**Process:**
1. Read project entry in mainfest.json
2. Extract:
   - `mission_statement` — What the system IS
   - `plain_spoken_lesson` — The insight it teaches
   - `defense_against_drift` — How it stays coherent
3. Produce: One-page context spec

**Output File:** `docs/working/context-[project].md`

**Example (Savepoint Protocol):**
```
MISSION: Capture semantic turning points where thinking shifts
LESSON: Your thinking matters more than your data
DEFENSE: Stays symbolic (markup language, not platform)
WHY NEEDED: Thinking was disappearing, not captured structurally
```

**Pass to:** Privacy & Security Specialist

---

### 2. Privacy & Security Specialist

**Purpose:** Screen extraction timelines for personal/sensitive data

**Process:**
1. Read `docs/extraction_timelines/[project]-timeline.md`
2. Scan for:
   - Real names → Flag for anonymization
   - Specific locations → Flag for removal
   - Financial data → Flag for generalization
   - Family details → Flag for anonymization
   - Client/business secrets → Flag for removal
   - Health/sensitive info → Flag for complete removal
3. Produce: Sanitized version + redaction report

**Output Files:**
- `docs/working/sanitized-[project].md` (cleaned timeline)
- `docs/working/redactions-[project].md` (what was removed/why)

**Critical Gate:** "Is this safe for public repo?"
- If NO: Return with redaction report
- If YES: Approve for Timeline Narrator

**Pass to:** Timeline Narrator Specialist

---

### 3. Timeline Narrator Specialist

**Purpose:** Identify narrative arc from sanitized timeline

**Process:**
1. Read `docs/working/sanitized-[project].md` chronologically
2. Identify:
   - When/why was project conceived?
   - How did it evolve over time?
   - What decisions emerged?
   - What survived? What changed?
   - What was the actual arc?
3. Produce: Structured outline (no prose yet)

**Output File:** `docs/working/outline-[project].md`

**Example Structure:**
```
PROJECT: Aiden Jae

TIMELINE ARC:
- Initial conception: Problem with luxury + handmade coherence
- Early exploration: Visual identity experiments
- Key pivot: Realized complete ownership was essential
- Technical decisions: Why Shopify over custom
- Resolution: System proved coherence across brand/visual/technical
```

**Pass to:** Master Builder Copywriter Specialist

---

### 4. Master Builder Copywriter Specialist

**Purpose:** Write case study in Master Builder voice

**Process:**
1. Read: context spec + timeline outline
2. Write three-part narrative:

   **Part 1: The System (100-150 words)**
   - What it IS, stated directly
   - Mission reframed conversationally

   **Part 2: Why I Needed to Make It (300-500 words)**
   - The actual problem/constraint
   - Why this mattered
   - Source: manifest context + timeline context

   **Part 3: How I Did It (800-1200 words)**
   - Chronological story from timeline
   - Follow the actual arc
   - Show decisions, survival, evolution
   - Source: sanitized timeline

3. Voice check: Read aloud. Pass peer test?

**Output File:** `docs/working/draft-[project].md`

**Pass to:** Alignment Verifier Specialist

---

### 5. Alignment Verifier Specialist

**Purpose:** Verify copy matches manifest, not generic patterns

**Process:**
1. Read finished copy against manifest context
2. Check:
   - Does it open with mission from manifest?
   - Does "why" section come from manifest constraint?
   - Does "how" section follow extraction timeline?
   - Any generic process language instead of specific system?
   - Does it explain THIS system, or generic decision-making?
3. Output: Approval or redline

**Output File:** `docs/working/verified-[project].md`

**If Issues Found:**
- Specific: "Rewrite 'The System' section to be less generic"
- Return to: Master Builder Copywriter for revision

**If Approved:**
- Pass to: Privacy Specialist (Final Gate)

---

### 6. Process Capture Agent

**Purpose:** Document actual workflow + user thinking as it happens

**Process:**
Runs BETWEEN each specialist step:

1. Observe specialist output
2. Document:
   - What was supposed to happen (the plan)
   - What actually happened
   - Decisions made in real-time
   - USER'S decisions/thinking shifts
   - Surprises or blockers
   - Process deviations
   - What worked/what didn't

3. Capture USER'S thinking:
   - When user makes a decision
   - Why they made it
   - How understanding shifts as work proceeds
   - Reactions to specialist output
   - Patterns noticed

**Output File:** `docs/working/process-log-[project].md`

**Feeds Into:** Colophon (Living document updated as work happens)

**Example Entry:**
```
[2026-02-XX] Savepoint Protocol - After Timeline Narrator output:
- Timeline showed decision-making was more important than features
- User realized: this validates manifest mission (turning points matter)
- User decision: Emphasize "where thinking shifted" over timeline length
- Process note: Timeline Narrator identified arc perfectly
- User insight: This is Savepoint working on Savepoint (meta)
```

---

### 7. Privacy Specialist (Final Gate)

**Purpose:** Last check before anything goes public

**Process:**
1. Read finished/verified copy
2. Check:
   - Any extraction timeline quoted directly? (NO - should be synthesized)
   - Any personal data remaining? (NO)
   - Any sensitive information? (NO)
   - Safe for public GitHub repo? (YES/NO)

**Output:** Approval or "sections X and Y need revision"

**If Approved:**
- Signals: Ready for single commit to public repo

**If Not Approved:**
- Return to: Master Builder Copywriter with specific issues

---

## The Workflow: Local Only, Public Only When Approved

```
EXECUTION SEQUENCE (All Local, No Commits)

For each project [Savepoint, Aetherwright, Aiden-Jae, Encore, Homestead, Echo-Bone, MathOnTape, Photogeography]:

1. MANIFEST CONTEXT SPECIALIST
   Reads: mainfest.json[project]
   Outputs: docs/working/context-[project].md

2. PROCESS CAPTURE AGENT (Observes)
   Documents: What context specialist found
   Outputs: docs/working/process-log-[project].md
   Captures: Any user decisions about this project

3. PRIVACY & SECURITY SPECIALIST
   Reads: extraction_timelines/[project].md
   Reads: context spec
   Outputs: docs/working/sanitized-[project].md
   Gate Check: Safe for public? YES/NO

4. PROCESS CAPTURE AGENT (Observes)
   Documents: Privacy decisions, redactions, any issues
   Captures: User reactions to what was found/removed

5. TIMELINE NARRATOR SPECIALIST
   Reads: sanitized timeline
   Outputs: docs/working/outline-[project].md

6. PROCESS CAPTURE AGENT (Observes)
   Documents: What arc Timeline Narrator identified
   Captures: User's thinking about narrative flow

7. MASTER BUILDER COPYWRITER SPECIALIST
   Reads: context + outline
   Outputs: docs/working/draft-[project].md

8. PROCESS CAPTURE AGENT (Observes)
   Documents: Draft created, voice quality, any issues
   Captures: User feedback on draft

9. ALIGNMENT VERIFIER SPECIALIST
   Reads: draft vs. manifest
   Outputs: Approval or Redline

10. PROCESS CAPTURE AGENT (Observes)
    Documents: Verification results
    Captures: User decisions about revisions if needed

11. PRIVACY SPECIALIST (FINAL GATE)
    Reads: Verified copy
    Gate Check: Safe for public? YES/NO

12. PROCESS CAPTURE AGENT (Final)
    Documents: Approval status
    Captures: User's thinking as work completes

IF APPROVED BY PRIVACY SPECIALIST:
→ Single commit to public repo: case study only
   (No extraction timelines, no working files, no sensitive data)

IF NOT APPROVED:
→ Revise and cycle back
```

---

## Projects to Rebuild (In Order)

**Tier 1 (Protocols):**
1. Savepoint Protocol
2. Order of the Aetherwright

**Tier 2 (Applied Systems):**
3. Aiden Jae
4. Encore
5. Modernist Homestead

**Tier 3 (Practice):**
6. Echo & Bone
7. MathOnTape
8. Photogeography

**Special Case:**
9. Colophon (See below)

---

## Colophon: Meta-Demonstration

**Updated Mission (from planning session):**

> "Demonstrate the systems that build the site by capturing the site-building process itself. Colophon is proof: here's Savepoint marking where thinking shifts. Here's Aetherwright showing intentional sovereign decision-making. Here's narrative infrastructure being built. Process Capture Agent documents it all, making the methodology visible, not theoretical."

**Colophon is NOT:**
- Technical documentation of how Jekyll works
- Process diagram of specialist agents
- Post-mortem analysis

**Colophon IS:**
- Living record of user thinking as rebuild happens
- Real-time demonstration of systems in practice
- Honest account of what worked, what failed, what surprised
- Meta-proof: these systems actually work

**Source:** `docs/working/process-log-*.md` (all projects) + user decisions

**Update Schedule:** After every 2-3 projects completed, Process Capture Agent synthesizes findings into Colophon update

---

## Enforcement Mechanisms

### 1. Specialist Ownership
Each agent owns ONE piece. Cannot be skipped or combined.

### 2. Output Files as Gates
Next specialist reads PREVIOUS specialist's output file. Cannot proceed without it.

### 3. Process Capture Required
After each specialist: Process Capture Agent documents what happened + user thinking.

### 4. Privacy as Final Gate
Nothing public without Privacy Specialist approval.

### 5. No Commits Until Complete
All work stays local. Single commit only when Privacy Specialist approves.

---

## Quality Checklist Per Project

**Before starting Manifest Context Specialist:**
- [ ] Project in mainfest.json? (manifest entry exists)
- [ ] Mission statement clear? (not [PENDING])
- [ ] Plain spoken lesson identified?
- [ ] Defense against drift specified?

**After Manifest Context Specialist:**
- [ ] Context spec written? (docs/working/context-[project].md exists)
- [ ] Does it answer "what is this system?" clearly?

**After Privacy & Security Specialist:**
- [ ] Redactions justified?
- [ ] No sensitive data remaining?
- [ ] Extraction timeline never goes to public repo?

**After Timeline Narrator Specialist:**
- [ ] Outline follows chronological arc?
- [ ] Shows conception → evolution → resolution?

**After Master Builder Copywriter:**
- [ ] Three-part structure clear? (System, Why, How)
- [ ] Passes read-aloud test?
- [ ] Master Builder voice consistent?

**After Alignment Verifier:**
- [ ] Matches manifest mission?
- [ ] Specific to THIS system (not generic)?
- [ ] No extraction content quoted directly?

**After Privacy Specialist (Final Gate):**
- [ ] Safe for public? YES
- [ ] Ready to commit? YES

---

## Success Criteria

**Phase 2 Rebuild Succeeds If:**

1. **All 8 case studies rebuilt** following manifest-first, specialist-driven approach
2. **Zero misalignment** — Each narrative demonstrably matches its manifest mission
3. **Privacy protected** — No extraction timelines in public repo, no sensitive data exposed
4. **Colophon captures process** — Living document shows actual thinking + workflow
5. **Specialists actually used** — Process Capture Agent proves each specialist ran
6. **Quality gates held** — No generic language slipped through
7. **Systems demonstrated** — Colophon shows Savepoint/Aetherwright/narrative infrastructure working in practice

---

## Known Risks & Mitigations

**Risk 1: Specialists don't actually run (reverting to generalist)**
- Mitigation: Process Capture Agent between every step. Output files required.

**Risk 2: Extraction content still dominates narrative**
- Mitigation: Master Builder Copywriter works from outline only (synthesized), not raw timeline.

**Risk 3: Privacy gate misses something**
- Mitigation: Run TWICE if uncertain. Better safe than exposed.

**Risk 4: Project complexity varies**
- Mitigation: Specialist architecture works for any project type (technical, philosophical, visual, operational).

**Risk 5: Token exhaustion during execution**
- Mitigation: Batch work by tier. Can pause after Tier 1, then Tier 2, then Tier 3.

---

## Next Steps

**When tokens refresh:**

1. Create specialist agent prompts in `/docs/specialists/`
2. Distribute to appropriate agents
3. Start with Tier 1: Savepoint Protocol
4. Run full pipeline on one project as proof-of-concept
5. If successful: Scale to remaining projects
6. Process Capture Agent synthesizes into Colophon every 3 projects

---

## Files Reference

**Source Files (Never Committed):**
- `docs/mainfest.json` — Manifest (mission, why, defense)
- `docs/extraction_timelines/[project]-timeline.md` — Raw timeline (local only)
- `docs/voice-protocol.md` — Voice standards

**Working Files (Local, Never Public):**
- `docs/working/context-[project].md` — Manifest extract
- `docs/working/sanitized-[project].md` — Privacy-cleaned timeline
- `docs/working/redactions-[project].md` — What was removed
- `docs/working/outline-[project].md` — Timeline narrative arc
- `docs/working/draft-[project].md` — Case study draft
- `docs/working/verified-[project].md` — Verified copy
- `docs/working/process-log-[project].md` — Process capture

**Public Files (Only After Privacy Gate):**
- `_protocols/[project].md` — Rebuilt case study (TO REPO)
- `_systems/[project].md` — Rebuilt case study (TO REPO)
- `_practice/[project].md` — Rebuilt case study (TO REPO)

**Living Document:**
- `docs/COLOPHON-WORKING.md` — Updated as rebuild proceeds

---

## This Plan Is Your Insurance

This document prevents another Phase 2 failure by:

1. **Making manifest primary** (not extraction content)
2. **Using specialists** (not generalist mistake-making)
3. **Capturing process** (honest Colophon about what actually happened)
4. **Protecting privacy** (gates before public)
5. **Enforcing gates** (can't skip, can't combine)

**Execution is mechanical:** Follow the workflow, pass between specialists, Process Capture documents, Privacy gates before public.

---

**Ready to execute when tokens refresh.**
