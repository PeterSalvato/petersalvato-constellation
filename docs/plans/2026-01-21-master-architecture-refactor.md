# Master Architecture Refactor Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restructure the Jekyll site from a directory-based navigation model to a Collections-based architecture with the NASA-inspired "Aero-Space Brutalism" aesthetic, implementing the console-based homepage, printer exhaust marginalia, and updated navigation structure.

**Architecture:** Convert `evidence/`, `labs/`, and `system/` directories into Jekyll Collections (`_evidence/`, `_protocols/`, `_labs/`). Create a unified navigation system via `_data/navigation.yml`. Implement the "console" homepage layout with status board. Add NASA-inspired CSS with printer exhaust effects (crop marks, vertical slugs, registration targets). Update typography to Helvetica Now Display (fallback Inter) and Space Mono for data.

**Tech Stack:** Jekyll Collections, SCSS, Responsive Grid Layout, Google Fonts (Helvetica Now, Space Mono), NASA design principles.

---

## CURRENT STATE ANALYSIS

### File Structure
```
petersalvato.com/
├── evidence/
│   ├── enterprise-systems/ (index.md, the-encore-platform.md)
│   └── brand-commerce-systems/ (index.md, aiden-jae.md)
├── labs/
│   └── visual-research/ (index.md, echo-and-bone.md)
├── system/ (doctrine.md, contact.md)
├── _data/
│   ├── brand_systems.yml
│   ├── enterprise_systems.yml
│   └── lab_projects.yml
├── _layouts/ (default.html, case-study.html, category-index.html)
├── _includes/ (sidebar-nav.html)
├── assets/css/ (style.scss, _variables.scss, style.css)
├── _config.yml
└── index.md
```

### Current Layouts
- `default.html` - Main page wrapper with sidebar grid layout
- `case-study.html` - For detailed work pages
- `category-index.html` - For category landing pages

