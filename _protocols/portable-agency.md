---
layout: log
title: "Portable Agency"
type: "INFRASTRUCTURE PROTOCOL"
status: "Live"
---

## What It Is

A homelab-based infrastructure stack for digital autonomy. Everything runs locally. No cloud dependencies for critical operations.

The premise: if your family's data, media, backups, and compute depend entirely on services you don't control, you've built on someone else's foundation. When they change their pricing, deprecate their API, or go offline, your infrastructure goes with them.

## The Problem

Cloud-only stacks create three kinds of risk:
- **Geographical risk.** Cross-border relocation means your data crosses jurisdictions you didn't choose.
- **Vendor risk.** Service changes, price hikes, and deprecations happen on someone else's schedule.
- **Availability risk.** When the internet goes down — and it does — cloud-dependent infrastructure goes dark.

For a family navigating relocation, chronic health constraints, and neurodivergent workflow, these aren't theoretical risks. They're operational constraints.

## The Stack

### Local Compute
Ubuntu server. Docker containers for service isolation. GPU-enabled for local AI inference. The compute lives in the house, not in someone else's datacenter.

### Data Sovereignty
Self-hosted storage. Automated backups with local and off-site redundancy. Media server (Plex/Jellyfin) for the family's content library. No subscription required to access your own files.

### Network-Agnostic Design
Core services function on the local network. Internet connectivity extends capability but isn't required for baseline operation. The family can access their systems regardless of ISP status.

### AI Infrastructure
Local LLM inference for sensitive or high-frequency tasks. No data leaves the network for routine AI operations. Cloud APIs available as a supplement, not a dependency.

## What It Proves

Digital autonomy isn't a philosophy — it's an infrastructure decision. When the systems your family depends on run in your house, on your hardware, under your control, the risk profile changes fundamentally.

Portable Agency is the same principle as every other system I build: if the structure doesn't survive the removal of a dependency, it's not durable. The homelab is the proof that sovereignty is an engineering problem, not a lifestyle brand.
