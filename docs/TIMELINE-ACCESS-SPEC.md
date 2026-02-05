# Timeline Access Design Specification

**Document Type:** Implementation Specification
**Phase:** 2, Week 1, Task 2.3
**Purpose:** Define how 8,922+ extraction entries are accessed, filtered, and presented
**Status:** Ready for Checkpoint 2.1 Review

---

## Timeline Assets Available

### Master Timeline
- **File:** `/docs/extraction_timelines/MASTER-TIMELINE.md`
- **Content:** 8,922 chronological entries
- **Format:** Markdown with structured entries
- **Scope:** All extraction across all 20 projects
- **Date Range:** 2023-01-01 through 2024-12-31 (approximately)

### Individual Project Timelines
- **Files:** 21 project-specific timeline files in `/docs/extraction_timelines/`
- **Count:** One per project across all tiers
- **Format:** Markdown with chronological entries
- **Example files:**
  - `savepoint-protocol-timeline.md`
  - `aiden-jae-timeline.md`
  - `order-of-the-aetherwright-timeline.md`
  - `new-city-timeline.md`
  - `modernist-homestead-timeline.md`
  - [16 more project timelines]

### Index Document
- **File:** `/docs/extraction_timelines/_INDEX.md`
- **Content:** Manifest of all timeline files
- **Purpose:** Navigation and file reference

---

## Timeline Access Design Decision

**Selected: Option A (Separate Pages)**