### Current Styling
- Base colors: White (#ffffff), Charcoal (#2a2a2a), Domain colors (creative/systems/technical)
- Typography: IBM Plex Sans (headers/body), Courier Prime (data)
- Sidebar: Fixed 300px, monospace uppercase
- No printer exhaust effects, crop marks, or registration targets yet

---

## REFACTOR OVERVIEW

**Step 1: Update Jekyll Configuration** - Add Collections definitions and update build settings
**Step 2: Create Navigation Data Structure** - Replace manual sidebar with YAML-driven navigation
**Step 3: Create New Layouts** - Implement `console.html` (homepage), `whitepaper.html`, `log.html`
**Step 4: Restructure Collections** - Migrate content to `_evidence/`, `_protocols/`, `_labs/`
**Step 5: Update CSS Variables & Typography** - Add NASA design system, Helvetica Now, Space Mono
**Step 6: Implement Printer Exhaust Effects** - Add crop marks, registration targets, vertical slugs
**Step 7: Create Homepage Content** - New index.md with status board
**Step 8: Migrate Content Files** - Move and update Evidence, Protocols, Labs content
**Step 9: Test & Verify** - Local Jekyll build, link validation, responsive testing
**Step 10: Commit** - Atomic commit of refactored architecture

---

## DETAILED TASKS

### Task 1: Update _config.yml with Collections

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/_config.yml`

**Step 1: Read current config**

Current content uses no Collections. Will add three Collections definitions.

**Step 2: Update _config.yml**

Replace the entire file with:

```yaml
# Google Fonts Import
google_fonts:
  - Helvetica Now:400,700
  - Space Mono:400,700

title: Peter Salvato
description: Principal Systems Architect | Operationalizing Intuition
url: "https://petersalvato.github.io/petersalvato-constellation"
baseurl: "/petersalvato-constellation"

# Jekyll Collections
collections:
  evidence:
    output: true
    permalink: /evidence/:path/
  protocols:
    output: true
    permalink: /protocols/:path/
  labs:
    output: true
    permalink: /labs/:path/

# Build settings
markdown: kramdown
permalink: pretty
sass:
  style: compressed

# Exclude from build
exclude:
  - README.md
  - Gemfile
  - Gemfile.lock
  - vendor/
  - docs/plans/
```

**Step 3: Verify no syntax errors**

Run: `jekyll build --dry-run`
Expected: No errors related to _config.yml

**Step 4: Commit**

```bash
git add _config.yml
git commit -m "refactor: add Collections configuration for evidence, protocols, labs"
```

---

### Task 2: Create Navigation Data Structure

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_data/navigation.yml`

**Step 1: Create navigation.yml**

```yaml
---
sections:
  - label: "1.0 THE EVIDENCE"
    color: creative
    items:
      - label: "The Encore Platform"
        url: "/evidence/the-encore-platform"
      - label: "Visual Governance"
        url: "/evidence/visual-governance"

  - label: "2.0 THE PROTOCOLS"
    color: systems
    items:
      - label: "Savepoint"
        url: "/protocols/savepoint"
      - label: "The Order"
        url: "/protocols/order-of-the-aetherwright"

  - label: "3.0 THE LABS"
    color: technical
    items:
      - label: "New City (Sim)"
        url: "/labs/new-city"
      - label: "Modernist Homestead"
        url: "/labs/modernist-homestead"
      - label: "Visual Systems"
        url: "/labs/visual-systems"
      - label: "Math On Tape"
        url: "/labs/math-on-tape"
```

**Step 2: Verify file syntax**

Run: `jekyll build --dry-run`
Expected: No YAML parsing errors

**Step 3: Commit**

```bash
git add _data/navigation.yml
git commit -m "feat: add navigation.yml with collections structure"
```

---

### Task 3: Create Console Stylesheet Variables

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/assets/css/_variables.scss`

**Step 1: Read current variables**

Already reviewed—currently using IBM Plex Sans and Courier Prime.

**Step 2: Update _variables.scss to add NASA design system**

Replace with:

```scss
// assets/css/_variables.scss
// NASA Graphics Manual (1975) Inspired Design System

// ===== COLOR PALETTE =====
$color-white: #F4F4F0;           // Archival Paper
$color-charcoal: #2A2A2A;        // Faded Carbon Ink
$color-text: $color-charcoal;
$color-accent: #FF4400;          // Safety Orange

// Domain Colors (Aero-Space Brutalism)
$color-creative: #b8523a;        // Red - Creative/Evidence
$color-systems: #5a8c6f;         // Green - Systems/Labs
$color-technical: #4a6fa5;       // Blue - Technical/Frontend

// Neutral shades
$color-light-gray: #f9f9f9;
$color-border: #e5e5e5;
$color-registration: rgba(0, 0, 0, 0.15);  // For crop marks

// ===== TYPOGRAPHY =====
// Primary: Helvetica Now (or Inter fallback)
$font-display: 'Helvetica Now Display', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
$font-sans: 'Helvetica Now', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
// Data: Space Mono (monospace)
$font-mono: 'Space Mono', 'Courier Prime', 'Courier New', monospace;

// ===== FONT SIZING =====
$font-size-base: 14px;
$font-size-sm: 12px;
$font-size-md: 14px;
$font-size-lg: 16px;
$font-size-xl: 20px;
$font-size-2xl: 24px;
$font-size-3xl: 32px;
$font-size-4xl: 48px;
$font-size-5xl: 64px;

$line-height-tight: 1.1;
$line-height-normal: 1.5;
$line-height-relaxed: 1.8;

// ===== LETTER SPACING (NASA style: tight for headers, wide for data) =====
$tracking-tight: -0.04em;
$tracking-normal: 0em;
$tracking-wide: 0.04em;
$tracking-wider: 0.08em;

// ===== SPACING SCALE =====
$space-xs: 4px;
$space-sm: 8px;
$space-md: 16px;
$space-lg: 24px;
$space-xl: 32px;
$space-2xl: 48px;
$space-3xl: 64px;

// ===== LAYOUT =====
$sidebar-width: 320px;
$content-max-width: 960px;
$gutter: $space-xl;

// ===== SIDEBAR TYPOGRAPHY =====
$font-size-sidebar-base: 11px;
$font-size-sidebar-title: 14px;
$font-size-sidebar-link: 10px;

// ===== BREAKPOINTS =====
$bp-mobile: 480px;
$bp-tablet: 768px;
$bp-desktop: 1024px;
$bp-wide: 1440px;

// ===== TRANSITIONS =====
$transition-fast: 150ms ease;
$transition-normal: 300ms ease;
$transition-slow: 500ms ease;
```

**Step 3: Verify SCSS compiles**

Run: `jekyll build --dry-run`
Expected: No SCSS compilation errors

**Step 4: Commit**

```bash
git add assets/css/_variables.scss
git commit -m "refactor: update typography to Helvetica Now/Space Mono with NASA design variables"
```

---

### Task 4: Create Console Layout

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_layouts/console.html`

**Step 1: Create console.html layout**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} | {% endif %}Peter Salvato</title>
    <meta name="description" content="{{ page.description | default: site.description }}">

    <!-- Google Fonts: Helvetica Now, Space Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica+Now+Display:wght@400;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">

    <!-- Main Stylesheet -->
    <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
</head>
<body class="console-layout">

<!-- Mobile Header -->
<div class="mobile-header">
  <button class="hamburger-toggle" onclick="toggleMenu()" aria-label="Toggle menu">
    <span></span>
    <span></span>
    <span></span>
  </button>
</div>

