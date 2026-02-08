# Case Study: AI DevOps Workbench

## The Constraint

How do you use AI for serious engineering work when every session starts from zero and outputs are unreproducible?

---

## The Problem (July 2025)

The team at Cluen was evaluating AI for their enterprise development workflow. The boss wanted GitHub Copilot. The thinking: it's from Microsoft, it autocompletes code, problem solved.

But autocomplete isn't engineering. It's a faster linter. The real problem was different:

> "Throw a prompt at ChatGPT and you get output. Do it again and you can't reproduce it. Bring in multiple agents and nobody knows what happened or why. Drift accumulates. Provenance vanishes."

For a legacy .NET codebase with Kendo UI, SCSS architecture, and complex JavaScript—worked on by a team of 3.5 engineers—the question was different. How do you:
- Share domain expertise across team members without each person becoming a full-stack expert?
- Maintain consistent architectural decisions when AI suggestions vary by session?
- Track what the AI contributed versus what humans decided?

---

## The Approach: Documentation-Driven AI

The solution wasn't a new AI tool. It was a methodology for using AI tools systematically.

**Rule directories:** Each team member writes the rules for their area of expertise. Not prose—structured documents that define naming conventions, architectural patterns, allowed dependencies, forbidden patterns. An index file that maps the system. Atomic notes that can be selectively loaded.

**JSON prompting as configuration:** Prompts aren't improvised. They're structured, versioned, and treated like code. System prompts define agent roles and constraints. The same prompt produces the same behavior.

**Explicit provenance:** Every AI-assisted change is traceable. What agent was used? What prompt? What human decisions were made on top of the output?

---

## The Architecture: Workbench + Agency

The system split into two components:

**AI DevOps Workbench:** The orchestration layer. Defines how Claude Code operates in a project. Uses `CLAUDE.md` as a project constitution. Maintains `conventions.md` for patterns and `symbol-index.md` for terminology. Creates institutional memory that persists across sessions.

**Portable Agency:** 30 specialists across 13 departments—Design, Frontend, Backend, Database, Testing, DevOps, Security, Product, AI/Data, Mobile, Management. Each specialist is a structured prompt with defined expertise, invoked via slash commands.

The division matters:
- Workbench handles the *how*: orchestration, methodology, memory
- Agency handles the *what*: domain expertise, quality standards, audits

Integration: `npm run integrate` links all specialists into `.claude/agents/`, maintaining separation while providing seamless access.

---

## The Methodology

**Multi-expert collaboration:** The `react-performance-audit` specialist can be balanced against `accessibility-expert`. Conflicts are resolved through `/manage-conflict-resolution`, not left implicit.

**Cross-department reviews:** `/manage-cross-department-review` coordinates specialists across domains. A feature doesn't ship with only backend sign-off.

**Self-improving methodology:** `/methodology-auto-update on` and `/methodology-track-changes` create a learning system. Patterns discovered during work become part of the permanent methodology.

**Production focus:** Unlike tools that generate "demo code," the system emphasizes production quality. Security audits, performance optimization, accessibility compliance, comprehensive testing—built into the workflow, not added after.

---

## What It Proves

The AI DevOps Workbench demonstrates that:

1. **AI can be systematized.** "Vibecoding"—prompting until something works—is replaced by reproducible, auditable workflows.

2. **Documentation is the interface.** The methodology files (`conventions.md`, `symbol-index.md`) become the contract between humans and AI. Update the docs, update the behavior.

3. **Multi-agent coordination is possible.** With explicit handoffs, conflict resolution, and cross-department review, 30 specialists can work together without contradicting each other.

4. **Institutional memory survives sessions.** The project learns. Patterns discovered on day 50 are still available on day 500.

---

## Current State

Two repositories, open source:
- `AI-Devops-Workbench`: The orchestration framework
- `PortableAgency`: 30 specialists across 13 departments

Used in production at Cluen for enterprise development. The same methodology that governs Encore's architecture now governs how AI assists in building it.

---

*Generated: 2026-02-07*
*Method: Sequential reading of 42 conversations over 10 months*
