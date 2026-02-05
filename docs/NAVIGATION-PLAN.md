# Navigation Plan & Mockup

**Document Type:** Navigation Design & Implementation Guide
**Phase:** 2, Week 1, Task 2.4
**Purpose:** Show how users access Layer 2 and Layer 3, plan navigation changes, document all modifications
**Status:** Ready for Checkpoint 2.1 Review

---

## Current Navigation (Layer 1 Only)

### Sidebar Structure (Active)

**Location:** `_includes/sidebar-nav.html`, driven by `_data/navigation.json`

**Desktop View:**
```
┌─────────────────────────────┐
│     petersalvato.com        │  [Logo/Title]
│                             │
│  01. PROTOCOLS       (red)  │
│  ├─ Savepoint                │
│  ├─ Aetherwright             │
│  ├─ AI DevOps                │
│  └─ Portable Agency          │
│                             │
│  02. APPLIED SYSTEMS (blue) │
│  ├─ Encore                   │
│  ├─ Aiden-Jae                │
│  ├─ Everyday Gold            │
│  ├─ Altrueism                │
│  └─ Modernist Homestead      │
│                             │
│  03. PRACTICE       (green) │
│  ├─ New City                 │
│  ├─ MathOnTape               │
│  ├─ Photogeography           │
│  ├─ The Deep Cuts            │
│  ├─ Echo & Bone              │
│  ├─ Versagrams               │
│  ├─ Cryptozoology            │
│  ├─ Motorology               │
│  ├─ Sentimentology           │
│  └─ Monstrum                 │
│                             │
│  ABOUT            (neutral) │
│  ├─ How I Think              │
│  ├─ Provenance               │
│  └─ Colophon                 │
│                             │
└─────────────────────────────┘
```

**Key Characteristics:**
- Fixed 250px width, always visible
- 4 sections (Protocols, Systems, Practice, About)
- Tier colors (red, blue, green)
- Fully expanded on all pages
- No collapsing/expanding sections

**Data Structure:**
```json
{
  "sections": [
    {
      "label": "01. PROTOCOLS",
      "color": "red",
      "items": [...]
    },
    // ... three more sections
  ]
}
```

---

## Phase 2 Navigation Challenge

**Problem:** How to add 25+ new pages (5 process archives + 20 timelines) without:
1. Overwhelming the sidebar
2. Making layers unclear
3. Breaking the existing design
4. Cluttering navigation

**Constraint:** Keep Layer 1 primary and fully visible. Layer 2/3 discoverable but secondary.

---

## Navigation Design Recommendations

### Option 1: Expandable Secondary Sections (Recommended)

**Approach:**
- Keep Layer 1 (4 sections) exactly as-is
- Add Layer 2 section below Layer 1 (collapsible)
- Add Layer 3 section below Layer 2 (collapsible)
- Each secondary section collapses/expands with toggle

**Sidebar View (Collapsed Secondary):**
```
┌─────────────────────────────┐
│     petersalvato.com        │
│                             │
│  01. PROTOCOLS       (red)  │
│  ├─ Savepoint                │
│  ├─ Aetherwright             │
│  ├─ AI DevOps                │
│  └─ Portable Agency          │
│                             │
│  02. APPLIED SYSTEMS (blue) │
│  ├─ Encore                   │
│  ├─ Aiden-Jae                │
│  ├─ Everyday Gold            │
│  ├─ Altrueism                │
│  └─ Modernist Homestead      │
│                             │
│  03. PRACTICE       (green) │
│  ├─ New City                 │
│  ├─ MathOnTape               │
│  ├─ Photogeography           │
│  ├─ The Deep Cuts            │
│  ├─ Echo & Bone              │
│  ├─ Versagrams               │
│  ├─ Cryptozoology            │
│  ├─ Motorology               │
│  ├─ Sentimentology           │
│  └─ Monstrum                 │
│                             │
│  ABOUT            (neutral) │
│  ├─ How I Think              │
│  ├─ Provenance               │
│  └─ Colophon                 │
│                             │
│  ▼ PROCESS ARCHIVES [+]     │  ← Collapsible
│  ▼ TIMELINES        [+]     │  ← Collapsible
│                             │
└─────────────────────────────┘
```