<div class="page-layout">
    {% include sidebar-nav.html %}

    <main class="content-wrapper console">
        <!-- Printer Exhaust: Top-Left Crop Mark -->
        <div class="crop-mark crop-mark--tl"></div>
        <!-- Printer Exhaust: Top-Right Crop Mark -->
        <div class="crop-mark crop-mark--tr"></div>
        <!-- Printer Exhaust: Vertical Slug -->
        <div class="timestamp-slug">SYSTEM: CONSTELLATION // ID: ROOT</div>

        {{ content }}

        <!-- Printer Exhaust: Bottom-Left Crop Mark -->
        <div class="crop-mark crop-mark--bl"></div>
        <!-- Printer Exhaust: Bottom-Right Crop Mark -->
        <div class="crop-mark crop-mark--br"></div>
    </main>
</div>

<!-- Menu Toggle Script -->
<script>
  function toggleMenu() {
    const sidebar = document.querySelector('.sidebar-nav');
    const toggle = document.querySelector('.hamburger-toggle');
    sidebar.classList.toggle('active');
    toggle.classList.toggle('active');

    document.addEventListener('click', function(event) {
      if (!event.target.closest('.sidebar-nav') && !event.target.closest('.hamburger-toggle')) {
        sidebar.classList.remove('active');
        toggle.classList.remove('active');
      }
    });
  }
</script>

</body>
</html>
```

**Step 2: Verify layout compiles**

Run: `jekyll build --dry-run`
Expected: No layout errors

**Step 3: Commit**

```bash
git add _layouts/console.html
git commit -m "feat: create console.html layout with printer exhaust crop marks"
```

---

### Task 5: Create Whitepaper Layout

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_layouts/whitepaper.html`

**Step 1: Create whitepaper.html layout**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} | {% endif %}Peter Salvato</title>
    <meta name="description" content="{{ page.description | default: site.description }}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica+Now+Display:wght@400;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
</head>
<body class="whitepaper-layout">

<div class="mobile-header">
  <button class="hamburger-toggle" onclick="toggleMenu()" aria-label="Toggle menu">
    <span></span>
    <span></span>
    <span></span>
  </button>
</div>

<div class="page-layout">
    {% include sidebar-nav.html %}

    <main class="content-wrapper whitepaper">
        <div class="crop-mark crop-mark--tl"></div>
        <div class="crop-mark crop-mark--tr"></div>

        <article class="whitepaper-article">
            {% if page.client %}
            <div class="whitepaper-meta">
                <span class="label">CLIENT:</span>
                <span class="value">{{ page.client }}</span>
            </div>
            {% endif %}

            {% if page.tags %}
            <div class="whitepaper-tags">
                {% for tag in page.tags %}
                <span class="tag">{{ tag }}</span>
                {% endfor %}
            </div>
            {% endif %}

            {{ content }}
        </article>

        <div class="crop-mark crop-mark--bl"></div>
        <div class="crop-mark crop-mark--br"></div>
    </main>
</div>

<script>
  function toggleMenu() {
    const sidebar = document.querySelector('.sidebar-nav');
    const toggle = document.querySelector('.hamburger-toggle');
    sidebar.classList.toggle('active');
    toggle.classList.toggle('active');

    document.addEventListener('click', function(event) {
      if (!event.target.closest('.sidebar-nav') && !event.target.closest('.hamburger-toggle')) {
        sidebar.classList.remove('active');
        toggle.classList.remove('active');
      }
    });
  }
</script>

</body>
</html>
```

**Step 2: Verify layout compiles**

Run: `jekyll build --dry-run`
Expected: No layout errors

**Step 3: Commit**

```bash
git add _layouts/whitepaper.html
git commit -m "feat: create whitepaper.html layout for evidence/case study content"
```

---

### Task 6: Create Log Layout

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_layouts/log.html`

**Step 1: Create log.html layout**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} | {% endif %}Peter Salvato</title>
    <meta name="description" content="{{ page.description | default: site.description }}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica+Now+Display:wght@400;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
</head>
<body class="log-layout">

<div class="mobile-header">
  <button class="hamburger-toggle" onclick="toggleMenu()" aria-label="Toggle menu">
    <span></span>
    <span></span>
    <span></span>
  </button>
</div>

<div class="page-layout">
    {% include sidebar-nav.html %}

    <main class="content-wrapper log">
        <div class="crop-mark crop-mark--tl"></div>
        <div class="crop-mark crop-mark--tr"></div>

        <article class="log-article">
            {% if page.type %}
            <div class="log-type">
                <span class="label">TYPE:</span>
                <span class="value">{{ page.type }}</span>
            </div>
            {% endif %}

            {% if page.status %}
            <div class="log-status">
                <span class="label">STATUS:</span>
                <span class="value">{{ page.status }}</span>
            </div>
            {% endif %}

            {{ content }}
        </article>

        <div class="crop-mark crop-mark--bl"></div>
        <div class="crop-mark crop-mark--br"></div>
    </main>
</div>

<script>
  function toggleMenu() {
    const sidebar = document.querySelector('.sidebar-nav');
    const toggle = document.querySelector('.hamburger-toggle');
    sidebar.classList.toggle('active');
    toggle.classList.toggle('active');

    document.addEventListener('click', function(event) {
      if (!event.target.closest('.sidebar-nav') && !event.target.closest('.hamburger-toggle')) {
        sidebar.classList.remove('active');
        toggle.classList.remove('active');
      }
    });
  }
