# Case Study Prose System: Discovery & Development

## Problem Statement

How do you generate case study prose that:
- Is grounded in actual project thinking (not inferred or hallucinated)
- Follows consistent voice/tone (Craftsman Voice Protocol)
- Is repeatable across 17+ projects
- Can be documented and taught

## Initial Approaches & Failures

### Approach 1: Automated Skeleton → Prose
**Assumption:** Extract moments from chats into skeleton JSON, then generate prose via LLM

**Result:** Generated fragments, not narrative. Sounded like assembled pieces, not synthesized thinking.

**Why it failed:**
- Tried to automate the synthesis step
- Treated prose generation as a code generation problem (it's not)
- Delegated without verifying
- Lost grounding in actual conversations

### Approach 2: Template-Based Assembly
**Assumption:** Skeleton moments + voice rules = prose through template system

**Result:** Robotic, unmemorable, missed the actual story

**Why it failed:**
- Templates can't capture narrative flow
- Prose writing requires understanding, not pattern-matching
- Human synthesis is necessary, not optional

### Approach 3: Agent Delegation with Claimed Verification
**Assumption:** Dispatch agent, agent rewrites all 16 files, trust the report

**Result:** Claimed quality but didn't actually verify. Files were poor when spot-checked.

**Why it failed:**
- Avoided doing the actual work
- Trusted reports without checking
- Prose writing can't be delegated away
- Verification is essential, not optional

## Key Insight: Skeleton as Index, Not Scaffold

**The breakthrough:** Skeleton JSON isn't intermediate data. It's an **index** into raw chat exports.

Instead of: Skeleton → generate prose

The actual process: **Manifest (story) + Skeleton (index) + Raw Chats (source) → Extract passages → Synthesize prose**

This changes everything because:
- Story is already defined in manifest
- Skeleton tells you WHERE to look in raw chats (timestamps, moment types)
- Raw chats are the evidence
- Extraction is mechanical (find text, copy text, note coordinates)
- Prose synthesis is where human judgment matters

## The Three-Phase System

### Phase 1: Extraction (Mechanical - No Heavy LLM Thinking)
- Input: Skeleton JSON (index) + Raw chat exports (source material)
- Process: For each skeleton moment, find it in raw chats using timestamp/snippet
- Output: Markdown file with all moments in sequence, each with actual chat passages and line numbers
- Goal: Create a bounded, context-complete document that fits in full context

### Phase 2: Prose Synthesis (Where Craft Lives)
- Input: Extraction markdown (complete, grounded, all context included)
- Process: Read extracted passages, understand the story, write prose that demonstrates the manifest story
- Output: Case study prose (900-1200 words)
- Goal: Synthesize passages into coherent narrative using voice protocol

### Phase 3: Generalization & Integration
- Take the extraction tool built for Aetherwright
- Generalize for any skeleton/raw chat combination
- Integrate into Savepoint Protocol as documented, repeatable system
- Make it available for all 17 projects + future work (colophon, etc.)

## Why This Works

**Extraction is mechanical:** Find text in files, copy it, note line numbers. No hallucination possible because you're retrieving, not inventing.

**Prose fits in context:** Once extracted markdown is created, entire project case study material fits in one document. No need to traverse large files or lose context.

**Grounding is built-in:** Every claim in prose can be traced back to line numbers in raw chats. Verification is possible.

**Repeatable process:** Once working for Aetherwright, tool generalizes to any skeleton + raw chats.

## Current Status

**Completed:**
- ✅ Built extraction tool for Order of the Aetherwright
- ✅ Tested with 344 skeleton moments
- ✅ Fixed extraction to be context-manageable (363KB, not 29MB)
  - Smart passage truncation: extracts only snippet + surrounding context
  - Result: 10,131 lines (vs. 765,520 lines in naive extraction)

**In Progress:**
- Synthesize prose from extraction document
- Verify quality against manifest + voice protocol
- Document the process

**Next:**
- Generalize extraction tool for all 17 projects
- Integrate into Savepoint Protocol
- Create prose generation workflow documentation

## Data Architecture

**Raw Exports** (3 platforms, different formats):
- Gemini: `/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json`
- ChatGPT: `/home/peter/homelab/knowledge/exports/data-2026-01-26-15-50-54-batch-0000/conversations.json`
- Claude: `/home/peter/homelab/knowledge/exports/7bb7d7448a4fe8b37c10d84958a3011b01d3dc5d3b4a88cb8a89ceea3ebda027-2026-01-22-18-47-51-f068f48a77d44e359188dc77169ae29d/conversations.json`

**Processing Pipeline**:
Raw Exports → Parse/Ingest → Timelines (by project) → Skeletons (index) → Extraction Tool → Markdown → Prose

**Organized by Project**:
- Timelines: `/docs/extraction-output/{project}-timeline.json` (3,201 conversations indexed by project)
- Skeletons: `/docs/case-study-skeletons/{project}-skeleton.json` (344 moments for Aetherwright)

## Artifacts Generated

- This discovery document (ongoing)
- Extraction tool: `scripts/extract_skeleton_to_markdown.py` (smart truncation, context-aware)
- Extraction markdown for Aetherwright: `docs/extraction-output/order-of-the-aetherwright-extraction.md`
  - **Size:** 363KB (10,131 lines) ✓ Fits in context
  - **Format:** 344 moments sequentially, each with:
    - Skeleton snippet
    - Source line number
    - Relevant passage (truncated to context + surrounding text)
- Case study prose for Aetherwright (synthesized from extraction, next step)
- Generalized extraction system (tool + documentation)
- Integration into Savepoint Protocol

## Learning: First Implementation & Refinement

**Problem:** Initial extraction produced 29MB markdown (765,520 lines)
- Reason: Extracted ENTIRE timeline entry content (full conversation passages)
- Result: Didn't fit in context for prose synthesis

**Diagnosis:**
- 344 skeleton moments × average ~85KB per extracted passage = bloat
- The skeleton doesn't need entire conversations, just the relevant moment

**Solution:** Smart passage truncation
- When passage > 2000 chars, extract only:
  - 500 chars before snippet
  - The snippet itself
  - 500 chars after snippet
- Falls back to first 1000 chars if snippet not found
- Adds ellipses to show truncation

**Result:** 363KB extraction (down from 29MB)
- Maintains grounding: each moment still has line number + source
- Fits in context: 10,131 lines vs. 765,520
- Preserves signal: includes snippet + relevant context

**Key Insight:** Extraction isn't about copying raw chats. It's about indexing them. The skeleton moment's snippet is the query; the passage is the result that proves the query matched something real.

---

## Implementation Notes

**Extraction Tool Requirements:**
1. Load skeleton JSON from `docs/case-study-skeletons/`
2. Load raw chat exports (need to clarify structure/location)
3. For each skeleton moment: search raw chats by timestamp/snippet
4. Extract passage with line numbers (start:end format)
5. Organize by skeleton sequence
6. Output markdown file with clear structure

**Markdown Output Format:**
```markdown
# [Project Name] - Prose Extraction Source

**Manifest:** [What is this project?]

## Extracted Moments

### Moment 1: [Type] - [Timestamp]
**Skeleton snippet:** "..."
**Source:** [filename] lines X-Y
**Passage:**
[Full chat excerpt]

### Moment 2: [Type] - [Timestamp]
...
```

---

## Lessons for Colophon & Savepoint Case Studies

This discovery process itself demonstrates:
- The importance of iterating through failures to understand the actual problem
- How to separate mechanical work (extraction) from craft work (synthesis)
- Why validation and verification are essential, not optional
- How indexing (skeleton) relates to traversal and source material (raw chats)

This process **becomes the case study** for both Savepoint Protocol and Colophon.