**When Layer 2 Expanded:**
```
┌─────────────────────────────┐
│     petersalvato.com        │
│                             │
│  01. PROTOCOLS       (red)  │
│  ├─ Savepoint                │
│  ├─ Aetherwright             │
│  ├─ AI DevOps                │
│  ├─ Portable Agency          │
│                             │
│  02. APPLIED SYSTEMS (blue) │
│  ├─ Encore                   │
│  ├─ Aiden-Jae                │
│  ├─ Everyday Gold            │
│  ├─ Altrueism                │
│  └─ Modernist Homestead      │
│                             │
│  03. PRACTICE       (green) │
│  ├─ New City                 │
│  ├─ MathOnTape               │
│  ├─ Photogeography           │
│  ├─ The Deep Cuts            │
│  ├─ Echo & Bone              │
│  ├─ Versagrams               │
│  ├─ Cryptozoology            │
│  ├─ Motorology               │
│  ├─ Sentimentology           │
│  └─ Monstrum                 │
│                             │
│  ABOUT            (neutral) │
│  ├─ How I Think              │
│  ├─ Provenance               │
│  └─ Colophon                 │
│                             │
│  ▲ PROCESS ARCHIVES [-]     │
│  ├─ Browse All Archives      │
│  ├─ Savepoint Decision Log   │
│  ├─ Aiden-Jae Decision Log   │
│  ├─ Aetherwright Decision Log│
│  ├─ New City Decision Log    │
│  └─ Modernist Homestead Log  │
│                             │
│  ▼ TIMELINES        [+]     │
│                             │
└─────────────────────────────┘
```

**Advantages:**
- Layer 1 always fully visible (primary focus)
- Layer 2 discoverable via toggle (secondary)
- Layer 3 discoverable via toggle (tertiary)
- Clean hierarchy through collapse/expand
- No sidebar overflow

**Disadvantages:**
- Requires JavaScript for toggle functionality
- Slightly more complex to maintain
- Mobile considerations (toggles on small screens)

---

### Option 2: Static Footer Navigation

**Approach:**
- Keep sidebar exactly as-is (no changes)
- Add footer section with Layer 2 and 3 links
- Footer appears on every page
- Smaller, secondary-looking text

**Footer View:**
```
[Main content area]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROCESS ARCHIVES: How Work Gets Built
  Savepoint Protocol  |  Aiden-Jae  |  Aetherwright  |  New City  |  Homestead

TIMELINES: Deep Research
  Master Timeline  |  Browse by Project

© Peter Salvato — Colophon — How I Think
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Advantages:**
- No sidebar changes needed
- No JavaScript required
- Clean, minimal presentation
- Mobile-friendly
- Doesn't overwhelm main navigation

**Disadvantages:**
- Layers hidden until page bottom
- Users might miss them (need to scroll)
- Less prominent
- May feel like afterthought placement

---

### Option 3: Case Study Sidebar Widgets Only

**Approach:**
- Keep sidebar navigation unchanged
- Add "How This Was Built" widget to case study pages only
- Widget links to process archive
- Process archive footer links to timeline
- Users discover Layer 2/3 through deliberate navigation

**Case Study Page Layout:**
```
[Sidebar Navigation]  [Main Article]
                      ┌─────────────────────┐
                      │ Case Study Title    │
                      │                     │
                      │ Main article        │
                      │ content...          │
                      │                     │
                      │ [End of article]    │
                      │                     │
                      │ ╔═════════════════╗ │
                      │ ║  HOW THIS WAS   ║ │
                      │ ║  BUILT          ║ │
                      │ ║                 ║ │
                      │ ║ Interested in   ║ │
                      │ ║ decisions,      ║ │
                      │ ║ constraints, &  ║ │
                      │ ║ failures?       ║ │
                      │ ║                 ║ │
                      │ ║ Read the        ║ │
                      │ ║ Process Archive ║ │
                      │ ║   [→ Link]      ║ │
                      │ ╚═════════════════╝ │
                      │                     │
                      │ ╔═════════════════╗ │
                      │ ║  FULL           ║ │
                      │ ║  CONVERSATION   ║ │
                      │ ║  TIMELINE       ║ │
                      │ ║                 ║ │
                      │ ║ 487 entries of  ║ │
                      │ ║ research and    ║ │
                      │ ║ iteration       ║ │
                      │ ║                 ║ │
                      │ ║ Explore Timeline ║ │
                      │ ║   [→ Link]      ║ │
                      │ ╚═════════════════╝ │
                      │                     │
                      │ [Related content]   │
                      └─────────────────────┘
```

**Process Archive Footer Links to Timeline:**
```
[Process Archive Content]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RELATED CONTENT
  Read Case Study
  Explore Full Timeline (487 entries)
  Browse Other Projects
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Advantages:**
- Sidebar completely unchanged
- Layers surface naturally through content
- Progressive discovery (main content → process → timeline)
- No JavaScript needed
- Users find what they need
- Clean, uncluttered sidebar

