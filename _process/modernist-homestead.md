---
layout: process-archive
title: "Modernist Homestead - Process Archive"
project: "modernist-homestead"
permalink: /process-archives/modernist-homestead/
---

## How This Was Built

Modernist Homestead is infrastructure-as-care. A home server system designed for a neurodivergent household of four. The constraint wasn't technical—it was social and cognitive: build systems that reduce friction for people with varying attention spans, executive function challenges, and different levels of technical literacy.

---

## Key Decisions Made

**Decision 1: Household as operational unit, not nuclear family**

- Why chosen: "Family" is social concept. "Household" is operational. Five different people need five different things—media, gaming, work, learning, storage. Single system for one family doesn't work.
- What considered: One system per person (fragmented), shared system with permissions (complex), hierarchical (authoritarian)
- What it solved: Each person can operate independently while sharing infrastructure. No single person can break it for everyone.

**Decision 2: Physical infrastructure as visible communication**

- Why chosen: Hidden complexity is mysterious. When operators don't understand the system, they can't fix it. Make it visible so people can learn it.
- What considered: Abstracted interfaces (user-friendly, opaque), configuration files only (powerful, invisible), physical labels and documentation (teachable)
- What it solved: System literacy. People understand what's running, where data lives, how to recover when something breaks.

**Decision 3: Local-first infrastructure, not cloud-dependent**

- Why chosen: Cloud services fail. ISPs go down. We needed operational continuity independent of external providers. Also: data sovereignty. Your data lives in your house, not someone else's.
- What considered: All-cloud (convenient, dependent), hybrid (complex), local-only (limited remote access)
- What it solved: Resilience. The household doesn't depend on external services. When internet fails, the system keeps running.

**Decision 4: Automation by principle, not for convenience**

- Why chosen: Most automation fails. Automated systems need debugging. Better to automate decisions we've already made than to automate everything possible.
- What considered: Automate everything (brittle), automate nothing (labor-intensive), automate only stable decisions (sustainable)
- What it solved: Reliability. The system only automates what we've proven works. Less magic. More predictability.

**Decision 5: Documentation as operational requirement**

- Why chosen: Five operators at different skill levels. If the original operator leaves (or becomes unavailable), someone else has to maintain it. Without documentation, that's impossible.
- What considered: Oral knowledge (fast, fragile), code comments only (dense, incomplete), full documentation (maintainable, laborious)
- What it solved: Knowledge transfer. Someone can read the CONVENTIONS.md file and understand how the system works. The system survives personnel changes.

---

## What Didn't Work (and Why We Fixed It)

**Experiment 1: Centralized automation**

We built a master automation layer. One script controlled everything. "Start all services. Mount all drives. Run all backups."

Reality: Master script was single point of failure. One error broke everything. Debugging was nightmare. Multiple operators couldn't run pieces independently.

How resolved: Decentralized. Each service owns its own startup script. Each component is independent. You can restart media without restarting storage.

The learning: Centralized control is convenient until it fails. Then it's catastrophic. Better to accept some redundancy for resilience.

---

**Experiment 2: Cloud-first for convenience**

We tried Google Drive for everything. Convenient. Syncs automatically. Remote access built-in.

Reality: Bandwidth constraints appeared. ISP outages meant no data access. Google API changes broke integrations. We weren't in control. We were dependent.

How resolved: Moved core to local storage. Google Drive as secondary backup, not primary. Restored operational independence.

The learning: Convenience has a cost. That cost is paid in dependency. For a household system, independence matters more than convenience.

---

**Experiment 3: Hidden complexity**

We hid infrastructure. "Users don't need to know how this works. Just use the interface."

Reality: People got confused. When something broke, nobody knew how to fix it. System literacy evaporated. People stopped trusting it.

How resolved: Made everything visible. Labeled physical drives. Documented system architecture. People could see the shape of the system.

The learning: Transparency is security. When people understand the system, they can help maintain it.

---

## Technical Architecture Notes

**Docker containerization for modularity**

Each service runs in a container: Jellyfin, Nextcloud, game servers, knowledge systems. Containers isolate failures. You can restart one service without affecting others.

Why containers: Portable. Reproducible. Easy to test. Can be deployed on any Linux host.

---

**Local storage with distributed backup**

Primary storage on 7TB drive. Secondary backups on two 4.5TB drives using rsync. 3-2-1 backup strategy: 3 copies, 2 different media types, 1 tested recovery.

Why rsync: Simple. Fast. Verifiable. Works without central orchestration.

---

**CONVENTIONS.md as operational contract**

Living document. Every configuration decision is documented with rationale. Every change updates the document. Becomes the source of truth for "how does this system work?"

Why documentation-first: Operability depends on understanding. If it's not documented, future operators won't know why decisions were made.

---

## The Constraints That Shaped Everything

**Constraint 1: Neurodivergent household**

Executive function varies. Attention spans are unpredictable. Energy levels fluctuate. Complex systems require constant attention—that's not sustainable here.

How it shaped design: Systems must be simple enough that someone with low-function days can still operate them. Automation only where it's reliable. Clear documentation so you don't have to remember details.

---

**Constraint 2: Multiple operators at different skill levels**

Not everyone is technical. One person understands Docker. Another barely uses command line. System must be operable by people at different levels.

How it shaped design: Made everything visible and documented. Anyone can read CONVENTIONS.md and understand structure. Advanced operators can dig deeper. Novices aren't blocked.

---

**Constraint 3: Operational continuity**

If the original operator becomes unavailable (illness, unavoidable absence, changes mind), someone else has to maintain it. The system can't depend on a single person.

How it shaped design: Heavy investment in documentation. Clear procedures. Redundancy at critical points. If Peter is gone for three months, Randi needs to keep the system running.

---

## What We'd Do Differently

If starting over, we'd document from day one. Not after. We documented the system months after building it. That was inefficient. Documenting alongside building is better.

We'd also build the monitoring earlier. Not just alerts—visibility. A dashboard that shows system health, storage usage, backup status. Early visibility catches problems before they become failures.

What held: The constraint-driven approach. The decision to prioritize operator resilience over feature richness. The principle that documentation is infrastructure, not luxury.

How this informed other work: Modernist Homestead proved that systems for people with constraints are more resilient than systems designed for "typical users." That shaped everything: Savepoint (built for neurodivergent operators), Aetherwright (built for multi-team coherence), Aiden-Jae (built for craft constraints).

