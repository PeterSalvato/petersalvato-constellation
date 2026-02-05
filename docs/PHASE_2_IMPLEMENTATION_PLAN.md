# Phase 2 Implementation Plan
## Site Architecture, Multi-Layer Structure, Extraction Access

**Phase:** 2 of 4 (Architecture & Multi-Layer Build)
**Duration:** 2-3 weeks (2026-03-10 to 2026-03-31)
**Effort:** 40-50 hours
**Status:** Ready to Begin

---

## Phase 2 Overview

### Purpose
Transform the site from single-layer (case studies only) to multi-layer architecture that surfaces extraction content while maintaining focus and readability.

### Scope
- Update site information architecture
- Create extraction timeline access layer
- Build search/filtering capability
- Add process archive layer
- Update navigation to surface new content
- Implement without breaking current case studies

### Deliverables
- Redesigned information architecture (documented)
- Updated site navigation (responsive, clear)
- Extraction timeline access (working)
- Search/filter functionality (functional)
- Process archive layer (organized)
- Updated homepage (reflective of new structure)

### Success Criteria
- ✓ Site architecture supports multiple content layers
- ✓ Extraction content discoverable without overwhelming main narrative
- ✓ Navigation clear and intuitive
- ✓ Master Builder voice maintained
- ✓ Site builds and deploys without errors
- ✓ Reading experience smooth (not cluttered)

---

## What Phase 2 Does NOT Do

- ✗ Does NOT change case studies (those stay as rebuilt in Phase 1)
- ✗ Does NOT redesign visual aesthetics (focuses on architecture)
- ✗ Does NOT break Master Builder voice
- ✗ Does NOT add animation, complexity, or "features" for feature's sake
- ✗ Does NOT implement full-text search (too complex for scope)

---

## Phase 2 Architecture Approach

### Layer 1: Main Narrative (Current)
- 5 rebuilt case studies (Savepoint, Homestead, Aiden Jae, New City, Aetherwright)
- Homepage with new manifesto
- Tier landing pages (Protocols, Applied Systems, Practice)
- About/Provenance

**Visibility:** Fully prominent, primary navigation

### Layer 2: Process Archives (New)
- Decision logs for each project
- Technical architecture notes
- Design system documentation
- What didn't work explanations

**Visibility:** Secondary navigation, discoverable but not primary focus

### Layer 3: Extraction Timelines (New)
- Master timeline (all 8,922 entries chronologically)
- Individual project timelines (all 20 projects)
- Indexed by date, project, platform
- Search/filter by project or date range

**Visibility:** Tertiary, specialized access (for deep research)

### Navigation Model

**Homepage:**
- New manifesto (extraction-informed)
- Introduction to three layers
- Quick links to each tier

**Tier Pages (Protocols/Systems/Practice):**
- Core case studies (Layer 1)
- Link to process archives (Layer 2)
- Link to extraction timelines (Layer 3)

**Project Pages (Individual Case Studies):**
- Full case study (Layer 1)
- "How This Was Built" sidebar → process archive (Layer 2)
- "Full Conversation Timeline" link → extraction timeline (Layer 3)

**New: Process Archive Pages**
- Decision log for project (why choices made)
- Technical decisions documented
- Failed experiments explained
- Constraints and how they shaped thinking

**New: Timeline Access**
- Master timeline searchable by project
- Individual project timelines chronological
- Filter by date range
- Show/hide by platform

---

## Technical Implementation

### Jekyll Structure Changes

**New Collections (if needed):**
- `_process` — Process archive pages
- `_timelines` — Timeline index pages (optional, timelines already exist)

**New Data Files:**
- `_data/process_index.json` — Links to process docs
- `_data/timeline_index.json` — Links to timeline files

**New Layouts:**
- `process-archive.html` — Process documentation layout
- `timeline-index.html` — Timeline access layout
- `timeline-view.html` — Display individual timeline

**Updated Layouts:**
- `default.html` — Update navigation structure
- `domain-index.html` — Update tier pages (add Layer 2/3 links)

