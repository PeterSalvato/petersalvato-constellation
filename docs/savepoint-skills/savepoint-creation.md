# Skill Spec: Savepoint Creation

**Status:** Initial capture
**Version:** 0.1
**Date:** 2026-02-07

---

## Purpose

Drop properly formatted Savepoint Protocol v3.0 savepoints during work—capturing decisions, reasoning, and semantic state in a structured, searchable, timestamped format.

---

## The Problem It Solves

Marathon work sessions produce insights that evaporate. Decisions get made but the reasoning isn't captured. Context leaks as you switch between tasks or sessions.

Without structured capture:
- You remember *what* you decided but not *why*
- Reconstruction requires re-reading entire histories
- Semantic lineage tracing has nothing to trace

---

## Core Capability

On invocation (e.g., `/savepoint`):

1. **Capture current context** — What project? What domain? What's the state?
2. **Identify the semantic core** — What's the decision/insight/crystallization?
3. **Format to v3.0 spec** — Proper syntax, timestamp, metadata
4. **Output or save** — Screen, clipboard, file, or all three

---

## v3.0 Syntax

```
savepoint
  protocol_version:3.0
  category:[domain_context]
  function:[role or purpose]
  importance:[optional: low/medium/high/critical]
  confidence:[optional: low/medium/high]
  timestamp:[ISO 8601 format]
  # [semantic content - single line, atomic, searchable]
/
```

### Content Block Rules

- Begins with `#` on its own line
- Single-line only
- Semantically atomic — stands alone as searchable anchor
- Required unless function is `anchor` or `stub`
- The actual decision/insight, not a summary of the conversation

---

## Example

```
savepoint
  protocol_version:3.0
  category:skill_development
  function:specification
  importance:high
  confidence:medium
  timestamp:2026-02-07T19:45:00Z
  # Semantic lineage tracing is the general capability; case study synthesis is one application.
/
```

---

## Potential Modes

*(To be refined)*

- **Quick** — Minimal prompting, infer what you can
- **Full** — Prompt for all metadata
- **Auto** — Detect from conversation context, confirm before saving

---

## Implementation Questions

*(To be answered through use)*

- Where do savepoints save by default? `.savepoints/`? Project-specific?
- Naming convention? `YYYY-MM-DD-HH-MM-[slug].md`?
- Should multiple savepoints in one session be in one file or separate?
- How to handle multi-project sessions?
- Integration with semantic lineage tracing (output should be input)?

---

## Relationship to Other Tools

- **Savepoint creation** is the capture mechanism
- **Conversation export** provides bulk historical material
- **Semantic lineage tracing** processes savepoints + exports
- **CLI tools** (`sp extract`, etc.) provide batch operations

---

## Origin

Savepoint Protocol v3.0 syntax was formalized April 2025. This skill makes creation frictionless—invoking it during work rather than reconstructing afterward.

The protocol exists. The skill makes it usable in flow.

---

*Initial capture. To be refined through application.*
