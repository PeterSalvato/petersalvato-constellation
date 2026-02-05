# Site Architecture: Multi-Layer Structure

**Document Type:** Information Architecture Design
**Phase:** 2, Week 1, Task 2.1
**Purpose:** Define three-layer site structure, navigation model, and user journeys
**Status:** Ready for Checkpoint 2.1 Review

---

## Current State (Phase 1 Complete)

### Layer 1: Main Narrative - Complete
- 5 core case studies rebuilt with extraction-integrated content
- Manifesto repositioned with extraction content visible
- All case studies pass voice consistency and extraction accuracy checks
- Full prominence in primary navigation

**Core Case Studies (5 projects):**
1. **Savepoint Protocol** (Protocols tier, red)
   - File: `_protocols/savepoint-protocol.md`
   - Layout: system-01
   - Status: Complete, voice verified

2. **Aiden-Jae** (Applied Systems tier, blue)
   - File: `_systems/aiden-jae.md`
   - Layout: system-02
   - Status: Complete, voice verified

3. **Aetherwright** (Protocols tier, red)
   - File: `_protocols/order-of-the-aetherwright.md`
   - Layout: system-01
   - Status: Complete, voice verified

4. **New City** (Practice tier, green)
   - File: `_practice/new-city.md`
   - Layout: system-03
   - Status: Complete, voice verified

5. **Modernist Homestead** (Applied Systems tier, blue)
   - File: `_systems/modernist-homestead.md`
   - Layout: system-02
   - Status: Complete, voice verified

### Extraction Timeline Resources Available
- **Master Timeline:** 8,922 entries, chronological
- **Individual Project Timelines:** 20 project files available
- **Location:** `/docs/extraction_timelines/`

---

## Three-Layer Architecture

### Layer 1: Main Narrative (PRIMARY NAVIGATION)

**What:** Core case studies and site-defining content
**User Intent:** "Show me your best work and how you think"
**Navigation Location:** Primary sidebar (fully expanded, always visible)

**Content in Layer 1:**
- 5 rebuilt case studies (Savepoint, Aiden-Jae, Aetherwright, New City, Modernist Homestead)
- Manifesto (homepage)
- Tier landing pages (Protocols, Applied Systems, Practice)
- About/How I Think
- Provenance/Bio

**Navigation Pattern:**
```
Sidebar - Always Visible (250px fixed)
├─ 01. PROTOCOLS (red)
│  ├─ Savepoint Protocol
│  ├─ Order of the Aetherwright
│  ├─ AI DevOps Workbench
│  └─ Portable Agency
├─ 02. APPLIED SYSTEMS (blue)
│  ├─ Encore
│  ├─ Aiden-Jae ← REBUILT
│  ├─ Everyday Gold
│  ├─ Altrueism
│  └─ Modernist Homestead ← REBUILT
├─ 03. PRACTICE (green)
│  ├─ New City ← REBUILT
│  ├─ MathOnTape
│  ├─ Photogeography
│  ├─ The Deep Cuts
│  ├─ Echo & Bone
│  ├─ Versagrams
│  ├─ Cryptozoology
│  ├─ Motorology
│  ├─ Sentimentology
│  └─ Monstrum
└─ ABOUT (neutral)
   ├─ How I Think
   ├─ Provenance
   └─ Colophon
```

**Visual Hierarchy:**
- Full prominence (100% opacity, standard font weight)
- Leading navigation design pattern
- Accessed immediately on site entry

**Success Metric:** Users can access all Layer 1 content with 0 additional clicks

---

### Layer 2: Process Archives (SECONDARY NAVIGATION)

**What:** Decision logs, technical notes, what failed, constraints that shaped thinking
**User Intent:** "How was this built? What decisions shaped this?"
**Navigation Location:** Secondary navigation (discoverable, not primary)

**Content in Layer 2:**
- 5 Process Archive pages (one per core case study)
  - Decision log (key decisions + why)
  - Technical architecture notes
  - What didn't work (experiments + resolution)
  - Constraints and how they shaped thinking