**Updated Navigation:**
- `_data/navigation.json` — Add Layer 2 and 3 links
- `_includes/sidebar-nav.html` — Adjust presentation

### CSS/Styling Considerations

**Goals:**
- Layer 2 and 3 content clearly distinguished from Layer 1
- Secondary content visually deprioritized (not hidden)
- Mobile-friendly navigation
- No increase in page load times

**Approach:**
- Use subtle visual hierarchy (opacity, color, spacing)
- Collapsible sections for Layer 2/3 on case study pages
- Separate pages for timeline access (don't inline)
- Progressive disclosure (more detail on demand)

---

## Phase 2 Weekly Breakdown

### Week 1 (2026-03-10 to 2026-03-17): Architecture Design & Planning

**Task 2.1: Information Architecture Document** (3-4 hours)
- Define exact layer structure
- Map current pages to new structure
- Design navigation model
- Create site map (visual)
- Document user journeys (how to access each layer)

**Deliverable:** Architecture document with diagrams

**Task 2.2: Process Archive Strategy** (2-3 hours)
- Define what goes in each project's process archive
- Decide on structure (decision log vs. narrative vs. bullet points)
- Create template for process docs
- Identify key decisions to document for each project

**Deliverable:** Process archive template and strategy doc

**Task 2.3: Timeline Access Design** (2-3 hours)
- Define how timelines will be accessed
- Decide on filtering/search approach (simple or advanced?)
- Plan master timeline presentation
- Design individual timeline presentation

**Deliverable:** Timeline access specification

**Task 2.4: Navigation Mockup** (2-3 hours)
- Sketch how navigation will change
- Show how users access Layer 2 and 3
- Plan mobile experience
- Document all navigation changes

**Deliverable:** Navigation mockup and plan

---

### Week 2 (2026-03-17 to 2026-03-24): Implementation

**Task 2.5: Update Jekyll Templates** (8-10 hours)
- Update `default.html` with new navigation structure
- Create/update layout files for process archives
- Create layout files for timeline access
- Implement Layer 2/3 navigation links
- Ensure no breaking changes to current pages

**Task 2.6: Create Process Archive Pages** (8-10 hours)
- Write process archive for each of 5 projects
- For each: decision log, technical notes, what failed, what surprised
- Create individual pages or single collection
- Link from case studies
- Maintain Master Builder voice

**Task 2.7: Implement Timeline Access** (6-8 hours)
- Create timeline index pages
- Implement filtering/navigation for timelines
- Link from case studies to relevant timelines
- Create master timeline navigation
- Test all links

**Task 2.8: Update Navigation Data** (3-4 hours)
- Update `_data/navigation.json`
- Create `_data/process_index.json`
- Create `_data/timeline_index.json`
- Update homepage links
- Verify all navigation working

---

### Week 3 (2026-03-24 to 2026-03-31): Testing, Refinement, Deployment

**Task 2.9: Build & Test** (4-5 hours)
- Full Jekyll build
- Test all new pages
- Verify no 404s
- Check navigation thoroughly
- Mobile testing

**Task 2.10: Voice Consistency Audit** (3-4 hours)
- Read all new process archive pages
- Verify Master Builder voice maintained
- Check for jargon, marketing language
- Refine as needed

**Task 2.11: Content Refinement** (4-5 hours)
- Refine process archives based on feedback
- Adjust timeline presentation if needed
- Update navigation labels for clarity
- Optimize content for readability

**Task 2.12: Performance & Optimization** (2-3 hours)
- Check page load times
- Optimize CSS if needed
- Ensure no breaking changes
- Verify deployment ready

**Task 2.13: Final Testing & Deployment** (3-4 hours)
- Comprehensive final build
- All pages render correctly
- All links working
- Ready for go-live

---

## Key Design Decisions to Make

### Question 1: How Prominent Should Layer 2 (Process) Be?

**Option A: Discoverable but Not Primary**
- Small "How This Was Built" link in case study sidebar
- Separate pages (don't inline)
- Only accessed by users interested in process

**Option B: More Prominent**
- "Process Architecture" section on each case study
- Expanded sidebar with process links
- More visible in navigation

**Option C: Integrated into Case Study**
- Process documentation embedded in case study
- "How This Was Built" section within article
- Same page, just separated by scrolling

**Recommendation:** Option A (discoverable but secondary)
- Keeps Layer 1 (case studies) primary
- Respects user who just want the work
- Process available for those interested
- Doesn't clutter main narrative

---

### Question 2: How Should Timeline Content Be Accessed?

**Option A: Separate Pages**
- `/timelines/savepoint-protocol/` shows timeline
- Master timeline at `/timelines/`
- Search by project or date

**Option B: Embedded in Case Studies**
- Timeline data displayed on case study page
- Can filter/expand
- Everything in one place

**Option C: Dedicated Timeline Section**
- `/research/` or `/thinking/` as main entry
- All timelines browsable
- Master timeline primary view

**Recommendation:** Option A (separate pages)
- Clear separation of content types
- Timeline-specific features (filtering, sorting) easier to implement
- Doesn't bloat case study pages
- Mobile-friendly (don't need to load all timeline data)

---

### Question 3: Process Archive Structure?

**Option A: Decision Logs**
- Bulleted decisions for each project
- Why chosen, what alternatives, what failed
- Scan-friendly format

**Option B: Narrative Prose**
- Written like mini-essays
- Explains thinking and context
- Reads like articles

**Option C: Hybrid**
- Key decisions as bullets
- Narrative explanations below
- Best of both

**Recommendation:** Option C (hybrid)
- Supports different reading styles
- Decisions scannable, explanations available
- Maintains Master Builder voice
- Not overwhelming

---

## Content Specification: Process Archives

### What Goes in Each Project's Process Archive

**Template for Each Project:**

```
# Project Name - Process Archive

## Key Decisions Made

- **Decision 1:** Why chosen, what considered, what failed
- **Decision 2:** Why chosen, what considered, what failed
- [Continue for 5-8 key decisions]

## What Didn't Work (and Why We Fixed It)

- Experiment 1: What was tried, why failed, how resolved
- Experiment 2: What was tried, why failed, how resolved

## Technical Architecture Notes

- Platform choice: Why selected, constraints
- Integration points: How systems talk to each other
- Scaling considerations: What limits exist, how addressed

## The Constraints That Shaped Everything

- Constraint 1: How it forced clarity
- Constraint 2: How it drove innovation
- Constraint 3: How it became a feature

## What We'd Do Differently

- If starting over, what would change?
- What principles held, what would adjust?
- How did this inform other projects?
```

**Tone:** Master Builder (direct, concrete, specific)
**Length:** 1500-3000 words per project
**Voice:** First person, honest about failures

---

## Content Specification: Timeline Access

### Master Timeline Page

**Purpose:** Chronological view of all ideation across all projects

**Content:**
- 8,922 entries in chronological order
- Filterable by project or date range
- Show/hide by platform (Claude, Gemini)
- Quick stats (total entries, date range, etc.)

**User Experience:**
- Default: Show last 50 entries (most recent first)
- Search/filter to narrow
- Expandable detail for each entry
- Link from each entry to full project timeline

### Individual Project Timeline Pages

**Purpose:** Deep dive into one project's ideation history

**Content:**
- All entries for that project chronologically
- Grouped by date
- Show conversation context
- Platform indicator

**User Experience:**
- Can browse or search within
- Link to full conversation entries
- Connections to other projects shown
- Mobile-friendly viewing

---

## Risk Mitigation

### Risk: Site Becomes Confusing With Multiple Layers

**Mitigation:**
- Clear visual separation of layers
- Explicit navigation (don't hide Layer 2/3)
- Test with users (friends, peers)
- Progressive disclosure (more detail on demand)

### Risk: Extraction Content Overwhelming

**Mitigation:**
- Keep Layer 1 (case studies) primary
- Layer 2/3 accessed only by interested users
- Don't inline extraction into case studies
- Careful information architecture

### Risk: Performance Issues With Large Timeline Files

**Mitigation:**
- Load timelines on separate pages (not homepage)
- Use pagination if needed
- Optimize Jekyll build
- Test load times before deployment

### Risk: Breaking Existing Pages

**Mitigation:**
- Don't modify case study files (already complete)
- Add new pages, don't replace old ones
- Preserve all existing URLs
- Thorough testing before deployment

---

## Success Metrics

### Phase 2 Success = All of These:

1. **Information Architecture**
   - ✓ Three layers clearly defined
   - ✓ Navigation intuitive
   - ✓ No dead ends

2. **Content Completeness**
   - ✓ 5 process archive pages written
   - ✓ Timeline access implemented
   - ✓ All links working
   - ✓ No 404s

3. **Voice Consistency**
   - ✓ All new content Master Builder voice
   - ✓ Read-aloud test passes
   - ✓ No jargon, no marketing language
   - ✓ Consistent with Phase 1

4. **Technical Quality**
   - ✓ Site builds without errors
   - ✓ All pages render correctly
   - ✓ Mobile responsive
   - ✓ No breaking changes to existing content
   - ✓ Performance acceptable

5. **User Experience**
   - ✓ Navigation clear and intuitive
   - ✓ Extraction content discoverable
   - ✓ Not overwhelming
   - ✓ Easy to focus on case studies (Layer 1)

---

## Checkpoint Structure

### Checkpoint 2.1 (End Week 1)
**Review:** Architecture and strategy documents
- Is information architecture sound?
- Does process archive strategy work?
- Are timeline access plans feasible?
- Navigation mockups approved?

**Decision:** Proceed to Week 2 or adjust architecture

### Checkpoint 2.2 (End Week 2)
**Review:** All new pages and templates
- Do process archives work?
- Are timelines accessible?
- Navigation functional?
- Voice consistent?

**Decision:** Proceed to Week 3 or refine content

### Checkpoint 2.3 (End Week 3)
**Review:** Final testing and refinement
- All tests pass?
- No 404s or broken links?
- Performance acceptable?
- Ready to deploy?

**Decision:** Approve Phase 2 complete or request final changes

---

## Files Modified/Created

### New Files
- `/docs/process-archive-template.md` (template for process docs)
- `/docs/timeline-access-spec.md` (timeline implementation spec)
- `/docs/site-architecture.md` (IA document)
- `/_process/[project-name].md` (5 files, one per project)
- `/timelines/index.md` (timeline access page)
- `/timelines/[project-name]/index.md` (individual timeline pages)

### Modified Files
- `_data/navigation.json` (add Layer 2/3 links)
- `_data/index.json` (update homepage links)
- `_layouts/default.html` (update navigation)
- `_includes/sidebar-nav.html` (adjust for new structure)
- `_config.yml` (if adding new collections)

### Preserved (No Changes)
- All 5 case study markdown files (Phase 1 complete)
- All extraction timeline files
- Current CSS/styling (no redesign)

---

## Next Step After Phase 2

Once Phase 2 is complete:
- **Phase 3:** Testing, refinement, performance optimization (2 weeks)
- **Phase 4:** Positioning finalization and go-live (2-3 weeks)

Full project timeline:
- Phase 1: Content (complete) ✓
- Phase 2: Architecture (2-3 weeks)
- Phase 3: Testing (2 weeks)
- Phase 4: Launch (2-3 weeks)

**Total remaining:** 6-8 weeks to complete brand reconstruction

---

**Phase 2 Implementation Plan: Ready to Begin**

**Start Date:** 2026-03-10 (Monday)
**Target Completion:** 2026-03-31 (Friday)
**Effort:** 40-50 hours across 2-3 weeks
**Deliverable:** Multi-layer site architecture with extraction access

Let's build the architecture layer.
