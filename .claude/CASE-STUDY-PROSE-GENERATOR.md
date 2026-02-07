---
name: Case-Study-Prose-Generator
description: Generate case study prose from narrative skeletons using Craftsman Voice Protocol - grounded in actual conversation moments, show don't tell
---

# Case Study Prose Generator

## Purpose

Transform narrative skeletons (extracted moments, constraints, arc) into full case study prose (800-1200 words) using the Craftsman Voice Protocol. Each case study shows the thinking evolution through actual conversation snippets, grounded in constraint and consequence.

## Input Requirements

### Skeleton File
Located in `docs/case-study-skeletons/{project}-skeleton.json`

Contains:
- `project`: Project name
- `constraint`: The specific problem driving the work
- `arc`: Chronological array of moments with:
  - `type`: genesis, realization, problem, pivot, refinement, integration, validation, artifact
  - `snippet`: Actual quote from conversation
  - `platform`: claude, gemini, chatgpt
  - `timestamp`: ISO datetime
  - `content`: Full conversation excerpt (if available)

### Voice Protocol
Reference: `COPYWRITING-VOICE-PROTOCOL.md`

Core principle: **Show, don't tell. Lead with action. Ground everything in consequence.**

Key rules:
- Lead with what was built, not why it was needed
- Use concrete verbs (hold, break, craft, land, drifts) not abstract ones (leverage, implement, optimize)
- Show consequence through actual moments, not explanation
- Speak as craftsman mentor to apprentice: "you" for demonstration, "I" for authority
- Use material/structural language: scaffold, fidelity, joints, structure, load
- No theater, hype, or aspiration — only what actually happened

## Generation Process

### Step 1: Analyze the Skeleton
- Extract the constraint (driving problem)
- Map the arc (what moments show the evolution)
- Identify inflection points (where thinking shifted)
- Note the validation (proof it worked)

### Step 2: Structure the Prose (800-1200 words)

**Opening (1-2 sentences):**
- Lead with what was built: "I built X to solve Y"
- Reference the constraint directly
- No explanation, just demonstration

**Body (4-6 sections, following arc):**
- **The Problem** (show, don't explain):
  - Use arc moments that show the gap
  - Quote from actual snippets where relevant
  - Show what didn't work and why

- **The Pivot(s)** (show the thinking shift):
  - Use "realized" and "shift" moments from arc
  - Ground in actual conversation content
  - Show what changed and why

- **The Solution** (show structural choices):
  - Use integration/refinement moments
  - Ground in material/structural language
  - Explain through consequence, not theory

- **Validation** (show it survived):
  - Use artifact/validation moments
  - Prove through what actually happened
  - Reference constraints it solved

**Closing (2-3 sentences):**
- What this taught about the craft
- Why it matters (through demonstration)
- No summary, no explanation

### Step 3: Apply Craftsman Voice Protocol

**For each paragraph:**
- ✅ Does it show action? Or explain process?
- ✅ Does it use concrete verbs?
- ✅ Does it ground in actual moments/snippets?
- ✅ Can you hear it spoken?
- ✅ Is it mentor-to-apprentice tone?

**Red flags (revise if present):**
- ❌ "The approach was to..." → Replace with action
- ❌ "This ensures..." → Replace with consequence
- ❌ "Best practices suggest..." → Replace with "what happened"
- ❌ "We believe..." → Replace with "I learned..."
- ❌ Any hype language: revolutionary, innovative, best-in-class, paradigm

### Step 4: Ground in Skeleton Evidence

Every claim must trace back to arc moments:
- Reference actual snippets from conversations
- Use timestamps to show progression
- Show platform diversity (claude, gemini, chatgpt)
- Make thinking evolution visible through moments

## Output Format

**File location:** `docs/case-study-prose/{project}-prose.md`

**File structure:**
```markdown
# {Project Name}

{Prose: 800-1200 words in Craftsman Voice}

---

## Narrative Sources

- **Moments extracted:** N
- **Platforms:** Claude, Gemini, ChatGPT
- **Timeline span:** YYYY-MM-DD to YYYY-MM-DD
- **Constraint:** [Direct quote of driving problem]
```

## Quality Checklist

Before publishing, verify:

- ✅ Prose is 800-1200 words
- ✅ Opens with "I built..."
- ✅ Every claim grounded in arc moment
- ✅ No abstract explanations (all show-don't-tell)
- ✅ Craftsman voice throughout (can hear it spoken)
- ✅ Material language used (scaffold, fidelity, joints, structure)
- ✅ Shows thinking evolution (pivots, realizations)
- ✅ Shows validation (survived this constraint)
- ✅ No hype, theater, or aspiration
- ✅ Mentor-to-apprentice tone maintained

## Example Application

**Skeleton input:** savepoint-protocol-skeleton.json
- Constraint: "Capture semantic turning points where thinking shifts"
- Arc: 6 moments showing genesis → problem → pivot → solution → validation

**Prose output (excerpt):**
> I built a markup language to mark where my thinking changed. Not what I thought—where the understanding shifted. Tagging systems don't capture that moment. They capture outcomes. But the real work is knowing when you realized something.
>
> The problem emerged when I noticed my own notes: I had timestamps for decisions but not for realizations. The gap between them is where the thinking happened. If you lose that, you lose the rigor...

## Integration

### Use When
- Generating case study prose from narrative skeletons
- Needing to apply Craftsman Voice consistently across projects
- Creating reusable content for portfolio/colophon
- Matching tone across multiple case studies

### Reuse For
- Colophon project case studies
- Future project documentation
- Portfolio refinement and voice consistency checks
- Any content needing Craftsman Voice + evidence grounding

## Related Assets
- `COPYWRITING-VOICE-PROTOCOL.md` — Full voice rules and examples
- `AGENT-COPYWRITING-VOICE.md` — How to use the copywriting voice agent
- `/docs/case-study-skeletons/` — Input skeleton files (17 projects)
- `/docs/extraction-output/` — Timeline data supporting skeletons