- Target length: 1500-3000 words per project
- Hybrid format: Key decisions as bullets, narrative explanations below

**Organization by Project:**
```
Savepoint Protocol Process Archive
├─ Key Decisions Made
├─ What Didn't Work
├─ Technical Architecture Notes
└─ The Constraints That Shaped Everything

Aiden-Jae Process Archive
├─ Key Decisions Made
├─ What Didn't Work
├─ Technical Architecture Notes
└─ The Constraints That Shaped Everything

[Repeat for Aetherwright, New City, Modernist Homestead]
```

**Navigation Pattern:**

Option A: "How This Was Built" sidebar links on case study pages
```
Case Study Page
├─ Main content (Layer 1)
└─ Sidebar widget
   ├─ How This Was Built → /process-archives/savepoint-protocol
   └─ Full Conversation Timeline → /timelines/savepoint-protocol
```

Option B: Process Archives Index Page
```
/process-archives/
├─ Overview (why this layer exists)
├─ Savepoint Protocol Archive
├─ Aiden-Jae Archive
├─ Aetherwright Archive
├─ New City Archive
└─ Modernist Homestead Archive
```

**Recommendation:** Both approaches combined
- Process Archives Index provides central discovery
- Case study pages have direct links to their archive
- Users find this through deliberate search, not accidentally

**Visual Hierarchy:**
- Subdued prominence (85% opacity, secondary color, smaller text size)
- Nested under main case study navigation
- Clearly distinguished from Layer 1

**Access Journey:**
```
User on case study page
    ↓
Notices "How This Was Built" secondary link
    ↓
Clicks to process archive
    ↓
Reads decision log, technical notes, what failed
    ↓
Optional: Link back to case study or explore other archives
```

**Success Metric:** Interested readers find process archives; casual visitors focus on main case study

---

### Layer 3: Extraction Timelines (TERTIARY NAVIGATION)

**What:** Master timeline (8,922 entries) + 20 individual project timelines
**User Intent:** "Show me the deep research. I want to see the thinking process."
**Navigation Location:** Tertiary navigation (specialized access)

**Content in Layer 3:**
- Master Timeline: All 8,922 extraction entries chronologically
- Individual Project Timelines: One per project (20 files)
- Filterable by project, date range, platform
- Grouped by date, conversation context visible

**Data Source:**
```
Location: /docs/extraction_timelines/
├─ MASTER-TIMELINE.md (8,922 entries)
├─ savepoint-protocol-timeline.md
├─ aiden-jae-timeline.md
├─ order-of-the-aetherwright-timeline.md
├─ new-city-timeline.md
├─ modernist-homestead-timeline.md
├─ [14 more project timelines]
└─ _INDEX.md (manifest)
```

**Navigation Pattern:**

Option A: Deep Research Index
```
/timelines/
├─ Master Timeline (all entries, searchable)
├─ Savepoint Protocol Timeline
├─ Aiden-Jae Timeline
├─ Aetherwright Timeline
├─ New City Timeline
└─ [17 more individual timelines]
```

Option B: Link from case studies
```
Case Study Page
├─ Main content (Layer 1)
└─ Sidebar widget
   ├─ How This Was Built → /process-archives/savepoint-protocol
   └─ Full Conversation Timeline → /timelines/savepoint-protocol
```

**Recommendation:** Both approaches combined
- Master Timeline at `/timelines/` as main entry point
- Individual project timelines accessible from master
- Case study pages link directly to their timeline

**Access Journey:**
```
User on case study page or interested in deep research
    ↓
Clicks "Full Conversation Timeline" link
    ↓
Arrives at individual project timeline
    ↓
Can browse entries, filter by date, explore connections
    ↓
Optional: Return to case study or explore master timeline
```

**Visual Hierarchy:**
- Minimal prominence (75% opacity, tertiary color, small text)
- Only accessible through deliberate action
- Clearly marked as "deep research" / "for specialists"

