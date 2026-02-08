# Savepoint Protocol Skills

**Status:** Initial specification
**Date:** 2026-02-07

---

## Overview

These skills extend Savepoint Protocol from a storage format into an active cognitive toolkit. They're the operational layer—how you capture and process meaning, not just where you store it.

---

## The Skills

### 1. Savepoint Creation
**File:** `savepoint-creation.md`

Drop properly formatted v3.0 savepoints during work. Captures decisions and reasoning in structured format.

**When:** During work, when something crystallizes
**Output:** Formatted savepoint (screen/file/clipboard)

---

### 2. Semantic Lineage Tracing
**File:** `semantic-lineage-tracing.md`

Traverse large chronological documents and trace how meaning evolved over time.

**When:** After work, when you need to understand the arc
**Output:** Traced lineage (timeline, pivots, quotes, summary)

---

## How They Relate

```
During Work                    After Work
    │                              │
    ▼                              ▼
┌─────────────────┐    ┌─────────────────────────┐
│   /savepoint    │───▶│  Semantic Lineage       │
│   (capture)     │    │  Tracing (process)      │
└─────────────────┘    └─────────────────────────┘
    │                              │
    ▼                              ▼
┌─────────────────┐    ┌─────────────────────────┐
│  .savepoints/   │    │  Case Studies           │
│  (storage)      │    │  Decision Archaeology   │
└─────────────────┘    │  Architecture Tracing   │
                       │  (applications)         │
                       └─────────────────────────┘
```

---

## Applications

The skills are general; applications are specific:

| Application | Uses | Output |
|-------------|------|--------|
| Case Study Synthesis | Lineage Tracing | Narrative case study |
| Decision Archaeology | Lineage Tracing | Why was X decided? |
| Architecture Tracing | Lineage Tracing | How did system evolve? |
| Bug Hunting | Lineage Tracing | Where did this break? |
| Session Capture | Savepoint Creation | Structured checkpoint |
| Knowledge Preservation | Savepoint Creation | Searchable decisions |

---

## Integration with Savepoint Protocol

These skills are candidates for inclusion in the Savepoint Protocol CLI:

- `sp save` → Savepoint creation
- `sp trace` → Semantic lineage tracing
- `sp synthesize <type>` → Application-specific synthesis

Current CLI commands (`sp extract`, etc.) handle bulk export processing. These skills add:
- In-flow capture (during work)
- Post-hoc analysis (after work)

---

## Development Status

Both skills are at v0.1 — concepts captured, implementation pending.

Refinement will happen through use:
1. Try the skill manually
2. Note what's missing or awkward
3. Update the spec
4. Eventually codify into CLI/automation

---

## Origin

Emerged from case study generation work (2026-02-07). The process that worked—chronological reading with semantic tracking—revealed a general capability worth extracting.

---

*To be refined through application.*
