# Case Study: Portable Agency

## The Constraint

How do you maintain digital autonomy when everything runs in someone else's cloud?

---

## The Problem

Modern infrastructure is rented. ISP outage. Corporate policy shift. Algorithm change. Service discontinuation. The infrastructure you depend on can disappear with no notice and no recourse.

For a family with specific needs—neurodivergent members, complex medical requirements, creative work that requires control—this dependency creates unacceptable fragility.

---

## The Solution: Local-First Infrastructure

Portable Agency operates on a simple principle: if you don't control the hardware, you don't control the system.

**Homelab compute:** Ubuntu server running local services. Not a hobby project—production infrastructure for family operations.

**Offline data sovereignty:** Storage you own. Backup mirrors you control. No dependency on cloud sync that can be discontinued or repriced.

**AI compute:** Local LLM deployment through Ollama. RAG systems for personal knowledge bases. The AI assistance works when the internet doesn't.

**Media infrastructure:** Jellyfin for media. Local downloads via protected torrenting. No streaming service can decide what's available.

---

## The Architecture

The system spans hardware and software:

**Storage:**
- Primary: 7.3TB GoogleDrive mount (local sync)
- Backup: 4.6TB RAID1 mirror
- Secondary: 4.6TB additional mirror
- 3-2-1 backup strategy executed locally

**Services:**
- Jellyfin for media serving
- Ollama for local AI
- qBittorrent with VPN enforcement
- Custom containers for specific workflows

**Network:**
- Tailscale mesh for secure remote access
- UFW firewall
- fail2ban for brute-force protection

---

## Connection to AI DevOps Workbench

Portable Agency serves as the infrastructure layer for AI DevOps Workbench. The 30 specialists defined in Workbench can run locally. The methodology files persist on owned storage. The AI compute happens on controlled hardware.

When the Workbench says "create a security audit," the Agency provides the local infrastructure to execute it without sending code to external services.

---

## What It Proves

Portable Agency demonstrates that:

1. **Digital autonomy is achievable.** A non-expert can build and maintain local infrastructure that rivals cloud services in capability.

2. **The investment pays off in resilience.** Internet outages don't stop family operations. Service discontinuations don't orphan data.

3. **Control enables customization.** Systems built for specific needs—neurodivergent workflows, medical data privacy, creative control—rather than lowest-common-denominator features.

4. **The skills transfer.** Building homelab infrastructure teaches the same patterns used in enterprise operations.

---

## Current State

Live. The family operates on it daily. Storage, media, AI, network—all running on owned hardware.

The same discipline that produces enterprise systems (Encore) and cognitive tools (Savepoint) applies to domestic infrastructure.

---

*Generated: 2026-02-07*
*Method: Sequential reading of 80 conversations over 15 months*
