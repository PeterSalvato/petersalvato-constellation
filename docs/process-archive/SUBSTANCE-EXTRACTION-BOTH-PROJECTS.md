# Substance Extraction: Two Core Projects

Extracted from conversation archives using methodology from `/root/.claude/skills/substance-extraction/`

---

## Project 1: AI DevOps Workbench

### The Problem

Run a multi-agent workflow twice and you get different outputs—agents drift on naming, forget architectural decisions, and contradict earlier patterns. Add a second agent and you cannot trace what happened, why it happened, or where the split in understanding occurred. After 3+ hours in a conversation, context window closes and agents start hallucinating to fill gaps, creating technical debt you spend days cleaning up. You have no audit trail and cannot reproduce results.

### The Solution

Three-component system: **conventions.md** (decision log encoding naming rules, architectural patterns, component structure), **symbol-index.md** (relationship map showing dependencies, data flows, which components use which), and **standardized context prompts** that reference both documents before each session. Stack uses plaintext (code-as-documentation) and external validation to respect model limits. Every architectural decision gets documented in conventions.md immediately—making it a persistent context layer that persists across conversation resets.

### The Mechanics

Before starting AI work: read the three documents into context. Issue a standardized prompt that references both files explicitly. As you work, update conventions.md with every decision the moment you make it. If the AI assistant drifts (naming shifts, patterns forgotten), read the gap back into the conversation—forcing reconciliation against the documented decision. When conversation context threatens to close, create a new session, load the three documents, and resume with full coherence.

### The Proof

Website rebuild: 87% reduction in architectural inconsistencies, 43% faster feature cycles, 78% less time spent on AI context management, 100% team alignment on standards. New developer onboarded in 30 minutes instead of hours. Average developer regains 2.3 hours per week previously lost to context resets. Savepoint Protocol + Order of the Aetherwright together: ran a 12-year enterprise platform solo, zero unplanned downtime, full context recovery during crises.

---

## Project 2: Order of the Aetherwright

### The Problem

When a creative system relies on semi-mystical language (Frames, Reels, Glyphs) without sufficient internal rigor, terms risk semantic drift—users interpret the same glyph differently over time, fracturing coherence. A new person cannot easily join because it demands intense front-loading of philosophy and symbol-set digestion. Without continuous external policing of meaning, meanings blur. Without a governed process for amending the taxonomy, the system either ossifies (becomes brittle) or fragments (users invent divergent private versions).

### The Solution

Eight-glyph naming system where every folder name encodes its structural purpose—red glyphs mark logic, green mark expression, blue mark utility. Codex functions as central repository (akin to alchemical grimoire) encoding the glyph system, tenets, rituals, and ledger of recognized practitioners. Threefold Path structures all creative work as three sequential phases—Deconstruction, Iteration, Synthesis. Ritual of Attention uses the glyphs to visibly track effort across phases and identify primary versus peripheral focus. The Æ Sigil marks earned achievement, not claimed identity.

### The Mechanics

Before starting a project, answer: "What is the ONE question this solves?" Write it in scope.md. Everything in the project serves that question or gets deleted. Use glyphs to label folders, creating unambiguous structure. During work, track intensity across Threefold Path phases using Ritual of Attention (glyph notation), making effort allocation visible. The Steward guards the Codex and recognizes practitioners who embody the system—role emerges from consistent practice, not invitation. Savepoint Protocol + Order together: Savepoint manages the "why" and "when" (timestamped reflection), Codex tracks the "what" and "how" (structural encoding).

### The Proof

12-year solo platform (Encore): zero context loss during crises, recovered full decision context in 1 hour during 2-week hospital stay instead of 3 days. Portfolio projects gain hidden symbolic architecture—viewers sense structure without explicit explanation. Framework explicitly distances itself from persona or branding (preventing semantic capture by audience interpretation). The dyadic system (Savepoint + Order) creates interlock: you cannot advance without both. Used on real projects with measurable coherence across portfolio constellation—petersalvato.com, aetherwright.com, project documentation naming conventions, glyph metadata all aligned without external governance.

---

## Cross-Project Coherence

**Savepoint Protocol** (version control for cognitive state) and **Order of the Aetherwright** (taxonomic structure for creative work) form a **dyadic system** where neither is complete without the other:

- Savepoint answers: When do I pause? What have I learned? How do I resume with full context?
- Order answers: How do I structure the work itself? What naming rules protect meaning? How do I prove skill through system design?

Together: institutional memory + symbolic governance = intent survives technical execution.

**Critical Hostile Governance Principle**: Treat AI assistants as hostile operational environments. Default to distrust. Force constant verification. Isolate functions. Build explicit external constraints that cannot be self-altered. Create audit trails and decision logs that exist outside the conversation itself. This is how the three-document system (conventions.md + symbol-index.md + prompts) defeats context drift—it creates a governance layer the AI cannot rewrite.

---

## Sources & Conversation References

All extraction sourced from:
- `/home/peter/homelab/knowledge/archive/conversations/AE-CSA-Projects/csa-project-status-and-gaps.md` (Lines 1-644+)
- `/home/peter/homelab/knowledge/archive/conversations/AE-CSA-Projects/ae039.order-of-ætherwright-summary.md` (Full document)
- `/home/peter/homelab/knowledge/archive/conversations/AE-CSA-Projects/ae091.savepoint.syntax.formalization.protocol.v3.foundation.strategy.trajectory.exposure.closed-2025.md` (Lines 1-350+)
- `/home/peter/homelab/knowledge/exports/markdown_exports/claude_ai/0203_AI context loss solution.md` (Lines 19-150+)

Ready for voice agent shaping per AGENT-PROMPT.md format.
