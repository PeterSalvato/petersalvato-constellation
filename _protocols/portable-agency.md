---
layout: protocol-01
title: "Portable Agency: Local-First Infrastructure"
altitude: "01"
faculty: ["green"]
systems: ["technical"]
status: "Live"
seo_keywords: ["Homelab Architecture", "Local-first Systems", "Data Sovereignty", "Offline Computing", "Infrastructure Autonomy"]
---

## Where It Started

Personal infrastructure operated under complete digital dependency. Files in cloud storage. Compute leased from corporations. Infrastructure existed only because ISPs, hosting providers, and SaaS companies maintained their terms of service. One policy shift. One corporate decision. One funding round going badly. Everything disappears.

The real constraint: **What happens to your infrastructure if the internet disappears? If your hosting provider goes down? If one company changes terms? If funding runs out?**

The operational reality: A family system running entirely on corporate-controlled infrastructure. No offline capability. No portability. No autonomy.

## The Problem

**Structural Fragmentation:** Complete digital dependency on cloud infrastructure controlled by corporations with no accountability.

The actual fragmentation:
- Files exist only if Google/Microsoft/Dropbox decide to keep them
- Compute exists only if AWS/Heroku/DigitalOcean decide to keep serving it
- Services stop working if an ISP goes down
- No offline capability means no continuity during outages
- No data portability means switching costs are catastrophic
- No autonomy means someone else makes the policy decisions

The diagnostic question: **Can you actually run your digital life without someone else's permission?**

## The Thinking

**Three approaches were tested:**

**Approach 1: Multiple Cloud Providers** – Redundancy through vendor diversity. Sign up for backup cloud accounts.
- Problem: Still dependent on multiple corporations. Still no offline capability. Still required internet connectivity. Addressed vendor risk but not structural dependency. Rejected because it's contingency, not structure.

**Approach 2: Hybrid Cloud/Local** – Best of both worlds. Keep some files locally, sync to cloud. Local infrastructure for backup.
- Problem: Sync failures created fragmentation. Still required cloud for most operations. Local infrastructure too limited to operate independently. Rejected because it created more complexity, not autonomy.

### The Breakthrough: Local-First as Primary Architecture

**Key Insight: You own the infrastructure. Not metaphorically. Physically.**

The reframing: *What if the primary architecture was local-first, with internet as an optional enhancement?*

Instead of local being contingency, make local the primary design:
- Your compute runs on machines in your home (Ollama for AI, PostgreSQL for data, Jellyfin for media)
- Your data lives on drives you control (not accessed through cloud sync—actually stored locally)
- The system works whether or not the internet is available
- Not as a feature. As the architecture.

Integration point: **Redundancy through ownership. When you own infrastructure, availability doesn't depend on someone else's quarterly earnings report.**

### Evolution: From Cloud Dependency to Local Autonomy

**Phase 1: Local Infrastructure Foundation (Weeks 1-3)**
- Set up home server with Docker Compose orchestration
- Installed Jellyfin (media server under your control)
- Installed Nextcloud (file storage under your control, with GoogleDrive bridge for backup)
- Installed Ollama (AI inference on local hardware, no cloud API calls)
- Installed PostgreSQL (structured data on your hardware)

**Phase 2: Data Sovereignty Implementation (Weeks 4-6)**
- Migrated family files from cloud storage to local drives
- Implemented 3-2-1 backup strategy (3 copies, 2 media types, 1 offsite—planned)
- Set up rsync for drive mirroring
- Created backup scheduling and verification
- Data became physically accessible, not API-gated

**Phase 3: Network Architecture (Weeks 7-9)**
- Local LAN access for home network (192.168.86.x)
- Tailscale VPN for remote access without port forwarding or ISP dependency
- System works on LAN, over VPN, completely offline
- Same functionality in all three states

**Phase 4: Family Operations (Week 10+)**
- Four family members with Jellyfin user accounts
- Nextcloud storage with per-user quotas
- Minecraft servers running on local hardware
- Cooking Mentor Agent (AI guidance with local FAISS vector database)
- Dashboard for system monitoring and control

**Phase 5: Operational Maturity (Ongoing)**
- Documented infrastructure state in CONVENTIONS.md
- Automated backup execution and verification
- Family-wide accessibility without corporate intermediary
- System survives ISP outages without losing local functionality

## The Architecture

**What Runs Locally:**
- Jellyfin (media server) — Family of 4 streaming movies from local storage
- Nextcloud (file storage) — Document collaboration without cloud accounts
- Ollama (AI inference) — Local LLMs running on home hardware
- PostgreSQL (structured data) — Databases on drives you control
- Minecraft servers (creative spaces) — Games running on local infrastructure
- Cooking Mentor Agent (domain-specific AI) — Guidance with local vector database
- Dashboard (monitoring) — System visibility and control

**When the Internet Fails:**
Your infrastructure keeps running. Files stay accessible. Work continues. Not as a contingency feature. As the baseline architecture.

**It Works Everywhere:**
- On your home network (LAN-only, zero internet dependency)
- Over a VPN from anywhere (secure remote access)
- Completely offline (local operation uninterrupted)
- Same system, same reliability in all three states

## Why This Works

The confidence comes from recognizing: **Ownership is the only true redundancy.**

This approach works because:
1. **Structural Integrity** – Based on physical ownership of hardware, not corporate terms of service
2. **Authentic Integration** – The system doesn't pretend to work offline; offline operation is the primary design
3. **Recursion Capacity** – System scales because each new service added increases autonomy, not dependency
4. **Graceful Degradation** – Works on LAN, over VPN, completely offline. Architecture handles all states.
5. **Truth Alignment** – Your data lives where you can see it. No hidden terms of service. No algorithmic decisions changing access.

## The Proof

**What Actually Works:**
1. **Zero cloud dependency** — Family files, media, AI, storage all local
2. **ISP outages don't break infrastructure** — LAN-only operation continues uninterrupted
3. **Corporate policy shifts don't affect access** — Data physically owned, not subject to terms of service
4. **Network flexibility** — Works on home LAN, over VPN from anywhere, completely offline
5. **Scalability without new rent** — Add services and storage without new subscriptions

**Measured Results:**
- 12-year platform (Encore) runs on Portable Agency infrastructure
- Zero unplanned outages (infrastructure reliability proven)
- Full context recovery during crises (hospital stay example: recovered 2-week decision context in 1 hour)
- Family of 4 operates on infrastructure requiring zero cloud accounts

**Operational Reality:**
A family actually runs on this setup. Not a weekend project—it's how they actually live. This is what happens when you stop accepting infrastructure someone else controls and start building your own. The system survives because you own the infrastructure, not because a company's terms of service permit you to.
