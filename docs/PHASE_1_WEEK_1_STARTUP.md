# Phase 1 Week 1 Startup Guide
## Content Architecture, Extraction Mining, Manifesto Draft

**Week:** 1 of 4 (2026-02-10 to 2026-02-16)
**Effort:** 13-17 hours
**Deliverables:** 3 (architecture, mining, manifesto draft)
**Checkpoint:** Friday 2026-02-16

---

## What Week 1 Accomplishes

By end of Friday, you'll have:
1. **Content Architecture Template** — The structure every rebuilt case study will follow
2. **Extraction Mining Complete** — 25-50 key quotes per project identified
3. **Manifesto Statement Draft** — New opening that claims actual positioning

These three things are the foundation for Weeks 2-3 case study rebuilds.

---

## Task 1.1: Develop Content Architecture Template

**Time:** 3-4 hours
**What:** Define the narrative structure that rebuilt case studies will follow

### Your Assignment

Open `/home/peter/homelab/projects/active/petersalvato.com/docs/PHASE_1_IMPLEMENTATION_PLAN.md`

Go to section "Task 1.1: Establish Content Architecture"

Review the proposed 6-section structure:
```
1. OPENING STATEMENT (what problem?)
2. THE THINKING (why this approach?)
3. THE BUILDING (how built + extraction citations)
4. WHAT SURVIVED (process visibility)
5. THE SYSTEM (narrative+visual+technical unified)
6. THE LEARNING (what would you do differently?)
```

### Your Decision

**Question 1:** Does this structure work for your projects?
- If yes: Use it as-is
- If no: Modify it (what would work better?)

**Question 2:** For each section, what should be visible?
- Opening Statement: Problem statement only, or also why it matters?
- The Thinking: Constraints only, or also alternatives considered?
- The Building: All decisions, or only major pivots?
- What Survived: Successes only, or also failures/refinements?
- The System: Final state only, or also evolution?
- The Learning: Personal lessons, or also applicability to other work?

### Deliverable for Task 1.1

A finalized content architecture template documented as:
```markdown
# Content Architecture Template

Each rebuilt case study will follow this structure:

## 1. OPENING STATEMENT
[Your decision on what goes here]

## 2. THE THINKING
[Your decision on what goes here]

[... etc for all 6 sections ...]
```

Save as: `/docs/CONTENT_ARCHITECTURE_TEMPLATE.md`

---

## Task 1.2: Mine Extraction for Key Moments

**Time:** 8-10 hours
**What:** Identify 3-5 critical thinking moments per project from extraction timelines

### Your Assignment

For each of 5 projects:
1. Savepoint Protocol
2. Modernist Homestead
3. Aiden Jae
4. New City
5. Order of Aetherwright

**Do this:**

1. Open the project's timeline file (located in `/docs/extraction_timelines/`)
   - Example: `savepoint-protocol-timeline.md`

2. Read through blocks, looking for:
   - ✓ Major pivots or direction changes
   - ✓ Constraint problems being solved
   - ✓ Why something chosen over alternatives
   - ✓ Failure points and recovery
   - ✓ "Aha moments" where thinking shifts
   - ✓ Cross-project connections

3. For each key moment found, copy these details:
   - **Timestamp:** Date from the block header (e.g., 2024-04-12)
   - **Verbatim Quote:** Exact text from conversation (8-12 sentences)
   - **Context:** What conversation/topic was this part of?
   - **Why It Matters:** Why does this illuminate the project?
   - **Section It Maps To:** Which architecture section does it fit? (1-6)

4. Aim for **5-10 quotes per project** (5 projects = 25-50 total)

### Example Format

```markdown
# Savepoint Protocol - Key Extraction Moments

## Moment 1: Cognitive Turning Point Discovery
**Date:** 2024-10-15
**Maps To:** Section 2 (The Thinking)
**Verbatim Quote:**
> "The key insight was that these turning points aren't just moments of clarity—they're structural inflection points where the person's entire cognitive framework shifts. The savepoint isn't capturing the moment; it's capturing the transformation that happened."

**Context:** Discussion about what differentiates Savepoint from regular note-taking
**Why It Matters:** Shows the core problem being solved—transformation, not documentation

---

## Moment 2: [Continue for each moment...]
```

### Deliverable for Task 1.2

Create a new file: `/docs/EXTRACTION_MINING_RESULTS.md`

Format:
- Heading: Project name
- Subheadings: Each key moment (Moment 1, Moment 2, etc.)
- For each: Date, maps-to, quote, context, why-it-matters

**Total:** 25-50 quotes across 5 projects

---

## Task 1.3: Draft New Manifesto Statement

**Time:** 2-3 hours
**What:** Rewrite homepage manifesto to claim actual positioning