Why:
- Clear separation of content types (case study vs. timeline)
- Timeline-specific features (filtering, sorting) easier to implement
- Mobile-friendly (don't load all 8,922 entries at once)
- Users consciously choose to enter timeline research
- Performance maintained (no bloated case study pages)

---

## Information Architecture for Timelines

### Master Timeline Page

**URL:** `/timelines/`
**Purpose:** Entry point to extraction research and timeline exploration
**User Intent:** "Show me all the thinking across all projects"

**Content Layout:**

```
/timelines/ (Master Timeline Index)
│
├─ Header Section
│  ├─ Title: "Extraction Timelines"
│  ├─ Subtitle: "8,922+ entries of research, ideation, and iteration"
│  └─ Brief explanation of what timelines contain
│
├─ Quick Stats
│  ├─ Total entries: 8,922
│  ├─ Project count: 20
│  ├─ Date range: 2023-01-01 to 2024-12-31
│  └─ Last updated: [date]
│
├─ Master Timeline Viewer
│  ├─ Display: Last 50 entries (most recent first)
│  ├─ Each entry shows:
│  │  ├─ Date
│  │  ├─ Project name (link to project timeline)
│  │  ├─ Entry snippet (first 200 characters)
│  │  ├─ Expandable detail
│  │  └─ Link to full entry context
│  │
│  ├─ Controls
│  │  ├─ Project filter dropdown
│  │  ├─ Date range picker
│  │  ├─ Sort order toggle (newest/oldest first)
│  │  └─ Load more button
│  │
│  └─ Optional: Platform filter (Claude/Gemini/etc.)
│
├─ Project Timeline Links
│  ├─ Savepoint Protocol (487 entries)
│  ├─ Aiden-Jae (456 entries)
│  ├─ Aetherwright (512 entries)
│  ├─ New City (498 entries)
│  ├─ Modernist Homestead (445 entries)
│  └─ [15 more projects with entry counts]
│
└─ About This Section
   ├─ Why timelines exist (show research depth)
   ├─ How to use them (browsing, filtering, interpreting)
   └─ How entries relate to case studies
```

---

### Individual Project Timeline Pages

**URL:** `/timelines/[project-slug]/`
**Example:** `/timelines/savepoint-protocol/`
**Purpose:** Deep dive into one project's entire research history

**Content Layout:**

```
/timelines/savepoint-protocol/ (Project Timeline)
│
├─ Header Section
│  ├─ Project name: "Savepoint Protocol"
│  ├─ Link to case study: [link]
│  └─ Quick stats for this project
│
├─ Project Stats
│  ├─ Total entries: 487
│  ├─ Date range: 2023-02-15 to 2024-11-30
│  ├─ Conversations: [count]
│  └─ Key topics: [auto-generated or manual tags]
│
├─ Navigation
│  ├─ Link to Master Timeline
│  ├─ "Other Projects" sidebar
│  │  ├─ Savepoint Protocol (current)
│  │  ├─ Aiden-Jae
│  │  ├─ Aetherwright
│  │  └─ [all projects listed]
│  │
│  └─ Search/Filter Controls
│     ├─ Date range picker
│     ├─ Keyword search
│     ├─ Topic filter (if available)
│     └─ Sort order (newest/oldest)
│
├─ Timeline Entries (Chronological)
│  ├─ Grouped by month
│  │
│  ├─ [Month header: February 2023]
│  │  ├─ Entry 1 (2023-02-15)
│  │  │  ├─ Date/time
│  │  │  ├─ Snippet (first 300 characters)
│  │  │  ├─ "Read full entry" link
│  │  │  └─ "Jump to case study section" (if linked)
│  │  │
│  │  ├─ Entry 2 (2023-02-18)
│  │  └─ Entry 3 (2023-02-22)
│  │
│  ├─ [Month header: March 2023]
│  │  ├─ Entry 4 (2023-03-01)
│  │  └─ [more entries]
│  │
│  └─ [Continue through all months]
│
└─ Related Content
   ├─ Link to case study
   ├─ Link to process archive
   └─ Link to master timeline
```

---

## Content Presentation

### Master Timeline Entry Display

**Compact View (default):**
```
2024-12-28 | Savepoint Protocol
Initial exploration of context recovery without manual logging. What if
savepoint captures not just code state but decision context?

[Expand] [View Project Timeline] [More]
```

**Expanded View:**
```
2024-12-28 — Savepoint Protocol
Context recovery design

Initial exploration of context recovery without manual logging. What if
savepoint captures not just code state but decision context? Different from
version control because it's about decision history, not file history.

Questions: Can we make recovery automatic? What needs to be captured?

Platform: Claude (Claude.com)
Related entries: [link], [link]
Read in project timeline: [link]
```

### Individual Timeline Entry Display

**Standard View:**
```
[Date/Time] — [Topic]

[Full entry text - 200-500 words typically]

---
Connections: [Link to other dated entries], [Link to case study section]
Related project: [Link if it affects other projects]
```

---

## Navigation & Discovery

### Discovery Paths

**Path 1: From case study page**
```
Case Study Page (/systems/aiden-jae)
    ↓
Sidebar widget: "Full Conversation Timeline"
    ↓
Individual project timeline (/timelines/aiden-jae)
    ↓
Browse 456 entries chronologically
    ↓
Optional: Jump to master timeline, explore other projects
```

**Path 2: From process archive**
```
Process Archive (/process-archives/aiden-jae)
    ↓
Inline link: "See the full research timeline"
    ↓
Individual project timeline (/timelines/aiden-jae)
```

**Path 3: Direct research interest**
```
Master Timeline (/timelines/)
    ↓
Browse recent entries or filter by project
    ↓
Click "View Project Timeline" on entry
    ↓
Project timeline (/timelines/[project]/), full context
    ↓
Optional: Explore connected entries
```

**Path 4: Specialist exploration**
```
Master Timeline (/timelines/)
    ↓
Filter by date range (e.g., "Jan 2024 - Mar 2024")
    ↓
Browse subset of 200-300 entries
    ↓
Identify pattern or trend
    ↓
Jump to project timeline for deep dive
```

---

## Implementation Approach

### Option A: Static Markdown Pages (Recommended)

**Why static:**
- No build complexity (Jekyll native)
- No JavaScript required
- Fast loading
- Future-proof (no database dependencies)
- Git-versioned and auditable

**How it works:**

1. **Existing files used as-is**
   - Master timeline already exists at `/docs/extraction_timelines/MASTER-TIMELINE.md`
   - Individual project timelines already exist
   - No modification needed to timeline content

2. **Create navigation layers**
   - Create `/timelines/index.html` or `/timelines/index.md` that:
     - Lists all 20 projects with entry counts
     - Shows quick stats
     - Links to individual project timelines
     - Optionally embeds first 50 master timeline entries

3. **Link structure**
   - Case study pages link to individual project timeline
   - Individual project timeline pages link back to case study
   - Master timeline visible via `/timelines/` index

4. **Mobile handling**
   - Master timeline shows paginated view (50 entries per page)
   - Individual timelines load in full (or paginated)
   - Navigation remains accessible

### Option B: Dynamic with Filtering (More Complex)

**Requires:**
- Jekyll plugins for filtering (if local-only)
- OR: Generate static filtered pages during build
- OR: Client-side JavaScript for filtering

**Trade-off:**
- More user-friendly filtering
- More complexity to maintain
- Longer build times
- Requires JavaScript for best experience

**Recommendation:** Start with Option A (static). Add filtering only if needed after launch.

---

## Technical Implementation Details

### Master Timeline Page (`/timelines/index.md`)

**Structure:**
```markdown
---
layout: timeline-index
title: "Extraction Timelines"
---

## Extraction Timelines

8,922+ entries of research, thinking, and iteration across 20 projects.

### Quick Stats
- Total entries: 8,922
- Date range: 2023-01-01 to 2024-12-31
- Projects: 20
- Last updated: [auto-generated date]

### Recent Entries (Master Timeline)
[Embed first 50 entries from MASTER-TIMELINE.md]

### Browse by Project
[Link list with entry counts]
- Savepoint Protocol (487 entries) → /timelines/savepoint-protocol/
- Aiden-Jae (456 entries) → /timelines/aiden-jae/
- [etc.]

### About These Timelines
[Explanation of what timelines are and how to use them]
```

### Project Timeline Pages (`/timelines/[project]/index.md`)

**Structure:**
```markdown
---
layout: timeline-view
title: "Savepoint Protocol - Extraction Timeline"
project: "Savepoint Protocol"
project_url: "/protocols/savepoint-protocol"
timeline_file: "savepoint-protocol-timeline.md"
---

## Savepoint Protocol - Extraction Timeline

487 entries documenting the research, decisions, and thinking behind
Savepoint Protocol.

### Project Stats
- Entries: 487
- Date range: 2023-02-15 to 2024-11-30
- Conversations: [count if available]

### Navigation
- [Back to Master Timeline](/timelines/)
- [Read Case Study](/protocols/savepoint-protocol)
- [See Process Archive](/process-archives/savepoint-protocol)
- [Browse All Projects](/timelines/#projects)

### Timeline
[Full content from savepoint-protocol-timeline.md]
```

---

## Jekyll Configuration

### New Collections (if needed)

Add to `_config.yml`:
```yaml
collections:
  timelines:
    output: true
    permalink: /timelines/:name/
```

Alternatively: Keep timelines as regular pages in `/timelines/` directory.

### New Layouts

Create: `_layouts/timeline-index.html`
- Main timeline index page layout
- Lists projects with entry counts
- Shows recent entries

Create: `_layouts/timeline-view.html`
- Individual project timeline layout
- Chronological entry display
- Navigation back to master and case study

### Data Files (Optional)

Create: `_data/timeline_index.json`
```json
{
  "title": "Extraction Timelines",
  "description": "8,922+ entries of research and thinking",
  "projects": [
    {
      "name": "Savepoint Protocol",
      "url": "/timelines/savepoint-protocol/",
      "entry_count": 487,
      "date_range": "2023-02-15 to 2024-11-30"
    },
    ...
  ]
}
```

---

## User Experience Considerations

### Mobile Experience

**Constraint:** Mobile users shouldn't load all 8,922 entries at once

**Solution:**
- Master timeline shows "last 25 entries" on mobile
- "Load more" or pagination buttons for browsing
- Individual project timelines load in full (or paginated)
- Navigation remains prominent
- Touch-friendly expand/collapse on entries

### Performance

**Goals:**
- Master timeline homepage loads in <1 second
- Individual project timeline loads in <2 seconds
- No blocking JavaScript
- Mobile-friendly file sizes

**Strategy:**
- Don't embed full master timeline in master timeline page
- Show first 50 entries, link to "View More"
- Individual timelines can be larger (users deliberately navigated there)
- Minimize CSS/JS on timeline pages

### Accessibility

**Requirements:**
- Proper heading hierarchy (H1 for page, H2 for sections)
- Date entries clearly marked
- Project names linked with clear link text
- Mobile keyboard navigation works
- Screen reader friendly

---

## Filtering & Search Strategy

### Phase 2 (No Filtering)

**Keep it simple:**
- Master timeline shows recent entries first
- Project timelines show chronological order (oldest first)
- Navigation via links, not search
- Users reach timelines via case study or process archive links

### Optional Future (Phase 3+)

Only add if needed after launch:
- Date range picker (start/end dates)
- Project filter on master timeline
- Keyword search in timelines
- Platform filter (Claude/Gemini/etc.)

**Decision:** Build filtering only if user feedback requests it.

---

## Links from Case Studies

### On case study pages, add sidebar widget:

```html
<div class="timeline-link">
  <h4>Full Conversation Timeline</h4>
  <p>See all 487 entries documenting the research and iteration behind this work.</p>
  <a href="/timelines/savepoint-protocol/">Explore the Timeline</a>
</div>
```

**Styling:**
- Secondary prominence (lower opacity, smaller text)
- Positioned after main article
- Clear link text

---

## Content Guidelines

### What Goes in Timelines

**Include:**
- Research conversations and ideation
- Key decisions and decision-making process
- Failed experiments and learnings
- Implementation challenges and solutions
- Thinking that shaped the final result
- Platform-specific constraints and adaptations

**Format:**
- Chronological order (date and time if available)
- Conversation context preserved
- Entry length: 100-1000 words typically
- Grouped by month or project phase

**Don't modify:**
- Existing timeline files are complete
- No editing or filtering of content
- No removal of entries (even "boring" ones)
- Present research as-is, not curated

### Voice in Timeline Context

**Timelines are raw research.** The voice may vary because they're direct from conversation. This is intentional—it shows unfiltered thinking.

**On page:** Brief intro explaining "These are raw extraction entries. Voice and formality vary. They represent real-time thinking, not polished writing."

---

## Integration Across Layers

### How Three Layers Connect

```
Case Study (Layer 1) — Public, primary narrative
    ↓
"How This Was Built" link
    ↓
Process Archive (Layer 2) — Strategic decisions, constraints
    ↓
"See the Full Timeline" link (optional)
    ↓
Extraction Timeline (Layer 3) — Raw research, thinking process
    ↓
"See Decision in Case Study" (optional)
    ↓
Back to Case Study
```

### Cross-Links Strategy

**Case Study → Process Archive:** Direct link in sidebar

**Case Study → Timeline:** Direct link in sidebar

**Process Archive → Timeline:** Inline link (optional) in narrative

**Timeline → Case Study:** Link to relevant case study section (optional)

**Timeline → Master Timeline:** "Browse all projects" link from individual timeline

---

## Success Criteria - Timeline Access

✓ Master timeline accessible at `/timelines/`
✓ All 20 individual project timelines accessible at `/timelines/[project]/`
✓ 8,922+ entries organized chronologically
✓ Entry counts accurate and visible
✓ Case studies link to individual timelines
✓ Mobile responsive and performant
✓ No modification to existing timeline files
✓ Clear navigation between master and individual timelines
✓ Obvious relationship between layers (case study → archive → timeline)
✓ All links working (no 404s)

---

## Implementation Checklist

### Week 2 Tasks

**Files to Create:**
- [ ] `_layouts/timeline-index.html` (Master timeline page layout)
- [ ] `_layouts/timeline-view.html` (Individual project timeline layout)
- [ ] `/timelines/index.md` (Master timeline index)
- [ ] `/timelines/savepoint-protocol/index.md` (Project timeline page)
- [ ] `/timelines/aiden-jae/index.md` (Project timeline page)
- [ ] `/timelines/aetherwright/index.md` (Project timeline page)
- [ ] `/timelines/new-city/index.md` (Project timeline page)
- [ ] `/timelines/modernist-homestead/index.md` (Project timeline page)
- [ ] `/timelines/[18 more projects]/index.md` (Project timeline pages for all projects)
- [ ] `_data/timeline_index.json` (Timeline metadata)

**Files to Modify:**
- [ ] Case study layouts (add timeline sidebar widget)
- [ ] Case study pages (add timeline links)
- [ ] `_config.yml` (if adding new collection)

**Files NOT to Modify:**
- All timeline content files in `/docs/extraction_timelines/`
- All case study content
- All process archive content (not yet written)

---

## Styling Guidance

### Timeline Entry Styling

```scss
.timeline-entry {
  margin: 1.5rem 0;
  padding: 1rem;
  border-left: 3px solid var(--color-secondary);

  .entry-date {
    font-weight: 600;
    color: var(--color-text-secondary);
    margin-bottom: 0.5rem;
  }

  .entry-content {
    line-height: 1.6;
  }
}

.timeline-entry.expanded {
  border-left-color: var(--color-primary);
}
```

### Master Timeline Controls

```scss
.timeline-controls {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;

  select, input {
    padding: 0.5rem;
    border: 1px solid var(--color-border);
  }
}
```

---

## Next Steps

1. **Week 1:** This spec complete (Task 2.3)
2. **Week 2:** Create timeline layouts and pages (Task 2.7)
3. **Week 2:** Add sidebar widgets to case studies
4. **Week 3:** Test all links and navigation
5. **Future:** Add filtering/search if needed