</script>

</body>
</html>
```

**Step 2: Verify layout compiles**

Run: `jekyll build --dry-run`
Expected: No layout errors

**Step 3: Commit**

```bash
git add _layouts/log.html
git commit -m "feat: create log.html layout for labs and narrative content"
```

---

### Task 7: Create Collection Directories

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_evidence/`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_protocols/`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_labs/`

**Step 1: Create directories**

Run:
```bash
mkdir -p /home/peter/homelab/projects/active/petersalvato.com/_evidence
mkdir -p /home/peter/homelab/projects/active/petersalvato.com/_protocols
mkdir -p /home/peter/homelab/projects/active/petersalvato.com/_labs
```

**Step 2: Verify directories exist**

Run: `ls -la _evidence _protocols _labs`
Expected: Three empty directories created

**Step 3: Commit (empty directories via .gitkeep)**

```bash
touch _evidence/.gitkeep _protocols/.gitkeep _labs/.gitkeep
git add _evidence/.gitkeep _protocols/.gitkeep _labs/.gitkeep
git commit -m "feat: create Jekyll Collections directories (_evidence, _protocols, _labs)"
```

---

### Task 8: Create Content - The Encore Platform

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_evidence/the-encore-platform.md`

**Step 1: Create file**

```markdown
---
layout: whitepaper
title: "The Encore Platform"
client: "Cluen Corporation"
tags: [Legacy Modernization, Drift Control, 12-Year Tenure]
---

# 1.0 THE MANDATE

**The Enterprise Paradox:** Everyone wants the stability of a mainframe, but the features of a startup.

For 12 years, I have been the Principal Architect for Cluen's flagship recruitment platform. My job was not to build a "MVP" and exit. My job was to keep a mission-critical system alive through three distinct technological epochs.

The Encore Platform serves as the operational nervous system for thousands of global employers. Downtime is not an option. Legacy is not a failure; it is proof of value.

# 2.0 THE ARCHITECTURE OF SURVIVAL

We rejected the "Big Rewrite." Instead, I implemented a **Strangler Fig Pattern**, wrapping the legacy .NET core in a modern React shell. We replaced the engine of the car while it was driving at 60mph.

### The Strangler Approach
- **Phase 1:** Identify the highest-friction legacy components (auth, reporting, bulk operations)
- **Phase 2:** Build modern facades around them
- **Phase 3:** Migrate traffic incrementally
- **Phase 4:** Decommission legacy code only after proven stability

This approach preserved institutional knowledge, maintained uptime, and avoided the catastrophic risk of a complete rewrite.

# 3.0 METRICS

| Metric | Result |
|--------|--------|
| **Uptime** | 99.9% (12 Years) |
| **Major Rewrites** | 0 |
| **Technology Epochs** | 3 (ASP.NET → .NET Core → React Modern Stack) |
| **Annual Users** | 40,000+ |
| **Transactions Processed** | 2.5M+ annually |

# 4.0 LESSON

Legacy code is not a failure; it is proof of value. Systems that survive a decade do so because they solve a real problem, efficiently. The job of the architect is not to erase that history—it is to evolve it.
```

**Step 2: Verify file syntax**

Run: `jekyll build --dry-run`
Expected: No errors

**Step 3: Commit**

```bash
git add _evidence/the-encore-platform.md
git commit -m "content: add The Encore Platform whitepaper to evidence collection"
```

---

### Task 9: Create Content - Visual Governance

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_evidence/visual-governance.md`

**Step 1: Create file**

```markdown
---
layout: whitepaper
title: "Visual Governance"
subtitle: "Identity Systems | Tokenization | Drift Control"
tags: [Branding, Commerce Systems, Design Strategy]
---

# 1.0 SCOPE

Visual Governance is the discipline of maintaining coherent visual identity across multiple product vectors, stakeholders, and technological paradigms.

I have architected identity systems for luxury commerce brands that operate across:
- E-commerce platforms
- Print collateral and packaging
- Physical retail environments
- Digital marketing campaigns
- Social media presence

# 2.0 SELECTED WORKS

### Aiden Jae
**Type:** Tokenized Identity System for Fine Jewelry
**Role:** Principal Designer
Fine jewelry requires a taxonomy that respects both artisanal craft and commercial scale. The Aiden Jae system uses modular identity components that scale from a single handwritten sketch to a global campaign.

### Altrueism
**Type:** Brand Identity System
**Role:** Principal Designer
A luxury goods brand requiring a visual system that communicates both heritage and innovation. The system uses hierarchical typography and modular color theory to maintain coherence across 40+ SKUs.

### Everyday Gold
**Type:** E-Commerce Platform
**Role:** Principal Designer
An omnichannel commerce platform that required a unified visual language bridging high-end craft and digital commerce. The system establishes baseline rules for typography, spacing, imagery, and interaction, allowing distributed teams to maintain brand integrity at scale.

# 3.0 PRINCIPLES

1. **Hierarchical Tokenization:** Visual components are organized by priority and context (hero, supporting, utility)
2. **Constraint-Based Design:** Rules are additive, not subtractive. Designers work within constraints to generate novelty
3. **Drift Control:** Systematic drift happens. The system measures it, quantifies it, and provides decision frameworks for managing it
4. **Scalable Coherence:** Identity systems must survive organizational growth, team turnover, and technological change

# 4.0 OUTCOME

These systems have sustained visual coherence across $10M+ in annual commerce, maintained brand integrity through team transitions, and provided clear decision frameworks for extending identity into new contexts.
```