**Success Metric:** Researchers and interested deep-divers find timelines; general audience doesn't feel overwhelmed

---

## Navigation Design

### Current Primary Navigation (Layer 1 Only)

**URL Structure:**
- `/` — Homepage
- `/protocols/` — Tier landing page
- `/protocols/savepoint-protocol` — Case study
- `/systems/` — Tier landing page
- `/systems/aiden-jae` — Case study
- `/practice/` — Tier landing page
- `/practice/new-city` — Case study
- `/provenance` — About page

**Sidebar Structure (active):**
```
{
  "sections": [
    {
      "label": "01. PROTOCOLS",
      "color": "red",
      "items": [
        { "label": "Savepoint Protocol", "url": "/protocols/savepoint-protocol" },
        [...]
      ]
    },
    [...]
  ]
}
```

### New Navigation (Phase 2 Addition)

**New URL Structure:**
- `/process-archives/` — Process archives index
- `/process-archives/savepoint-protocol` — Savepoint process archive
- `/process-archives/aiden-jae` — Aiden-Jae process archive
- `/process-archives/aetherwright` — Aetherwright process archive
- `/process-archives/new-city` — New City process archive
- `/process-archives/modernist-homestead` — Modernist Homestead process archive

- `/timelines/` — Master timeline
- `/timelines/savepoint-protocol` — Savepoint protocol timeline
- `/timelines/aiden-jae` — Aiden-Jae timeline
- `/timelines/aetherwright` — Aetherwright timeline
- `/timelines/new-city` — New City timeline
- `/timelines/modernist-homestead` — Modernist Homestead timeline
- `/timelines/[project-name]` — Individual project timelines (20 projects)

**Sidebar Structure (after Phase 2):**
```
{
  "sections": [
    {
      "label": "01. PROTOCOLS",
      "color": "red",
      "items": [
        { "label": "Savepoint Protocol", "url": "/protocols/savepoint-protocol" },
        { "label": "Order of the Aetherwright", "url": "/protocols/order-of-the-aetherwright" },
        [...]
      ]
    },
    [...]
  ],
  "secondary": {
    "label": "PROCESS ARCHIVES",
    "color": "neutral",
    "items": [
      { "label": "How Work Gets Built", "url": "/process-archives/" },
      { "label": "Savepoint Decision Log", "url": "/process-archives/savepoint-protocol" },
      [...]
    ]
  },
  "tertiary": {
    "label": "EXTRACTION TIMELINES",
    "color": "neutral",
    "items": [
      { "label": "Master Timeline", "url": "/timelines/" },
      { "label": "Research Archives", "url": "/timelines/" },
    ]
  }
}
```

**Alternative: Nested Secondary Navigation**
Instead of expanding sidebar, secondary/tertiary accessible via:
1. Case study page sidebar widgets
2. Dedicated index pages (`/process-archives/`, `/timelines/`)
3. Footer navigation

**Recommendation:** Keep primary navigation clean, use case study page widgets + index pages

---

## Site Map (Hierarchical)