**Disadvantages:**
- Layers not visible from homepage/index pages
- User must navigate to case study to see Layer 2/3 links
- Less prominent than sidebar option

---

## Recommendation: Hybrid Approach

**Combine Options 2 & 3:**

1. **Keep sidebar exactly as-is** (no changes to existing navigation)
2. **Add Process Archives index link in footer** (every page)
3. **Add Timelines index link in footer** (every page)
4. **Add sidebar widgets to case study pages** (when user is interested)

**Why this works:**
- Layer 1 completely unchanged (existing users see no difference)
- Layer 2 discoverable via footer (visible on every page, but secondary)
- Layer 3 discoverable via footer (visible on every page, but tertiary)
- Case study pages offer quick links (interested users find them immediately)
- Process archive pages link to timelines (natural progression)
- No JavaScript needed
- Clean, coherent information architecture

**Footer Structure:**
```html
<footer class="site-footer">
  <div class="footer-sections">
    <div class="footer-section">
      <h4>PROCESS ARCHIVES</h4>
      <p>How work gets built: decisions, constraints, what failed</p>
      <a href="/process-archives/">Browse All</a>
    </div>

    <div class="footer-section">
      <h4>TIMELINES</h4>
      <p>8,922+ entries of research and thinking</p>
      <a href="/timelines/">Master Timeline</a>
    </div>
  </div>

  <div class="footer-credits">
    [Existing footer content]
  </div>
</footer>
```

---

## Mobile Navigation

### Desktop (≥ 1024px)
- Sidebar always visible (250px fixed)
- Footer at bottom, full width
- Main content offset by sidebar

### Tablet (768px - 1024px)
- Sidebar still visible but narrower (200px)
- Footer at bottom, full width
- Font sizes slightly reduced

### Mobile (< 768px)
- Sidebar becomes hamburger menu (toggle)
- Footer visible, sections condensed
- Links reorganized in readable stack

**Mobile Footer:**
```
[Main Content]

━━━━━━━━━━━━━━━━━━━━━━━━
PROCESS ARCHIVES
Browse All [→]

TIMELINES
Master Timeline [→]

About  Provenance  Colophon
━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Navigation Changes Summary

### Files to Modify

**1. `_includes/sidebar-nav.html`**
- No changes to existing rendering logic
- Remains exactly as-is

**2. `_layouts/default.html`**
- Add footer section if not present
- Add footer CSS import/styling

**3. Create new file: `_includes/footer.html`**
```html
<footer class="site-footer">
  <div class="footer-links-secondary">
    <div class="footer-link-group">
      <h4>PROCESS ARCHIVES</h4>
      <p>How decisions were made. What constraints shaped thinking. What didn't work.</p>
      <a href="/process-archives/">Browse Process Archives</a>
    </div>

    <div class="footer-link-group">
      <h4>TIMELINES</h4>
      <p>8,922+ entries of research, ideation, and iteration across 20 projects.</p>
      <a href="/timelines/">Explore Timelines</a>
    </div>
  </div>

  <hr class="footer-divider">

  <div class="footer-links-primary">
    <a href="/provenance">Provenance</a>
    <a href="/how-i-think">How I Think</a>
    <a href="/practice/colophon">Colophon</a>
  </div>
</footer>
```

**4. Create new file: `assets/css/_footer.scss`** (included in main.scss)
```scss
.site-footer {
  margin-top: 4rem;
  padding: 2rem 1.5rem;
  border-top: 1px solid var(--color-border);
  font-size: 0.9rem;
  color: var(--color-text-secondary);
  opacity: 0.85; // Subtle visual hierarchy
}

.footer-links-secondary {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
}

.footer-link-group {
  h4 {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
    color: var(--color-text-primary);
  }

  p {
    font-size: 0.85rem;
    margin-bottom: 0.75rem;
    line-height: 1.5;
  }

  a {
    display: inline-block;
    text-decoration: underline;
    &:hover {
      opacity: 1;
    }
  }
}

.footer-divider {
  margin: 2rem 0;
  border: none;
  border-top: 1px solid var(--color-border);
}