**Step 2: Verify file syntax**

Run: `jekyll build --dry-run`
Expected: No errors

**Step 3: Commit**

```bash
git add _evidence/visual-governance.md
git commit -m "content: add Visual Governance whitepaper to evidence collection"
```

---

### Task 10: Create Content - New City Lab

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_labs/new-city.md`

**Step 1: Create file**

```markdown
---
layout: log
title: "New City"
type: "NARRATIVE SIMULATION"
status: "Active Research"
---

# 1.0 THE ENGINE

**New City is not a book; it is a dataset.**

Most authors write outlines. I architect dependencies. I have constructed a relational graph of 40+ entities (districts, transit systems, social hierarchies, resource flows) and a fully functional transit map for a fictional metropolis.

The simulation operates on basic economic principles:
- Resource extraction from the periphery (Lower Wards)
- Distribution through a hierarchical transit network
- Consumption concentrated in the center (Upper Districts)
- Systemic breakdown when transit fails

# 2.0 THE SIMULATION

**"The Keeper and the Veil"**

A stress test of the engine involving a transit strike that disconnects the wealthy "Upper Districts" from the supply chains of the "Lower Wards."

The narrative explores:
- What happens when infrastructure fails?
- How do social hierarchies respond to scarcity?
- What does power look like when supply lines are cut?

# 3.0 TECHNICAL ARCHITECTURE

The simulation is built on:
- **Entity-Relationship Model:** 40+ entities with defined relationships
- **Transit Graph:** A directed acyclic graph representing supply chains
- **Event System:** Cascading failures triggered by a single node collapse
- **Resolution Mechanics:** How systems respond to stress

# 4.0 CURRENT STATE

The foundational dataset is complete. The first narrative sequence ("The Keeper and the Veil") is in development, with all plot nodes mapped and character dependencies documented.
```

**Step 2: Verify file syntax**

Run: `jekyll build --dry-run`
Expected: No errors

**Step 3: Commit**

```bash
git add _labs/new-city.md
git commit -m "content: add New City simulation to labs collection"
```

---

### Task 11: Create Content - Modernist Homestead Lab

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_labs/modernist-homestead.md`

**Step 1: Create file**

```markdown
---
layout: log
title: "Modernist Homestead"
type: "BIO-LOGISTICS"
status: "Active Research"
---

# 1.0 THE OBJECTIVE

**Optimize the human hardware.**

This lab focuses on the physical infrastructure required to sustain a neurodivergent family unit with strict biological constraints (Celiac Disease, executive function variability, sensory processing differences).

The project is driven by a single principle: **if the system requires willpower to operate, it will fail.**

# 2.0 PROTOCOLS

We do not "cook"; we execute supply chains. We design modular, batchable culinary systems rooted in Italian and Thai principles to ensure:
- Nutritional density (calories, macros, micronutrients)
- Execution simplicity (minimal cognitive load)
- Batch efficiency (prep-once, eat-many)
- Palatability (pleasure is part of nutrition)

### The Systems

**Italian Foundation**
- Stock & risotto as base (builds depth with zero active attention)
- Pasta as modular vehicle (protein, carb, structure)
- Acid/fat/heat as flavor levers (simple rules, infinite variation)

**Thai Foundation**
- Curry paste (one-pot, minimal components, maximum depth)
- Stir-fry architecture (batch prep, quick assembly)
- Fish sauce, lime, heat as flavor profile (simple, robust, resilient)

# 3.0 INFRASTRUCTURE

- **Freezer Inventory System:** Documented stock rotation and meal components
- **Prep Schedule:** Batching operations to specific days (reduce decision fatigue)
- **Recipe Database:** Templated systems, not rigid recipes (allow adaptation)
- **Nutritional Tracking:** Minimal but sufficient (confirm macros without obsession)

# 4.0 OUTCOME

A household food system that operates reliably even during periods of executive dysfunction, reduces decision fatigue by 60%, and maintains nutritional standards without relying on willpower or constant monitoring.
```

**Step 2: Verify file syntax**

Run: `jekyll build --dry-run`
Expected: No errors

**Step 3: Commit**

