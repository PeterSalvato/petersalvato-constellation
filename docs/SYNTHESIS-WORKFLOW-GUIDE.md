# NotebookLM Synthesis Workflow Guide

## Overview

The NotebookLM synthesis workflow is the **Timeline Narrator Specialist** in automated form.

Instead of manually reading 8000-line extraction timelines to identify narrative arcs, NotebookLM reads both the manifest mission (what it should be) and the extraction timeline (what actually happened), then synthesizes the story connecting them.

**Result:** Structured narrative outline with source citations, ready for Master Builder Copywriter.

---

## The Workflow

### Input
- **Manifest entry:** Mission statement + why + defense against drift
- **Extraction timeline:** 5000-8000 lines of chronological project events

### Process
1. NotebookLM reads both sources together
2. Identifies narrative arc (conception → pivots → resolution)
3. Marks key moments with timeline references
4. Validates against manifest mission
5. Returns structured synthesis

### Output
- `docs/working/outline-[project].md`
  - Raw synthesis response
  - Structured timeline arc
  - Evidence citations
  - Manifest alignment notes

---

## Step-by-Step Execution

### Week 1: Authentication (One-time, 5 minutes)

```bash
cd ~/.claude/notebooklm-mcp
source venv/bin/activate
notebooklm-mcp-auth --file
```

Follow the guided steps. This extracts and caches your authentication tokens.

**Result:** `~/.notebooklm-mcp/auth.json` (valid for ~1 week)

### Week 1: First Project Test

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python3 docs/synthesis-workflow.py savepoint-protocol
```

**Output:**
```
======================================================================
NotebookLM Synthesis: savepoint-protocol
======================================================================

Loading manifest and timeline...
✓ Manifest loaded: Savepoint Protocol
✓ Timeline loaded: 45000 characters

[1/4] Creating NotebookLM notebook...
✓ Notebook: 6082e8a2-6c8e-451d-8499-785f09dc0f5e

[2/4] Adding manifest source...
✓ Manifest added

[3/4] Adding extraction timeline...
✓ Timeline added

[4/4] Running synthesis query...
✓ Synthesis complete

✓ Outline written: docs/working/outline-savepoint-protocol.md

Next: Pass outline to Master Builder Copywriter
```

### Week 1: Run for All 8 Projects

```bash
for project in savepoint-protocol order-of-the-aetherwright aiden-jae encore modernist-homestead echo-and-bone mathontape photogeography; do
  echo "=== Synthesizing $project ==="
  python3 docs/synthesis-workflow.py "$project"
done
```

**Time:** ~20-25 minutes (3 minutes per project including NotebookLM processing)

**Result:** 8 outline files ready for Master Builder

---

## What NotebookLM Synthesis Does

### Example: Savepoint Protocol

**Input - Manifest:**
```
Mission: Capture semantic turning points where thinking shifts
Why: Your thinking matters more than your data
Defense: Stays symbolic (markup language, not platform)
```

**Input - Timeline (excerpt):**
```
Line 145: Initial problem - thinking was disappearing, not captured
Line 234: First attempt - simple tagging system
Line 412: Key pivot - realized need for "inflection points" not just notes
Line 567: Designed markup language structure
Line 689: First real usage showed the pattern work
Line 801: Evolved to full authorship infrastructure
```

**NotebookLM Synthesis:**
```
The story of Savepoint Protocol:

Started with a real problem: Peter's thinking was happening but not being
captured structurally. Notes weren't enough—he needed to mark where thinking
*changed*, not what he thought.

Timeline shows the evolution:
- First attempts were tagging systems (too generic)
- Key insight (line 412): The system isn't about capturing everything; it's about
  marking *turning points* where realization clicked
- This led to designing a markup language that could encode those moments
- Design proved itself in real usage (line 689+)

The manifest mission ("Capture semantic turning points") was proven by the timeline:
- System survives by staying symbolic (no platform lock-in)
- Works for both human authors and LLMs reading it
- Degrades gracefully if tools change

This is narrative solvency: the timeline evidence validates the manifest mission.
```

**Output - Outline File:**
```markdown
# savepoint-protocol - Narrative Outline

Generated: 2026-02-XX