### Current Manifesto (Outcome-Focused)

> "I work at the intersection of classical design and full-stack engineering. The systems I build serve creative teams and neurodivergent founders who need structural support—not another SaaS dependency, but infrastructure they can own and operate.
>
> This site indexes that work, organized by intent: the governing logic, the production deployments, and the creative practice."

### Your Assignment

Rewrite this to:
1. **Claim "Narrative Infrastructure Architect" positioning** (not just "systems architect")
2. **Make thinking/process visible** (not just outcomes)
3. **Explain extraction content** (what's on the site, why it's there)
4. **Maintain Master Builder voice** (direct, concrete, no jargon, no aspiration)
5. **Keep it brief** (2-3 short paragraphs max)

### What Should Be Different

**Before (What You Do):**
> "I work at the intersection of classical design and full-stack engineering"

**After (How You Think):**
> "I build narrative infrastructure—systems where brand story and technical architecture work as one"

**Before (Who You Serve):**
> "The systems I build serve creative teams and neurodivergent founders"

**After (What You Solve):**
> "I solve the constraint problem: how does meaning survive deployment?"

**Before (What's on Site):**
> "This site indexes that work, organized by intent"

**After (Why Site Looks Different):**
> "This site shows both the work and the thinking—3+ years of iterative work, decision-making, failed experiments, and what survived. Not just deliverables. The methodology visible."

### Draft Guidelines

✓ Do this:
- Start with the actual problem you solve
- Show that thinking is visible/accessible
- Reference that extraction content is on the site
- Use concrete vocabulary (build, hold, structure, constraint)
- Sound like you talking to someone you respect

✗ Don't do this:
- Marketing language ("cutting-edge," "innovative," "passionate")
- Jargon without earning it
- Aspirational tone
- Third-person reference (always "I")
- Long sentences with multiple clauses

### Tone Test

Read your draft out loud. Ask: "Would I say this to a peer I respect?"
- If yes: Good
- If no: Rewrite until yes

### Deliverable for Task 1.3

Create a new file: `/docs/MANIFESTO_DRAFT.md`

Format:
```markdown
# New Manifesto Statement (Draft)

## Current Manifesto (For Reference)
[Current text here]

## New Manifesto (Proposed)
[Your new text here, 2-3 short paragraphs]

## What Changed
- Claim: From "systems architect" to "narrative infrastructure architect"
- Visibility: From outcomes-only to outcomes+thinking
- Explanation: From "work indexed by intent" to "work showing methodology"

## Voice Notes
[Any notes on maintaining voice, avoiding pitfalls, etc.]
```

---

## How to Do This Week

### Time Allocation

- **Monday-Tuesday (2/10-2/11):** Task 1.1 (Content Architecture) - 3-4 hours
- **Tuesday-Thursday (2/11-2/13):** Task 1.2 (Extraction Mining) - 8-10 hours
  - Monday 2/10-2/11: Savepoint Protocol + Modernist Homestead
  - Wednesday 2/12: Aiden Jae
  - Wednesday-Thursday 2/12-2/13: New City + Aetherwright
- **Thursday (2/13):** Task 1.3 (Manifesto Draft) - 2-3 hours
- **Friday (2/14-2/16):** Buffer for completion + review

### Working Environment

```bash
# Open your terminal
cd /home/peter/homelab/projects/active/petersalvato.com

# Have these files open simultaneously:
# 1. /docs/PHASE_1_IMPLEMENTATION_PLAN.md (reference)
# 2. /docs/extraction_timelines/ (source material)
# 3. Text editor for writing deliverables
# 4. /docs/voice-protocol.md (maintain voice)
```

### Where to Save Deliverables

All Week 1 outputs go in `/docs/`:
- `CONTENT_ARCHITECTURE_TEMPLATE.md`
- `EXTRACTION_MINING_RESULTS.md`
- `MANIFESTO_DRAFT.md`

Then commit to git:
```bash
git add docs/CONTENT_ARCHITECTURE_TEMPLATE.md
git add docs/EXTRACTION_MINING_RESULTS.md
git add docs/MANIFESTO_DRAFT.md
git commit -m "feat: Phase 1 Week 1 - Content architecture, extraction mining, manifesto draft"
```

---

## Quality Checklist for Week 1

### For Content Architecture Template
- ✓ 6 sections defined (or your modified version)
- ✓ Each section has clear guidance on what goes there
- ✓ Template is reusable for all 5 projects
- ✓ Decisions documented for why this structure works

### For Extraction Mining
- ✓ 25-50 total quotes collected (5+ per project)
- ✓ Each quote is verbatim from timeline file (no paraphrasing)
- ✓ Each quote has: date, context, why-it-matters, section-mapping
- ✓ Quotes are substantial (8-12 sentences each, not one-liners)
- ✓ Quotes illuminate thinking, not just outcomes

### For Manifesto Draft
- ✓ Claims "narrative infrastructure architect" positioning
- ✓ Makes thinking/process visible
- ✓ Explains extraction content existence
- ✓ Maintains Master Builder voice (read-aloud test passes)
- ✓ 2-3 short paragraphs (concise, not verbose)

---

## Checkpoint 1: Friday 2026-02-16

**Review these 3 deliverables:**

1. **CONTENT_ARCHITECTURE_TEMPLATE.md**
   - Does this structure work?
   - Any modifications needed?
   - Ready to use for Week 2?

2. **EXTRACTION_MINING_RESULTS.md**
   - Are quotes substantive?
   - Are they verbatim?
   - Good distribution across 5 projects?
   - Ready to use for Week 2 rebuilds?

3. **MANIFESTO_DRAFT.md**
   - Does it claim actual positioning?
   - Does voice sound right?
   - Does it explain the new site?
   - Ready for integration into homepage?

### Possible Checkpoint Outcomes

**Option A: Approve All Three**
→ Proceed to Week 2 (Case Study Rebuilds)

**Option B: Approve with Minor Revisions**
→ Apply revisions Friday afternoon
→ Proceed to Week 2 Monday

**Option C: Request Significant Changes**
→ Revise based on feedback
→ Re-review when ready
→ Proceed to Week 2 when approved

---

## If You Get Stuck

### On Task 1.1 (Content Architecture)

**Question:** "What should go in Section X?"
**Answer:** Reread the current case study for that project. What's currently there? What's missing?

**Question:** "Is this structure flexible enough?"
**Answer:** Yes. It's a template, not a constraint. Modify it if needed.

**Question:** "What if projects need different structures?"
**Answer:** That's fine. Use one architecture per project if needed. Document why.

### On Task 1.2 (Extraction Mining)

**Question:** "How do I find the key moments?"
**Answer:** Read through timeline blocks. Look for:
- Where does the person change their mind?
- Where do they solve a hard problem?
- Where do they discover something new?
- Where do they explain *why*, not just *what*?

**Question:** "What if I can't find 5-10 quotes per project?"
**Answer:** That's okay. Quality > quantity. Better to have 3 great quotes than 10 weak ones.

**Question:** "Do I need to read ALL blocks?"
**Answer:** No. Skim for key moments. Read those blocks carefully. Extract quotes.

### On Task 1.3 (Manifesto)

**Question:** "How do I claim 'narrative infrastructure architect'?"
**Answer:** Explain what problem you actually solve:
- Not: "I'm a narrative architect"
- Actually: "I solve how stories survive deployment by building systems where narrative, visual, and technical work as one"

**Question:** "How much should I reference extraction content?"
**Answer:** Enough to explain why the site looks different. Something like:
"This site shows both work and thinking—years of decision-making, failed experiments, and what survived visible."

**Question:** "Can I keep some of the current manifesto?"
**Answer:** Yes. Keep what works. Change what doesn't. It should feel like an evolution, not a complete rewrite.

---

## Quick Reference: Files You'll Need

**Read these:**
- `/docs/PHASE_1_IMPLEMENTATION_PLAN.md` (Task details)
- `/docs/voice-protocol.md` (Maintain voice)
- `/docs/extraction_timelines/*.md` (Source material for mining)

**Write these:**
- `/docs/CONTENT_ARCHITECTURE_TEMPLATE.md` (Task 1.1)
- `/docs/EXTRACTION_MINING_RESULTS.md` (Task 1.2)
- `/docs/MANIFESTO_DRAFT.md` (Task 1.3)

**Current site files for reference:**
- `_data/index.json` (current manifesto)
- `_systems/*.md` (current case studies)
- `_protocols/*.md` (current protocol projects)

---

## You've Got This

Week 1 is the foundation. It's mostly thinking work (architecture, mining, writing), not heavy implementation.

By Friday, you'll have everything you need to rebuild the 5 case studies in Week 2.

**Start Date:** Monday, 2026-02-10
**Checkpoint:** Friday, 2026-02-16
**Deliverables:** 3 files documenting architecture, mining, and manifesto draft

Let's go.

---

## Next: Week 2 (2026-02-17)

Once Week 1 is approved, Week 2 begins:
- Rebuild Savepoint Protocol case study (6-8 hours)
- Rebuild Modernist Homestead case study (6-8 hours)

Using:
- Content architecture template (Task 1.1)
- Extraction quotes (Task 1.2)
- New voice guidance (implied by manifesto changes)

But that's Week 2. For now, focus on finishing Week 1 by Friday.