```
petersalvato.com
│
├─ / (Homepage - Manifesto)
│
├─ Layer 1: Main Narrative
│  ├─ /protocols/ (Tier landing page)
│  │  ├─ /protocols/savepoint-protocol (CORE CASE STUDY)
│  │  ├─ /protocols/order-of-the-aetherwright (CORE CASE STUDY)
│  │  ├─ /protocols/ai-devops-workbench
│  │  └─ /protocols/portable-agency
│  │
│  ├─ /systems/ (Tier landing page)
│  │  ├─ /systems/encore
│  │  ├─ /systems/aiden-jae (CORE CASE STUDY)
│  │  ├─ /systems/everyday-gold
│  │  ├─ /systems/altrueism
│  │  └─ /systems/modernist-homestead (CORE CASE STUDY)
│  │
│  ├─ /practice/ (Tier landing page)
│  │  ├─ /practice/new-city (CORE CASE STUDY)
│  │  ├─ /practice/mathontape
│  │  ├─ /practice/photogeography
│  │  ├─ /practice/the-deep-cuts
│  │  ├─ /practice/echo-and-bone
│  │  ├─ /practice/versagrams
│  │  ├─ /practice/cryptozoology
│  │  ├─ /practice/motorology
│  │  ├─ /practice/sentimentology
│  │  ├─ /practice/monstrum
│  │  └─ /practice/colophon
│  │
│  └─ About Section
│     ├─ /how-i-think
│     ├─ /provenance
│     └─ /practice/colophon
│
├─ Layer 2: Process Archives (NEW)
│  ├─ /process-archives/ (Index page - "How Work Gets Built")
│  ├─ /process-archives/savepoint-protocol
│  ├─ /process-archives/aiden-jae
│  ├─ /process-archives/aetherwright
│  ├─ /process-archives/new-city
│  └─ /process-archives/modernist-homestead
│
└─ Layer 3: Extraction Timelines (NEW)
   ├─ /timelines/ (Master timeline index)
   ├─ /timelines/savepoint-protocol
   ├─ /timelines/aiden-jae
   ├─ /timelines/aetherwright
   ├─ /timelines/new-city
   ├─ /timelines/modernist-homestead
   └─ /timelines/[18 more project timelines]
```

---

## User Journeys

### Journey 1: "I want to see your best work"

**User Type:** Hiring manager, potential client, curious visitor
**Entry Point:** Homepage

```
/
    ↓
Reads manifesto (value proposition)
    ↓
Clicks tier landing page (Protocols, Systems, Practice)
    ↓
Browses case study titles
    ↓
Clicks Savepoint Protocol (or other core case study)
    ↓
Reads full case study (Layer 1)
    ↓
Optional: Explores other case studies in same tier
    ↓
Exit or read About/Provenance
```

**Navigation Elements Used:** Homepage link, sidebar navigation (Layer 1 only)
**Time Investment:** 15-30 minutes
**Success:** Case study fully understood, no awareness of Layer 2/3 needed

---

### Journey 2: "How was this decision made?"

**User Type:** Builder, strategist, fellow practitioner
**Entry Point:** Case study page

```
/protocols/savepoint-protocol (Layer 1)
    ↓
Reads case study
    ↓
Notices "How This Was Built" sidebar widget
    ↓
Clicks to process archive
    ↓
/process-archives/savepoint-protocol (Layer 2)
    ↓
Reads decision log, technical notes, what failed
    ↓
Understands thinking and constraints
    ↓
Optional: Returns to case study with new context
```

**Navigation Elements Used:** Case study sidebar widget
**Time Investment:** 30-45 minutes
**Success:** Process visible, decisions understood, constraints clear

---

### Journey 3: "I want to see the raw research"

**User Type:** Researcher, deep practitioner, obsessive learner
**Entry Point:** Case study page (or direct search)

```
/systems/aiden-jae (Layer 1)
    ↓
Reads case study
    ↓
Notices "Full Conversation Timeline" sidebar widget
    ↓
Clicks to extraction timeline
    ↓
/timelines/aiden-jae (Layer 3)
    ↓
Browses 8,922+ entries chronologically
    ↓
Filters by date range or searches for topics
    ↓
Reads full conversation context
    ↓
Optional: Explores connections to other projects
```

**Navigation Elements Used:** Case study sidebar widget, timeline filtering
**Time Investment:** 60-120+ minutes
**Success:** Deep research accessible, thinking process visible

---

### Journey 4: "I'm designing a system. Show me how you think."

**User Type:** Fellow designer/architect
**Entry Point:** Search or direct link

```
/process-archives/ (Layer 2 index)
    ↓
Browses five process archives
    ↓
Selects Aiden-Jae (most relevant to jewelry/luxury positioning)
    ↓
Reads decision log, technical notes, constraints
    ↓
Follows connections to case study or timeline
    ↓
Extracts patterns applicable to own work
```