## Raw Synthesis Response
[Full NotebookLM response above]

## Timeline for Master Builder Copywriter

The events and arc identified:
- Problem: Thinking disappearing (line 145)
- First attempts: Generic tagging (line 234)
- Pivot: Realized need for inflection marking (line 412)
- Design: Markup language created (line 567)
- Validation: Real-world usage proves it works (line 689+)

## Next Step
Pass this outline to Master Builder with the source timeline.
Master Builder will write the case study in three parts:
1. Here is the system (what it is)
2. Here is why I needed to make it (the constraint)
3. Here is how I did it (chronological from timeline arc)
```

---

## Integration with Specialist Workflow

### Timeline Narrator Specialist (Automated)

```bash
# Run synthesis for [project]
python3 docs/synthesis-workflow.py [project-slug]

# Creates: docs/working/outline-[project].md
# Signature: docs/working/SPECIALIST-timeline-narrator-[project].sig
# Process log: Updated in docs/working/process-log-[project].md
```

### Master Builder Copywriter Specialist (Next Step)

Receives:
- Manifest context (`docs/working/context-[project].md`)
- Timeline outline (`docs/working/outline-[project].md`)
- Original timeline (`docs/extraction_timelines/[project]-timeline.md`)

Writes:
- Case study (`docs/working/draft-[project].md`)

---

## Why NotebookLM Works for This

1. **Reads both manifest AND timeline together**
   - Not extraction-first (the original failure)
   - Not manifest-only (unrealistic)
   - Both as equals → story emerges from the intersection

2. **Preserves source fidelity**
   - References specific timeline moments
   - Can verify each claim against source
   - Prevents invented details

3. **Validates narrative against mission**
   - Does timeline evidence prove manifest claims?
   - Are there gaps between intention and reality?
   - Where did the arc actually go?

4. **Scales efficiently**
   - 3 minutes per project
   - All 8 projects in one session
   - No manual reading of 5000-8000 line timelines

---

## Troubleshooting

### "Authentication expired"
```bash
cd ~/.claude/notebooklm-mcp && source venv/bin/activate
notebooklm-mcp-auth --file
```

### Script hangs on "Adding timeline"
- Timeline is too large (>50MB)
- Solution: Use first 5000 lines only, or split into sections
- Edit synthesis-workflow.py to truncate timeline if needed

### NotebookLM response is generic
- Manifest or timeline too brief
- Solution: Ensure extraction timeline has sufficient detail
- Or manually add context notes to manifest

### Synthesis takes >10 minutes per project
- Normal if NotebookLM is processing
- May indicate very large timeline
- Try with first 5000 lines as test

---

## Files Reference

**Scripts:**
- `docs/synthesis-workflow.py` - Main Timeline Narrator tool
- `~/.claude/notebooklm-mcp/` - MCP installation

**Documentation:**
- `docs/COMPLETE-REBUILD-PLAN.md` - Full specialist architecture
- `docs/NOTEBOOKLM-AUTH-SETUP.md` - Authentication guide
- `docs/SYNTHESIS-WORKFLOW-GUIDE.md` - This file

**Outputs (per project):**
- `docs/working/context-[project].md` - Manifest context
- `docs/working/outline-[project].md` - Synthesis + arc
- `docs/working/draft-[project].md` - Case study (Master Builder)

---

## Next Week Checklist

When tokens refresh and you're ready to execute:

- [ ] Authenticate: `notebooklm-mcp-auth --file` (5 min)
- [ ] Test: `python3 docs/synthesis-workflow.py savepoint-protocol` (3 min)
- [ ] Run all 8 projects (25 min)
- [ ] Review outlines for quality (30 min)
- [ ] Launch Master Builder Copywriter agents (day 2+)

**Total:** ~1 hour to synthesize all 8 outlines

Then Master Builder writes the case studies (~2-3 hours for all 8).

---

## Questions Before Launch?

Before tokens refresh next week, verify:
1. Do we have the Savepoint timeline? ✓
2. Is mainfest.json complete for all 8 projects? (Check for [PENDING] entries)
3. Is extraction timeline comprehensive enough for synthesis to work?
4. Any projects missing from manifest or timeline?

Resolve these NOW so execution is clean next week.
