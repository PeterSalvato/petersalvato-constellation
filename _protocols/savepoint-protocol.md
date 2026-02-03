---
layout: log
title: "Savepoint Protocol: Context Recovery for AI-Managed Work"
altitude: "01"
faculty: ["red", "green"]
systems: ["AI DevOps", "Context Management", "Institutional Memory"]
seo_keywords: ["context window", "decision logging", "AI governance", "institutional memory", "hostile governance", "audit trail"]
---

## The Problem

Run a multi-agent workflow twice and you get different outputs. Agents rename things. They forget decisions made three hours earlier. They contradict patterns. Add a second agent and the split is invisible. After 3+ hours, the context window closes. The assistant fills gaps with guesses, creating technical debt that takes days to fix. You have no record. You cannot run it again the same way.

## The Structure

Three documents survive conversation resets:

**conventions.md** — A decision log. What names stick. What patterns we follow. How components fit together. Every decision lands here the moment you make it. Not aspirational. Actual.

**symbol-index.md** — A map of what connects to what. Dependencies. Data flows. Which components call which. No diagrams. A text file you search without losing context.

**Standardized context prompts** — Before each session, paste all three documents into the conversation. Make the assistant read them aloud. Reference them by filename when it drifts.

The system runs on plaintext and external checks. It respects what the model actually does. The conversation is temporary. The documentation is permanent.

## How It Works

Paste the three documents before you start. Write a prompt that names both files explicitly. During work, update conventions.md every time you decide something. The moment it happens. When the assistant renames something or forgets a pattern, read the gap back. Force it to reconcile against what you documented. When the context window fills, start a new session, paste the three documents again, and continue with full coherence.

Treat AI assistants as hostile operational environments. Default to distrust. Verify constantly. Isolate functions. Build hard external constraints the AI cannot rewrite. Keep audit trails and decision logs outside the conversation. This is how the three-document system stops drift—it makes governance the AI cannot alter.

## What It Survived

Website rebuild: 87% fewer architectural inconsistencies. 43% faster feature cycles. 78% less time managing AI context. 100% team alignment on standards. New developer onboarded in 30 minutes instead of hours. Average developer recovered 2.3 hours per week lost to context resets.

Savepoint Protocol + Order of the Aetherwright ran a 12-year enterprise platform alone. Zero unplanned downtime. Full context recovery during crises. One hour to recover decision context instead of three days, even after a two-week hospital stay.

## What This Proves

Intent survives when you build governance outside the conversation. The decisions—what you chose, why, what you built on it—stays coherent across session boundaries. The work becomes reproducible. Trustworthy. Auditable. The system holds because the decisions live outside the moment.