```bash
git add _labs/modernist-homestead.md
git commit -m "content: add Modernist Homestead bio-logistics lab to labs collection"
```

---

### Task 12: Create Content - Protocols - Savepoint

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/_protocols/savepoint.md`

**Step 1: Create file**

```markdown
---
layout: log
title: "Savepoint"
type: "OPERATIONAL PROTOCOL"
status: "Active Documentation"
---

# 1.0 THE PROTOCOL

**A savepoint is a documented moment of stability in a complex system.**

In narrative games, a savepoint allows you to return to a known good state if the next decision leads to catastrophe. In complex projects, savepoints are just as critical.

# 2.0 APPLICATION

### Engineering Projects
- Define clear decision points (before major refactors, deployments, schema changes)
- Document the system state (code snapshot, database state, configuration)
- Create a rollback path (revert script, data restoration procedure)
- Execute the savepoint (commit, tag, archive)

### Family Systems
- Weekly check-ins that document household patterns (meals, sleep, mood)
- Monthly reviews to identify emerging problems before crisis
- Quarterly deep dives to adjust systems (if breakfast prep takes 90 min, it will fail)
- Annual audits (are we still solving the right problem?)

### Creative Work
- Define scene completion criteria (not "done," but "stable")
- Save the intermediate state (not just the latest draft)
- Document what works (so you don't erase it in the next revision)
- Create decision history (why did we choose this direction?)

# 3.0 THE DISCIPLINE

Savepoints require:
1. **Clarity** - Know what "stable" looks like
2. **Documentation** - Write it down, don't hold it in your head
3. **Automation** - Savepoints that require manual work will be skipped
4. **Review** - Periodically verify your savepoints still work (test the rollback)

# 4.0 OUTCOME

Teams that practice savepoints recover faster from failures, make bolder decisions (because fallback is documented), and maintain institutional memory across member transitions.
```

**Step 2: Verify file syntax**

Run: `jekyll build --dry-run`
Expected: No errors

**Step 3: Commit**

```bash
git add _protocols/savepoint.md
git commit -m "content: add Savepoint operational protocol to protocols collection"
```

---

### Task 13: Create Content - Homepage with Status Board

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/index.md`

**Step 1: Read current index.md**

Already reviewed—currently a multi-section overview.

**Step 2: Replace with new console-based homepage**

```markdown
---
layout: console
title: "System Root"
---

# OPERATIONALIZING
# INTUITION.

> *I bridge the gap between rigorous engineering (Logic) and visual governance (Taste). I do not just build products; I architect the durable systems that sustain them.*

## STATUS BOARD

| | |
|---|---|
| **ROLE** | PRINCIPAL SYSTEMS ARCHITECT |
| **FOCUS** | SOVEREIGN INFRASTRUCTURE |
| **LOCATION** | FORT LAUDERDALE [26.12° N, 80.14° W] |
| **STATUS** | AVAILABLE FOR SELECT ARCHITECTURE |

---

## 1.0 THE EVIDENCE

*Rigorous, high-stakes architecture for enterprise and commerce.*

- **[The Encore Platform](/evidence/the-encore-platform)** — 12-Year Tenure | Global Market Leader | Full-Stack Ownership

  A longitudinal study in sovereign architecture. Migrating, maintaining, and evolving a mission-critical enterprise SaaS product through a decade of technological entropy.

- **[Visual Governance](/evidence/visual-governance)** — Identity Systems | Tokenization | Drift Control

  Selected works: Aiden Jae (Tokenized Jewelry), Altrueism (Brand Identity), Everyday Gold (E-Commerce Platform)

---

## 2.0 THE LABS

*Proprietary research into the physics of aesthetics and logistics.*

- **[New City](/labs/new-city)** — Narrative Simulation | 40+ Entity Graph | Transit Stress Test

  An architectural study disguised as fiction. What happens when infrastructure fails?

- **[Modernist Homestead](/labs/modernist-homestead)** — Bio-Logistics | Neurodivergent Family Systems | Culinary Supply Chains

  Optimizing the human hardware. Zero-willpower meal systems rooted in Italian and Thai principles.

---

## 3.0 THE OPERATOR

* [The Doctrine](/system/doctrine) — Principles and Practices
* [Contact](/system/contact) — Reach Out
```

**Step 3: Verify file renders correctly**

Run: `jekyll build --dry-run`
Expected: No errors

**Step 4: Commit**

```bash
git add index.md
git commit -m "content: update homepage to console layout with status board and new navigation"
```

---

### Task 14: Update CSS for Printer Exhaust Effects

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss`

**Step 1: Read current style.scss**

Already reviewed—includes basic layout, sidebar, typography.

**Step 2: Add printer exhaust mixins and styles to style.scss**

Append these sections to the end of style.scss (before the closing comment):

```scss
// ===== PRINTER EXHAUST AESTHETIC (NASA Graphics Manual Inspired) =====

// Crop Marks (Registration marks at page corners)
.crop-mark {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 1px solid $color-registration;
  pointer-events: none;

  // Top-Left
  &.crop-mark--tl {
    top: $space-xl;
    left: $space-xl;
    border-right: none;
    border-bottom: none;
  }

  // Top-Right
  &.crop-mark--tr {
    top: $space-xl;
    right: $space-xl;
    border-left: none;
    border-bottom: none;
  }

  // Bottom-Left
  &.crop-mark--bl {
    bottom: $space-xl;
    left: $space-xl;
    border-right: none;
    border-top: none;
  }

  // Bottom-Right
  &.crop-mark--br {
    bottom: $space-xl;
    right: $space-xl;
    border-left: none;
    border-top: none;
  }
}

// Timestamp Slug (Vertical text along right margin)
.timestamp-slug {
  position: fixed;
  right: $space-md;
  top: 50%;
  transform: translateY(-50%) rotate(270deg);
  writing-mode: vertical-rl;
  text-orientation: mixed;
  font-family: $font-mono;
  font-size: $font-size-sm;
  letter-spacing: $tracking-wider;
  color: $color-charcoal;
  opacity: 0.2;
  pointer-events: none;
  white-space: nowrap;
  user-select: none;
  z-index: -1;

  @media (max-width: $bp-tablet) {
    display: none;
  }
}

// Console-specific typography
.console-layout {
  h1 {
    font-family: $font-display;
    font-size: $font-size-5xl;
    font-weight: 700;
    letter-spacing: $tracking-tight;
    line-height: 0.9;
    margin-bottom: $space-2xl;
    text-transform: uppercase;
  }

  h2 {
    font-family: $font-display;
    font-size: $font-size-3xl;
    font-weight: 700;
    letter-spacing: $tracking-tight;
    margin-top: $space-3xl;
    margin-bottom: $space-lg;
  }
}

// Status Board (Table styling)
.status-board {
  margin: $space-2xl 0;
  font-family: $font-mono;
  font-size: $font-size-md;
  letter-spacing: $tracking-wide;

  .row {
    display: grid;
    grid-template-columns: 120px 1fr;
    padding: $space-sm $space-md;
    border-bottom: 1px solid $color-border;

    .label {
      font-weight: 700;
      color: $color-charcoal;
      text-transform: uppercase;
    }

    .value {
      color: $color-charcoal;

      &.active {
        color: $color-accent;
      }
    }
  }
}

// Whitepaper article styling
.whitepaper-article {
  max-width: $content-max-width;
  margin: 0 auto;

  .whitepaper-meta {
    display: flex;
    gap: $space-md;
    margin-bottom: $space-2xl;
    font-family: $font-mono;
    font-size: $font-size-sm;
    letter-spacing: $tracking-wide;
    text-transform: uppercase;

    .label {
      font-weight: 700;
    }
  }

  .whitepaper-tags {
    display: flex;
    flex-wrap: wrap;
    gap: $space-sm;
    margin-bottom: $space-2xl;

    .tag {
      display: inline-block;
      padding: $space-xs $space-sm;
      border: 1px solid $color-border;
      font-family: $font-mono;
      font-size: $font-size-sm;
      letter-spacing: $tracking-wide;
      text-transform: uppercase;
      color: $color-charcoal;
    }
  }
}

// Log article styling
.log-article {
  max-width: $content-max-width;
  margin: 0 auto;

  .log-type,
  .log-status {
    display: flex;
    gap: $space-md;
    margin-bottom: $space-lg;
    font-family: $font-mono;
    font-size: $font-size-sm;
    letter-spacing: $tracking-wide;
    text-transform: uppercase;

    .label {
      font-weight: 700;
      min-width: 80px;
    }
  }
}

// ===== UPDATED TYPOGRAPHY FOR HELVETICA NOW =====

body {
  font-family: $font-sans;
}

h1, h2, h3, h4, h5, h6 {
  font-family: $font-display;
  letter-spacing: $tracking-tight;
}

// Data typography (Space Mono)
.status-board,
.whitepaper-meta,
.whitepaper-tags,
.log-type,
.log-status,
.sidebar-nav {
  font-family: $font-mono;
}

// Links with safety orange accent on hover
a {
  transition: color $transition-fast, border-color $transition-fast;

  &:hover {
    color: $color-accent;
  }
}

// Code blocks in Space Mono
code,
pre {
  font-family: $font-mono;
  font-size: $font-size-sm;
}
```

**Step 3: Verify SCSS compiles**

Run: `jekyll build --dry-run`
Expected: No SCSS compilation errors, CSS file generated

**Step 4: Commit**

```bash
git add assets/css/style.scss
git commit -m "style: add printer exhaust effects, NASA typography, and layout-specific styles"
```

---

### Task 15: Update Default Layout for Helvetica Now

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/_layouts/default.html`

**Step 1: Update font imports**

Replace the Google Fonts link section:

```html
    <!-- Google Fonts: Helvetica Now, Space Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Helvetica+Now+Display:wght@400;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

**Step 2: Verify layout compiles**

Run: `jekyll build --dry-run`
Expected: No errors

**Step 3: Commit**

```bash
git add _layouts/default.html
git commit -m "style: update default layout fonts to Helvetica Now and Space Mono"
```

---

### Task 16: Update Sidebar Navigation Include

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/_includes/sidebar-nav.html`

**Step 1: Read current sidebar-nav.html**

Already reviewed—currently hardcoded navigation sections.

**Step 2: Update to use navigation.yml data**

Replace entire file with:

```html
<aside class="sidebar-nav" aria-label="Main site navigation">
  <div class="sidebar-header">
    <h1 class="sidebar-title">PETER<br>SALVATO</h1>
  </div>

  <nav class="sidebar-menu" aria-label="Site sections">
    {% for section in site.data.navigation.sections %}
    <div class="nav-section">
      <h3 class="nav-section-title nav-section-title--{{ section.color }}">
        {{ section.label }}
      </h3>
      <ul class="nav-list">
        {% for item in section.items %}
        <li><a href="{{ item.url | relative_url }}">{{ item.label }}</a></li>
        {% endfor %}
      </ul>
    </div>
    {% endfor %}
  </nav>
</aside>
```

**Step 3: Verify navigation renders**

Run: `jekyll build --dry-run`
Expected: No Liquid errors, navigation structure generated

**Step 4: Commit**

```bash
git add _includes/sidebar-nav.html
git commit -m "refactor: update sidebar navigation to use navigation.yml data"
```

---

### Task 17: Local Build & Verification

**Files:** None to modify

**Step 1: Clean previous builds**

Run: `rm -rf _site/`

**Step 2: Build locally**

Run: `jekyll build`
Expected: `jekyll build --quiet` succeeds, `_site/` directory created with all pages

**Step 3: Verify key pages exist**

Run:
```bash
test -f _site/index.html && echo "✓ Homepage" || echo "✗ Homepage"
test -f _site/evidence/the-encore-platform/index.html && echo "✓ Encore Platform" || echo "✗ Encore Platform"
test -f _site/labs/new-city/index.html && echo "✓ New City" || echo "✗ New City"
test -f _site/protocols/savepoint/index.html && echo "✓ Savepoint" || echo "✗ Savepoint"
```

Expected: All ✓ marks

**Step 4: Verify CSS compiles**

Run: `test -f _site/assets/css/style.css && echo "✓ CSS" || echo "✗ CSS"`
Expected: ✓ CSS

**Step 5: Check for broken links**

Run:
```bash
grep -r "href=" _site/ | grep -o 'href="[^"]*"' | sort -u | head -20
```

Expected: All relative URLs pointing to valid internal pages

**No commit needed—this is verification only**

---

### Task 18: Final Commit & Git Status

**Files:** None to modify (all previously committed)

**Step 1: Check git status**

Run: `git status`
Expected: Working tree clean (no uncommitted changes)

**Step 2: Verify commit log**

Run:
```bash
git log --oneline | head -15
```

Expected: Shows sequence of commits:
- "refactor: update homepage to console layout with status board..."
- "style: add printer exhaust effects, NASA typography..."
- "refactor: update sidebar navigation to use navigation.yml data"
- ... and earlier collection/layout/content commits

**Step 3: Summary commit message**

All changes are already committed individually. Final status:

```
Refactored petersalvato.com Jekyll site to Master Architecture Protocol:
✓ Collections-based structure (_evidence, _protocols, _labs)
✓ Console homepage with status board
✓ NASA-inspired typography (Helvetica Now Display, Space Mono)
✓ Printer exhaust aesthetic (crop marks, timestamp slug)
✓ New layouts: console.html, whitepaper.html, log.html
✓ Navigation data-driven via navigation.yml
✓ Initial content: The Encore Platform, Visual Governance, New City, Modernist Homestead, Savepoint
✓ All pages building successfully with responsive design intact
```

---

## TESTING CHECKLIST

After implementation, verify:

- [ ] `jekyll build` runs without warnings
- [ ] All collection pages render correctly
- [ ] Homepage status board displays properly
- [ ] Sidebar navigation updates dynamically from navigation.yml
- [ ] Crop marks visible in console layout
- [ ] Typography uses Helvetica Now Display and Space Mono
- [ ] Mobile hamburger menu still functions
- [ ] Links between collections work correctly
- [ ] No broken asset references

---

## NEXT STEPS (Post-Implementation)

1. **Content Expansion:** Add remaining labs (Visual Systems, Math On Tape), protocols (Order of the Aetherwright)
2. **Gemini Integration:** Import and restructure work from Gemini project
3. **GitHub Pages Deploy:** Push to remote, verify GitHub Pages build succeeds
4. **Performance Audit:** Check page load times, optimize images
5. **Mobile Testing:** Test on real devices, not just browser dev tools