**Navigation Elements Used:** Layer 2 index, case study sidebar widgets
**Time Investment:** 45-60 minutes
**Success:** Decision-making process visible, patterns extractable

---

### Journey 5: "I want to understand your methodology"

**User Type:** Potential partner, researcher, methodology student
**Entry Point:** Homepage or direct navigation

```
/ (Homepage)
    ↓
Reads manifesto (Narrative + Visual + Technical unified)
    ↓
Selects Protocol tier
    ↓
/protocols/ (landing page)
    ↓
Reads Savepoint Protocol (foundational logic)
    ↓
/process-archives/savepoint-protocol (constraints that shaped it)
    ↓
/timelines/savepoint-protocol (deep research)
    ↓
Visits other protocols to validate consistency
    ↓
Reads Applied Systems to see methodology in production
    ↓
Exits with clear understanding of coherent methodology
```

**Navigation Elements Used:** All layers
**Time Investment:** 120-180 minutes
**Success:** Methodology clear, consistency evident across projects

---

## Content Structure Changes

### No Changes to Layer 1
- All existing case study files remain unchanged
- All URLs preserved
- All layouts preserved
- No breaking changes

### New Collections/Files for Layer 2

**Directory:** `_process/` (new collection)

**Files (5 total):**
- `_process/savepoint-protocol.md`
- `_process/aiden-jae.md`
- `_process/aetherwright.md`
- `_process/new-city.md`
- `_process/modernist-homestead.md`

**Frontmatter:**
```yaml
---
layout: process-archive
title: "Savepoint Protocol - Process Archive"
project_url: "/protocols/savepoint-protocol"
---
```

**Or: Single Index Page**
```
/process-archives/index.md
├─ Overview
├─ Savepoint Protocol Archive
├─ Aiden-Jae Archive
├─ [etc.]
```

### New Collections/Files for Layer 3

**Existing Timeline Files (already present):**
- Location: `/docs/extraction_timelines/`
- Count: 22 files (1 master + 21 projects)
- Content: Already complete, no modification needed

**Navigation Landing Page:**
```
/timelines/index.md
├─ Master Timeline (links to or embeds MASTER-TIMELINE.md)
├─ Individual project timeline links
├─ Search/filter explanation
```

---

## Navigation Data Structure

### Current (navigation.json)
```json
{
  "sections": [
    { "label": "01. PROTOCOLS", "color": "red", "items": [...] },
    { "label": "02. APPLIED SYSTEMS", "color": "blue", "items": [...] },
    { "label": "03. PRACTICE", "color": "green", "items": [...] },
    { "label": "ABOUT", "color": "neutral", "items": [...] }
  ]
}
```

### Updated (navigation.json - Phase 2)
```json
{
  "sections": [
    { "label": "01. PROTOCOLS", "color": "red", "items": [...] },
    { "label": "02. APPLIED SYSTEMS", "color": "blue", "items": [...] },
    { "label": "03. PRACTICE", "color": "green", "items": [...] },
    { "label": "ABOUT", "color": "neutral", "items": [...] }
  ],
  "secondary": {
    "label": "PROCESS ARCHIVES",
    "description": "How work gets built: decisions, technical choices, constraints",
    "items": [
      { "label": "Browse All", "url": "/process-archives/" },
      { "label": "Savepoint Decision Log", "url": "/process-archives/savepoint-protocol" }
    ]
  },
  "tertiary": {
    "label": "EXTRACTION TIMELINES",
    "description": "Deep research: 8,922+ entries across 20 projects",
    "items": [
      { "label": "Master Timeline", "url": "/timelines/" },
      { "label": "Project Timelines", "url": "/timelines/" }
    ]
  }
}
```

### New Data Files

