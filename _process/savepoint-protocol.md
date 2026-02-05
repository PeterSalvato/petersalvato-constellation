---
layout: process-archive
title: "Savepoint Protocol - Process Archive"
project: "savepoint-protocol"
permalink: /process-archives/savepoint-protocol/
---

## How This Was Built

Savepoint Protocol exists because executive dysfunction is a coherence problem, not a memory problem. The problem wasn't remembering tasks—it was maintaining a stable framework while context shifts, interruptions, and fatigue states pile up.

We built a protocol that captures transformation rather than just documentation. A savepoint isn't a snapshot of where you are. It's a structured record of *how your thinking changed*, so you can recover coherence even when context switches reset your working memory.

### Key Decisions Made

**Transformation capture, not documentation**
- Why chosen: Documentation systems assume memory is the bottleneck. Real constraint: maintaining coherent thought across context switches. If you capture *why* a decision changed, you can recover the thinking even when the context is gone.
- What considered: Task managers, note systems, structured journaling
- What it solved: Allowed recovery without having to reconstruct reasoning from scratch

**CLI interface, not graphical application**
- Why chosen: The protocol needs to integrate into existing workflow, not be a separate tool you switch to. CLI fits into shell history, pipes, scripts, and the thinking environment builders already use.
- What considered: Electron app, web interface, mobile app
- What it solved: Eliminated tool-switching friction. Reduced cognitive overhead of *using* the protocol.

**Semantic versioning for commits, not timestamps**
- Why chosen: A version number (1.2.3) is mnemonic and memorable. A timestamp (2024-10-15-14-32) is not. Neurodivergent cognition works better with numbers as anchors than with dates.
- What considered: Hash-based identification, sequential IDs, timestamp-based
- What it enabled: Memory hooks. You can say "back up to 3.1" and know where you are.

**JSON metadata layer for queryability**
- Why chosen: Machine-readable structure lets you ask questions: "show me all savepoints where I changed my mind about X." Free-form text can't answer that.
- What considered: Markdown-only, custom format, YAML
- What it solved: Enabled analysis of thinking patterns. Made the protocol actionable, not just archival.

**Single responsibility per savepoint**
- Why chosen: Forces clarity. If a savepoint tries to capture "everything I did today," it becomes a dump that's useless for recovery. One decision per savepoint keeps it focused.
- What considered: Bulk capture of all context at once
- What it solved: Maintainability. You know exactly what each savepoint is for.

**Off-platform storage in local files**
- Why chosen: You own the data. No dependency on providers. No sync failures. No closed platforms. Speed matters for a protocol you use daily.
- What considered: Cloud sync, proprietary tools, platform-dependent storage
- What it solved: Reliability and control. The system works even when internet is down.

### What Didn't Work (and Why We Fixed It)

**Early iteration: Screenshots alongside metadata**

We thought visual context (screenshots of the screen state when the savepoint was made) would help recovery. Turns out this created massive files, bloated git repos, and made searching impossible. The screenshot became noise.

How we fixed it: Store only the transformation narrative—what changed, why it changed, what decision was made. If you need screenshots for recovery, that means your transformation capture wasn't clear enough. This forced better documentation of the *thinking*, not the state.

The insight that stuck: A system that forces clarity of thought is more useful than a system that preserves every detail.

**Early iteration: Automatic context capture**

We built tooling to automatically detect "what context are you in right now" and bake that into savepoints. The system would scan files, track window focus, log timestamps.

What happened: It failed constantly. It captured wrong context. It became a source of friction instead of help. Neurodivergent users need *reliable* systems, not sophisticated ones that occasionally break.

How we fixed it: Made context capture manual but *easy*—a single flag in the command. You're responsible for naming your context. This means the protocol teaches you to *notice* your own context, rather than hiding it.

The insight that stuck: For neurodivergent workflow, reliability beats cleverness every time.

**Early iteration: Complex querying interface**

We built a sophisticated query language so you could ask the protocol sophisticated questions. "Show me all savepoints in project X with tag Y where decision Z changed."

What happened: Users looked at the interface and felt paralyzed. Too many options. The protocol became another system to learn instead of a tool that helped you think.

