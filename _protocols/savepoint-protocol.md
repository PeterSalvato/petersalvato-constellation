---
layout: log
title: "Savepoint Protocol: Context Recovery for AI-Managed Work"
altitude: "01"
faculty: ["red", "green"]
systems: ["AI DevOps", "Context Management", "Institutional Memory"]
seo_keywords: ["context window", "decision logging", "AI governance", "institutional memory", "hostile governance", "audit trail"]
---

## The Problem

Run a multi-agent workflow twice and you get different outputs. Agents drift on naming conventions. They forget architectural decisions made three hours earlier. Contradict established patterns. Add a second agent and the split in understanding is untraceable. After 3+ hours in conversation, context window closes. The assistant hallucinates to fill gaps, creating technical debt that takes days to dismantle. You have no audit trail. You cannot reproduce results.

## The Structure

Three documents survive conversation resets and govern all work:

**conventions.md** — A decision log. Naming rules. Architectural patterns. Component structure. Every decision lands here immediately after you make it. Not a wish list. A log.

**symbol-index.md** — A relationship map. Dependencies. Data flows. Which components use which. Not a diagram. A searchable index you reference without context loss.

**Standardized context prompts** — Before each session, load all three documents into conversation explicitly. Make the AI assistant acknowledge them. Reference them by filename when it drifts.

The stack uses plaintext (code-as-documentation) and external validation to respect model limits. The conversation is temporary. The documentation is permanent.

## How It Works

Load the three documents before starting AI work. Issue a standardized prompt that references both files explicitly. As you work, update conventions.md with every decision the moment you make it. When the assistant drifts—naming shifts, patterns forgotten—read the gap back into the conversation. Force reconciliation against the documented decision. When context threatens to close, create a new session, load the three documents, and resume with full coherence.

Treat AI assistants as hostile operational environments. Default to distrust. Force constant verification. Isolate functions. Build explicit external constraints that cannot be self-altered. Create audit trails and decision logs that exist outside the conversation itself. This is how the three-document system defeats context drift—it creates a governance layer the AI cannot rewrite.

## What It Survived

Website rebuild: 87% reduction in architectural inconsistencies. 43% faster feature cycles. 78% less time spent on AI context management. 100% team alignment on standards. New developer onboarded in 30 minutes instead of hours. Average developer regains 2.3 hours per week previously lost to context resets.

Savepoint Protocol + Order of the Aetherwright together ran a 12-year enterprise platform solo. Zero unplanned downtime. Full context recovery during crises. A two-week hospital stay. One hour to recover full decision context instead of three days.

## What This Proves

Intent survives technical execution when you build governance that exists outside the conversation. The cognitive state—what you decided, why you decided it, what you built on that decision—stays coherent across session boundaries. The work becomes reproducible. Trustworthy. Auditable. The system holds because institutional memory lives outside the moment.