**process_index.json:**
```json
{
  "title": "Process Archives",
  "description": "How decisions were made, what failed, constraints that shaped thinking",
  "projects": [
    {
      "name": "Savepoint Protocol",
      "url": "/process-archives/savepoint-protocol",
      "excerpt": "Context leak solution...",
      "tier": "01"
    },
    ...
  ]
}
```

**timeline_index.json:**
```json
{
  "title": "Extraction Timelines",
  "description": "8,922+ entries of research, thinking, and iteration",
  "master_timeline": "/timelines/",
  "projects": [
    {
      "name": "Savepoint Protocol",
      "url": "/timelines/savepoint-protocol",
      "entry_count": 487,
      "date_range": "2024-01-15 to 2024-12-30"
    },
    ...
  ]
}
```

---

## Visual Hierarchy & Styling

### Opacity Levels (CSS)

**Layer 1 (Main Narrative):**
- Text opacity: 100%
- Navigation item opacity: 100%
- Font weight: 400-600 (depending on hierarchy within Layer 1)
- Color: Full saturation

**Layer 2 (Process Archives):**
- Text opacity: 85%
- Navigation item opacity: 80%
- Font weight: 400 (standard)
- Color: Desaturated 20%

**Layer 3 (Extraction Timelines):**
- Text opacity: 75%
- Navigation item opacity: 70%
- Font weight: 400 (standard)
- Color: Desaturated 40%

### Spacing

**Layer 1:** Standard spacing (padding, margins as designed)
**Layer 2:** 10-15% reduced spacing, tighter grouping
**Layer 3:** 20-25% reduced spacing, compact grouping

### Color Strategy

**No new colors added.** Use existing tier colors (red, blue, green) with opacity/desaturation to indicate layer depth.

```
Layer 1: Color at 100% saturation, 100% opacity
Layer 2: Color at 80% saturation, 85% opacity
Layer 3: Color at 60% saturation, 75% opacity
```

---

## Implementation Checklist

### Files to Create
- [ ] `docs/PROCESS-ARCHIVE-STRATEGY.md` (Task 2.2)
- [ ] `docs/TIMELINE-ACCESS-SPEC.md` (Task 2.3)
- [ ] `docs/NAVIGATION-MOCKUP.md` (Task 2.4)
- [ ] `_layouts/process-archive.html` (Task 2.5)
- [ ] `_layouts/timeline-index.html` (Task 2.5)
- [ ] `_process/savepoint-protocol.md` (Task 2.6)
- [ ] `_process/aiden-jae.md` (Task 2.6)
- [ ] `_process/aetherwright.md` (Task 2.6)
- [ ] `_process/new-city.md` (Task 2.6)
- [ ] `_process/modernist-homestead.md` (Task 2.6)
- [ ] `process-archives/index.md` (Task 2.6)
- [ ] `timelines/index.md` (Task 2.7)

### Files to Modify
- [ ] `_config.yml` (add collections if needed)
- [ ] `_data/navigation.json` (add Layer 2/3 links)
- [ ] `_data/process_index.json` (create)
- [ ] `_data/timeline_index.json` (create)
- [ ] `_includes/sidebar-nav.html` (render secondary/tertiary)
- [ ] `_layouts/default.html` (if navigation structure changes)

### Files NOT to Modify
- All 5 case study files (Phase 1 complete)
- All extraction timeline files (already complete)
- Homepage layout (Phase 1 complete)

---

## Success Criteria - Architecture

✓ Three layers clearly defined and distinguished
✓ Navigation intuitive: Layer 1 primary, Layer 2 discoverable, Layer 3 specialist
✓ User journeys documented for each audience type
✓ No URLs removed or broken
✓ No changes to existing case studies
✓ Visual hierarchy using opacity/desaturation (not color change)
✓ Mobile navigation responsive
✓ Search-friendly (all layers accessible via sidebar or index pages)

---

## Next: Task 2.2 - Process Archive Strategy

See `PROCESS-ARCHIVE-STRATEGY.md` for detailed specification of what goes in each archive.