.footer-links-primary {
  display: flex;
  gap: 1.5rem;
  font-size: 0.85rem;

  a {
    text-decoration: underline;
    &:hover {
      opacity: 1;
    }
  }
}
```

---

## Case Study Sidebar Widgets

### Add to case study layouts (`_layouts/system-02.html`, `_layouts/system-03.html`, etc.)

**Widget HTML:**
```html
<aside class="case-study-sidebar-widgets">

  <div class="widget process-archive-link">
    <h4>How This Was Built</h4>
    <p>The decisions, constraints, and thinking behind this work.</p>
    <a href="/process-archives/{{ page.slug }}">
      Read the Process Archive →
    </a>
  </div>

  <div class="widget timeline-link">
    <h4>Full Conversation Timeline</h4>
    <p>See all {{ page.entry_count | default: '400+' }} entries documenting research and iteration.</p>
    <a href="/timelines/{{ page.slug }}">
      Explore the Timeline →
    </a>
  </div>

</aside>
```

**Widget CSS (in main.scss):**
```scss
.case-study-sidebar-widgets {
  margin: 2rem 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.widget {
  padding: 1rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background-color: var(--color-bg-secondary);
  opacity: 0.85; // Secondary prominence

  h4 {
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
    color: var(--color-text-primary);
  }

  p {
    font-size: 0.85rem;
    margin-bottom: 0.75rem;
    line-height: 1.5;
    color: var(--color-text-secondary);
  }

  a {
    display: inline-block;
    text-decoration: underline;
    font-size: 0.9rem;

    &:hover {
      opacity: 1;
    }
  }
}
```

---

## Navigation Accessibility

### Keyboard Navigation
- All links keyboard accessible (Tab order logical)
- Footer links reachable without scrolling (not required but helpful)
- Case study widgets in natural reading order

### Screen Reader Considerations
- Semantic HTML (footer, aside, nav elements)
- Heading hierarchy maintained
- Link text descriptive ("Read Process Archive" not "Read")
- Alt text for any icons

### WCAG Compliance
- Color contrast meets WCAG AA standards
- Text sizes remain readable
- No information conveyed by color alone
- Mobile touch targets > 44px

---

## Navigation Map (Phase 2)

```
HomePage
├─ Primary Navigation (Sidebar - Layer 1)
│  ├─ 01. PROTOCOLS
│  ├─ 02. APPLIED SYSTEMS
│  ├─ 03. PRACTICE
│  └─ ABOUT
│
├─ Footer (Secondary/Tertiary - Layers 2 & 3)
│  ├─ PROCESS ARCHIVES → /process-archives/
│  └─ TIMELINES → /timelines/
│
└─ [Optional: Mobile hamburger for sidebar]

Case Study Page
├─ Primary Navigation (Sidebar - Layer 1)
│
├─ Main Article (Layer 1 content)
│
├─ Sidebar Widgets (Layer 2 & 3 access)
│  ├─ How This Was Built → /process-archives/[project]
│  └─ Full Conversation Timeline → /timelines/[project]
│
└─ Footer (Secondary navigation)

Process Archive Page
├─ Primary Navigation (Sidebar - Layer 1)
│
├─ Archive Content (Layer 2)
│
├─ Related Links
│  ├─ Read Case Study → /[tier]/[project]
│  └─ Explore Full Timeline → /timelines/[project]
│
└─ Footer

Timeline Page
├─ Primary Navigation (Sidebar - Layer 1)
│
├─ Timeline Content (Layer 3)
│
├─ Related Links
│  ├─ Read Case Study → /[tier]/[project]
│  └─ Read Process Archive → /process-archives/[project]
│
└─ Footer
```

---

## Implementation Checklist

### Week 2 Implementation Tasks

**Files to Create:**
- [ ] `_includes/footer.html` (footer component)
- [ ] `assets/css/_footer.scss` (footer styling)

**Files to Modify:**
- [ ] `_layouts/default.html` (add footer include)
- [ ] `assets/css/main.scss` (import footer styles)
- [ ] All case study layout files (add sidebar widgets)

**Files to NOT Modify:**
- [ ] `_includes/sidebar-nav.html` (no changes)
- [ ] `_data/navigation.json` (no changes to structure, Layer 1 unchanged)

---

## User Testing Considerations

### Test Scenarios

**Scenario 1: New visitor**
- Lands on homepage
- Reads manifesto
- Clicks case study
- Does user notice "How This Was Built" widget?
- Does user find timelines?

**Scenario 2: Returning visitor with research interest**
- Lands on case study they previously read
- Wants to see decision-making
- Finds process archive via widget
- Success if click-through rate is high

**Scenario 3: Specialist researcher**
- Wants deep timeline research
- Finds footer link or case study widget
- Navigates to timeline
- Success if timeline is discoverable

### Metrics to Track
- Click-through rates on Layer 2/3 links
- Bounce rates on process archive pages
- Time spent on timelines
- User feedback on navigation clarity

---

## Success Criteria - Navigation

✓ Sidebar completely unchanged (no breaking changes to Layer 1)
✓ Layer 2 (Process Archives) discoverable via footer on every page
✓ Layer 3 (Timelines) discoverable via footer on every page
✓ Case studies have direct widgets to both layers
✓ Mobile responsive and accessible
✓ All links working (no 404s)
✓ Footer subtle but visible (proper visual hierarchy)
✓ Keyboard navigation functional
✓ Screen reader friendly
✓ No JavaScript required for core navigation

---

## Visual Mockup Examples

### Desktop Mockup (1200px+)

```
┌──────────────────────────────────────────────────────────────────────────┐
│                          PETERSALVATO.COM                                │
├────────────────────┬─────────────────────────────────────────────────────┤
│                    │                                                     │
│  01. PROTOCOLS     │  SAVEPOINT PROTOCOL                                 │
│  ├─ Savepoint      │                                                     │
│  ├─ Aetherwright   │  [Main article content]                             │
│  ├─ AI DevOps      │                                                     │
│  ├─ Portable       │  [Article continues...]                             │
│                    │                                                     │
│  02. APPLIED SYS.  │  ┌─────────────────────────────────────────────┐   │
│  ├─ Encore         │  │ HOW THIS WAS BUILT                          │   │
│  ├─ Aiden-Jae      │  │                                             │   │
│  ├─ Everyday Gold  │  │ The decisions and constraints behind        │   │
│  ├─ Altrueism      │  │ Savepoint Protocol.                         │   │
│  ├─ Modernist      │  │                                             │   │
│                    │  │ [→ Read Process Archive]                    │   │
│  03. PRACTICE      │  └─────────────────────────────────────────────┘   │
│  ├─ New City       │                                                     │
│  ├─ MathOnTape     │  ┌─────────────────────────────────────────────┐   │
│  ├─ Photo          │  │ FULL CONVERSATION TIMELINE                  │   │
│  ├─ Deep Cuts      │  │                                             │   │
│  ├─ Echo & Bone    │  │ 487 entries documenting research,           │   │
│  ├─ Versagrams     │  │ ideation, and iteration.                    │   │
│  ├─ Crypto         │  │                                             │   │
│  ├─ Motor          │  │ [→ Explore Timeline]                        │   │
│  ├─ Sentiment      │  └─────────────────────────────────────────────┘   │
│  └─ Monstrum       │                                                     │
│                    │                                                     │
│  ABOUT             │  [Related content...]                               │
│  ├─ How I Think    │                                                     │
│  ├─ Provenance     │                                                     │
│  └─ Colophon       │                                                     │
│                    │                                                     │
└────────────────────┴─────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│ PROCESS ARCHIVES              │  TIMELINES                                 │
│ How work gets built: decisions,│  8,922+ entries of research and thinking  │
│ constraints, what failed.      │  across 20 projects                       │
│ [→ Browse All]                │  [→ Master Timeline]                       │
│                                │                                            │
├────────────────────────────────────────────────────────────────────────────┤
│ Provenance  |  How I Think  |  Colophon                                    │
└────────────────────────────────────────────────────────────────────────────┘
```

### Mobile Mockup (375px)

```
┌──────────────────────────────┐
│  ☰  PETERSALVATO.COM         │
├──────────────────────────────┤
│                              │
│  SAVEPOINT PROTOCOL          │
│                              │
│  [Main article content...]   │
│                              │
│  ┌──────────────────────────┐│
│  │ HOW THIS WAS BUILT       ││
│  │                          ││
│  │ Read the Process         ││
│  │ Archive                  ││
│  │ [→]                      ││
│  └──────────────────────────┘│
│                              │
│  ┌──────────────────────────┐│
│  │ FULL CONVERSATION        ││
│  │ TIMELINE                 ││
│  │                          ││
│  │ 487 entries of research  ││
│  │ [→ Explore]              ││
│  └──────────────────────────┘│
│                              │
│  [Related content...]        │
│                              │
├──────────────────────────────┤
│ PROCESS ARCHIVES             │
│ How work gets built          │
│ [→ Browse All]               │
│                              │
│ TIMELINES                    │
│ Deep Research                │
│ [→ Master Timeline]          │
│                              │
├──────────────────────────────┤
│ Provenance                   │
│ How I Think                  │
│ Colophon                     │
└──────────────────────────────┘
```

---

## Next Steps

1. **Task 2.4 Complete:** Navigation plan documented
2. **Week 2:** Implement footer component
3. **Week 2:** Add sidebar widgets to case study layouts
4. **Week 3:** Test navigation across devices
5. **Week 3:** Verify all links functional