How we fixed it: Simple search by text, date range, and context. Query by looking at the files directly if you need something complex. Optimize for the common case (recovering a recent change), not for power users doing analysis.

The insight that stuck: Simplicity is a feature, not a limitation.

### Technical Architecture Notes

**Git-based storage with JSON metadata**

The protocol stores savepoints as git commits with structured metadata in JSON. Each commit is a savepoint. This gives you: free version control, auditable history, file sync compatibility (can push to GitHub), and the ability to use standard git tools if needed.

Trade-off: JSON is more rigid than free-form text, but it forces consistency. You're adding structure to thinking.

**Shell commands wrapping git operations**

The CLI is a thin wrapper around git. Commands like `sp save "context" "what changed"` translate to git commits with specific metadata structure. This means: no custom database, no server, just git doing what it does.

Scaling consideration: Works for individual use. Multi-user savepoints would require coordination (potential conflicts). Current design is single-user by constraint—which is fine. Neurodivergent work is often solo concentration time.

**Fallback mechanisms for context loss**

If you can't remember what context a savepoint was in, you can still find it. Tag-based search, text search, date range. Multiple paths to the same savepoint. Radial indexing—the same transformation appears in multiple contexts.

This means you don't have to remember the category you filed something under. The protocol was designed for people whose memory is unreliable—multiple paths beat single paths.

**Integration points with existing CLI tools**

The protocol outputs structured JSON, so standard tools can query it. `sp list | jq` works. `sp export | grep` works. It's composable with the Unix philosophy—do one thing well, output something standard other tools can consume.

### The Constraints That Shaped Everything

**Neurodivergent attention as the design constraint**

Executive dysfunction isn't about effort or intelligence. It's about working memory load and context-switching cost. Every time you switch contexts (from coding to email to a meeting to more coding), your brain has to rebuild the coherence of what you're doing.

A neurotypical person holds context implicitly: "I'm in 'work mode,' this task belongs to Project X, it relates to that conversation last week." A neurodivergent person needs all of that *explicit* or it falls apart.

The protocol exists to externalize that scaffolding. It makes implicit context explicit. This freed up cognitive resources previously spent on meta-work (remembering what mode you're in, what project this belongs to, why you made this choice last time).

**Reliability as non-negotiable**

For a protocol serving neurodivergent workflow, a system that's clever but occasionally breaks is worse than a system that's simple and reliable.

Every feature we added got tested against: "Does this add friction when the system has to be recovered from failure?" Unreliable features got cut. This meant no automatic anything, no cloud sync, no hidden magic. Simple enough to debug when it breaks.

**The protocol is useless if you don't trust it**

If you can't count on the protocol being there when you need it, you won't use it. This drove us toward offline-first, local storage, no external dependencies.

It also drove us toward simplicity. Complex systems break more often. Simple systems become muscle memory.

**Documentation is required for transfer**

The protocol only works if other people can use it—or if future-you can recover understanding. This meant: heavy documentation of how and why decisions were made. Not documentation as afterthought, but documentation as core requirement.

This constraint changed everything. It meant the protocol itself had to *teach* through its structure. If someone reads the git history and doesn't understand why something was saved, the documentation failed.

### What We'd Do Differently

If we restarted, the core structure would hold: transformation capture, radial indexing, local storage, CLI interface, JSON metadata.

What we'd adjust: Even more emphasis on *why* decisions were made, less on decorative metadata. We included some fields that nobody uses. The protocol was overdesigned in places—trying to be sophisticated when simple would have served better.

We'd invest more time early in the documentation and examples. The protocol is powerful, but it's not obvious how to use it until you've lived with it for a month.

Most importantly: We'd test with actual neurodivergent users much earlier. The constraint that shaped this protocol is specific—executive dysfunction, context-switching cost, working memory load. If you're building for that constraint, you need people living it to validate.

The principle that held: **Reliability and simplicity beat sophistication.** Every time we chose simple over clever, the system became more useful.

What this taught us about other work: Any system serving neurodivergent users (or frankly, any stressed humans) needs to optimize for coherence recovery, not just task completion. The thinking support matters more than the output.

---

*Process Archive for Savepoint Protocol. See case study at `/protocols/savepoint-protocol` for project overview.*
