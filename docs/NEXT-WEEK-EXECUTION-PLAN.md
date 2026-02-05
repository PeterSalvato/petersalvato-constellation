# Next Week Execution Plan (When Tokens Refresh)

**Written:** 2026-02-05 (93% token usage)
**For:** Week of 2026-02-10 (tokens refresh)
**Status:** Ready to execute immediately

---

## What We Decided This Week

### The Core Change: NotebookLM for Synthesis

**What was working:** Specialist agent architecture (Manifest Context → Privacy → Timeline Narrator → Master Builder → Alignment Verifier)

**What wasn't working:** Manual timeline narrative extraction

**Solution:** Use NotebookLM to synthesize narrative arcs from manifest + extraction timeline

**Why:**
- Manifest first (prevents extraction-driven narrative failure)
- Timeline grounded (evidence-based story)
- Source citations (can verify each claim)
- Scaled efficiency (3 min per project vs manual reading)

### The Tool: `synthesis-workflow.py`

A simple Python script that:
1. Loads manifest entry + extraction timeline
2. Creates NotebookLM notebook with both
3. Queries: "What is the story?"
4. Returns structured outline
5. Writes to `docs/working/outline-[project].md`

**Usage:**
```bash
python3 docs/synthesis-workflow.py savepoint-protocol
python3 docs/synthesis-workflow.py aiden-jae
# ... etc for all 8 projects
```

**Time:** 3 minutes per project, ~25 minutes total for all 8

---

## The Files We Created This Week

### Documentation
1. **`docs/COMPLETE-REBUILD-PLAN.md`** (updated)
   - Full specialist architecture
   - Timeline Narrator now uses NotebookLM synthesis
   - Quality gates, enforcement mechanisms
   - Ready to reference during execution

2. **`docs/NOTEBOOKLM-AUTH-SETUP.md`** (new)
   - Step-by-step authentication
   - Troubleshooting guide
   - Auth refresh instructions

3. **`docs/SYNTHESIS-WORKFLOW-GUIDE.md`** (new)
   - Complete workflow walkthrough
   - Example of Savepoint Protocol synthesis
   - Integration with specialist workflow
   - Execution checklist for next week

4. **`docs/NEXT-WEEK-EXECUTION-PLAN.md`** (this file)
   - What to do first when tokens refresh
   - Checklist before starting
   - Expected outcomes

### Code
1. **`docs/synthesis-workflow.py`** (new)
   - Timeline Narrator Specialist tool
   - Handles manifest loading, timeline loading, NotebookLM queries
   - Outputs structured outlines
   - Ready to use immediately after auth

---

## Next Week: Step-by-Step

### Step 1: Authenticate (5 minutes, do this first)

```bash
cd ~/.claude/notebooklm-mcp
source venv/bin/activate
notebooklm-mcp-auth --file
```

This will guide you through Chrome DevTools cookie extraction.

**Result:** `~/.notebooklm-mcp/auth.json` (valid for ~1 week)

### Step 2: Verify Manifest Completeness

Check that all 8 projects have complete manifest entries:

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
jq '.site_manifest[] | .projects[] | select(.mission_statement == "[PENDING - NEEDS EXTRACTION FROM CONVERSATIONS]")' docs/mainfest.json
```

**Expected:** No results (all missions defined)

**If there are [PENDING] entries:**
- Fill in manually from project knowledge, OR
- Extract from conversation archives using substance-extraction skill

### Step 3: Test First Project

```bash
python3 docs/synthesis-workflow.py savepoint-protocol
```

**Expected output:**
```
✓ Manifest loaded: Savepoint Protocol
✓ Timeline loaded: [X] characters
[1/4] Creating NotebookLM notebook...
[2/4] Adding manifest source...
[3/4] Adding extraction timeline...
[4/4] Running synthesis query...
✓ Outline written: docs/working/outline-savepoint-protocol.md
```

**Check the result:**
```bash
head -100 docs/working/outline-savepoint-protocol.md
```

Review the synthesis. Does it:
- Follow manifest mission? ✓
- Reference timeline events? ✓
- Identify actual arc? ✓
- Make sense for Master Builder input? ✓

### Step 4: Run All 8 Projects

```bash
cd /home/peter/homelab/projects/active/petersalvato.com

for project in \
  savepoint-protocol \
  order-of-the-aetherwright \
  aiden-jae \
  encore \
  modernist-homestead \
  echo-and-bone \
  mathontape \
  photogeography
do
  echo "=== $project ==="
  python3 docs/synthesis-workflow.py "$project"
  echo ""
