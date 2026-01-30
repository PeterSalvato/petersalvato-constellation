---
layout: whitepaper
title: "Encore"
client: "Cluen Corporation"
tags: [Legacy Modernization, Platform Architecture, 12-Year Tenure]
---

## The Work

For 12 years, I've been the Principal Architect for Cluen's flagship recruitment platform. The job wasn't to build something and move on. It was to keep it alive — through three distinct technological shifts, 40,000+ users, 2.5M+ annual transactions, and zero catastrophic failures.

Everyone wants a system that's both stable and modern. That's the actual constraint. You don't get to choose.

The Encore Platform is the operational backbone for thousands of global employers. Downtime is not acceptable. Legacy isn't a failure — it's proof that something matters enough to maintain.

## The Approach

Big rewrites break things. So we didn't do one.

Instead: wrap the legacy .NET core in a modern React shell. Replace the engine while the car's moving. The Strangler Fig pattern — not because it's fashionable, but because it respects two things: institutional knowledge and uptime.

**How it worked:**
1. Identify the friction points (auth, reporting, bulk operations)
2. Build modern interfaces around them
3. Route traffic incrementally to the new layer
4. Decommission legacy code only after the replacement is proven stable

No heroics. No faith-based architecture. Incremental replacement, verified at every step.

## The Numbers

| | |
|--------|--------|
| Uptime | 99.9% over 12 years |
| Major rewrites | 0 |
| Technology epochs survived | 3 |
| Annual users | 40,000+ |
| Annual transactions | 2.5M+ |

## What It Proves

Legacy code isn't a failure. It's evidence that something works. Systems that survive a decade survive because they solve a real problem, efficiently. The architect's job isn't to erase that — it's to evolve it.

That's harder than starting over. It's also more honest.