done
```

**Time:** ~25 minutes (3 min/project)

**Result:** 8 outline files in `docs/working/outline-*.md`

### Step 5: Spot-Check Quality

Review 2-3 randomly selected outlines:

```bash
# Random samples
cat docs/working/outline-aiden-jae.md | head -150
cat docs/working/outline-encore.md | head -150
cat docs/working/outline-echo-and-bone.md | head -150
```

For each, verify:
- [ ] Synthesis reads both manifest AND timeline
- [ ] Specific events referenced (with line numbers)
- [ ] Arc is chronological
- [ ] Conclusion ties back to manifest mission

### Step 6: Launch Master Builder Copywriter

Once all 8 outlines are solid, dispatch Master Builder Copywriter agents:

```bash
# For each project, run Master Builder with:
# Input: context spec + outline
# Output: docs/working/draft-[project].md
```

The Master Builder will:
1. Read context spec (from Manifest Context Specialist)
2. Read outline (from NotebookLM synthesis)
3. Write three-part case study:
   - The System (100-150 words)
   - Why I Needed It (300-500 words)
   - How I Did It (800-1200 words)

---

## Checklist Before You Start Next Week

- [ ] Do you have fresh auth cookies ready? (from Chrome DevTools)
- [ ] Is mainfest.json complete? (no [PENDING] entries)
- [ ] Are all extraction timelines in `docs/extraction_timelines/`?
- [ ] Have you read `docs/COMPLETE-REBUILD-PLAN.md`? (full context)
- [ ] Have you read `docs/SYNTHESIS-WORKFLOW-GUIDE.md`? (workflow overview)
- [ ] Do you understand the three-part narrative structure? (System → Why → How)
- [ ] Do you know where Master Builder voice is defined? (`docs/voice-protocol.md`)

---

## Expected Outcomes

### After Step 4 (All 8 syntheses):
- 8 outline files with synthesis + arc + evidence
- All grounded in manifest + extraction timeline
- Ready for Master Builder input

### After Master Builder completes:
- 8 case study drafts in `docs/working/draft-*.md`
- Three-part narrative structure
- Master Builder voice consistent
- Ready for Alignment Verifier

### After Alignment Verifier + Privacy gates:
- 8 verified case studies approved for public
- No sensitive data exposed
- Narratives validated against manifest
- Ready for single commit to GitHub

### Final Deliverable:
- 8 rebuilt case studies
- Complete narrative solvency (story + evidence + structure)
- Colophon updated with process captures
- Ready to push to public GitHub

---

## If Something Goes Wrong

### "Authentication expired"
```bash
cd ~/.claude/notebooklm-mcp && source venv/bin/activate
notebooklm-mcp-auth --file
```

### Script hangs
- Wait 30 seconds (NotebookLM processing)
- If >5 min, cancel and check timeline size

### Synthesis is generic
- Check that extraction timeline has good detail
- Manifest mission is clear enough
- Try with test project first

### Need to debug
```bash
# Check auth cache
cat ~/.notebooklm-mcp/auth.json | jq '.cookies | keys'

# Test NotebookLM connection directly
cd ~/.claude/notebooklm-mcp && source venv/bin/activate
python3 -c "from notebooklm_mcp.api_client import NotebookLMClient; print('✓ MCP works')"
```

---

## Architecture Summary (For Reference)

The complete workflow:

```
MANIFEST (what it should be)
    ↓
MANIFEST CONTEXT SPECIALIST
    ↓ outputs: context-[project].md
    ↓
EXTRACTION TIMELINE (what actually happened)
    ↓
TIMELINE NARRATOR SPECIALIST (NotebookLM synthesis)
    ↓ outputs: outline-[project].md
    ↓
MASTER BUILDER COPYWRITER SPECIALIST
    ↓ outputs: draft-[project].md
    ↓
ALIGNMENT VERIFIER SPECIALIST
    ↓ outputs: verified-[project].md or REDLINE
    ↓
PRIVACY SPECIALIST (FINAL GATE)
    ↓ outputs: APPROVED or REJECT
    ↓
COMMIT TO PUBLIC REPO
    ↓
Updated website with complete narratives
```

Each specialist does ONE thing and passes structured output to the next.

---

## What This Week's Work Enabled

1. **Direct API approach rejected** (too complex)
2. **MCP approach accepted** (proved it works)
3. **Synthesis workflow defined** (`synthesis-workflow.py`)
4. **Integration documented** (complete rebuild plan updated)
5. **Authentication guide created** (ready for next week)
6. **Execution checklist ready** (no ambiguity)

---

## Questions to Ask Yourself Before Launch

1. **Do you want to synthesize all 8 in one session, or batch them?**
   - All at once: 25 min, simpler
   - Batched: Spread over multiple days, less intensive

2. **Do you want me to handle Master Builder dispatch, or will you?**
   - I can: Easier continuity, one session
   - You will: Gives you control, can iterate per project

3. **Any projects with particularly sparse timelines?**
   - May need extra context in manifest
   - May need to expand timeline first

4. **Should Process Capture Agent run during this?**
   - Recommended: Captures actual workflow for Colophon
   - Can be added on-the-fly next week

---

## Success Criteria

You know next week is successful when:

- [ ] All 8 outlines generated without errors
- [ ] Each outline shows manifest mission → timeline evidence → arc
- [ ] Master Builder successfully writes from outlines
- [ ] Alignment Verifier approves without major redlines
- [ ] Privacy Specialist approves all copies
- [ ] Single commit to public repo with all 8 case studies
- [ ] Website updates with complete narratives

---

## Final Note

Everything is documented. Everything is ready.

The only thing blocking execution is:
1. Fresh NotebookLM auth (5 min setup)
2. Tokens tomorrow afternoon

Come back next week with fresh tokens, run `notebooklm-mcp-auth --file`, then execute the synthesis workflow.

The plan will execute cleanly.

Good luck.
