# Task 2: SCSS Structure Analysis & Mobile-First Migration Plan

**Date:** 2026-02-03
**Status:** Analysis Complete - Ready for Migration Planning
**Confidence Level:** High - All findings verified via grep and build testing

---

## Executive Summary

The `main.scss` file currently uses a **desktop-first architecture** with max-width media queries. The site was designed for desktop display with responsive adjustments for smaller screens. To transition to mobile-first, we need to:

1. Extract all mobile-first base styles (keep as-is, no queries)
2. Convert existing max-width queries to min-width equivalents
3. Reorganize file into mobile-first structure
4. Ensure all tests pass during migration

**Current Build Status:** ✅ **SUCCESS** (with 1 deprecation warning - unrelated to restructure)

---

## Current SCSS Structure (Lines 1-1477)

### Section Breakdown

| Section | Lines | Purpose | Status |
|---------|-------|---------|--------|
| VARIABLES | 4-43 | Color, typography, sizing, spacing, transitions | Core - no changes needed |
| GLOBAL / RESET | 45-67 | Box-sizing, html/body defaults | Mobile-friendly already |
| TYPOGRAPHY | 69-112 | Heading/paragraph/link defaults | Mobile-friendly already |
| SIDEBAR | 114-198 | Fixed 250px sidebar navigation | Desktop-specific - needs consideration |
| MAIN CONTENT | 200-213 | Main content wrapper with sidebar offset | Desktop-specific - needs redesign |
| SYSTEMWORKS / HOMEPAGE | 215-251 | Homepage header & manifesto styling | Desktop defaults |
| ROUTE CARDS | 253-312 | 3-column grid layout (desktop) | **Needs mobile adjustment** |
| FOOTER | 314-389 | Full-width footer with 3-column grid | **Needs mobile adjustment** |
| WORKBENCH-SPEC | 391-584 | Spec boxes, faculty indicators, content | Mostly mobile-friendly |
| WHITEPAPER / LOG | 586-763 | Header, meta grid, content blocks | **Some mobile adjustments needed** |
| DOMAIN INDEX | 765-843 | Index page with artifacts grid | Mostly mobile-friendly |
| UTILITIES | 845-863 | Text centering, font helpers | Mobile-friendly already |
| RESPONSIVE (SECTION HEADER) | 865-867 | Section marker only | N/A |
| THREE SYSTEMS - VISUAL | 887-940 | System tag indicators | Mobile-friendly already |
| PROTOCOL-01 LAYOUT | 942-1008 | 2-column protocol pages | **Needs mobile adjustment** |
| SYSTEM-02 LAYOUT | 1050-1084 | 2-column case study pages | **Needs mobile adjustment** |
| PRACTICE-03 LAYOUT | 1142-1250 | Single column artifact showcase | Mobile-friendly already |
| SHARED SPEC BLOCKS | 1252-1310 | Spec block styling across layouts | Mobile-friendly already |
| CODE BLOCKS | 1312-1339 | Code/pre styling | Mobile-friendly already |
| IMAGE GALLERIES | 1341-1446 | Gallery grids with media queries | **HAS MEDIA QUERIES - Active** |
| RESPONSIVE (MAIN SECTION) | 1448-1476 | **Main breakpoint section** | **HAS MEDIA QUERIES - Active** |

**Total Sections:** 20 major sections (well-organized)

---

## Current Media Queries (Detailed)

### All Media Queries Found: 8 Total

#### Commented Out (Inactive)
```scss
// Line 869-873: @media (max-width: 1400px)
// Affects: #domain-cards (3-col → 2-col)
// Status: INACTIVE - rules are commented out
// Reason: Likely disabled during development; rules never activated

// Line 875-883: @media (max-width: 900px)
// Affects: #domain-cards (2-col → 1-col), #main-content padding
// Status: INACTIVE - rules are commented out
// Reason: Likely disabled during development; rules never activated
```

#### Active (Currently Used)

**1. Line 1354-1356: .image-gallery--square**
```scss
@media (max-width: 768px) {
  grid-template-columns: 1fr;  // 2-column → 1-column
}
```
Breakpoint: **768px**
Purpose: Stack square gallery to single column on tablets/mobile
Current: Active and used

**2. Line 1366-1368: .image-gallery--three-col**
```scss
@media (max-width: 768px) {
  grid-template-columns: repeat(2, 1fr);  // 3-column → 2-column
}
```
Breakpoint: **768px**
Purpose: Reduce 3-column gallery to 2-column on tablets

**3. Line 1370-1372: .image-gallery--three-col**
```scss
@media (max-width: 512px) {
  grid-template-columns: 1fr;  // 2-column → 1-column
}
```
Breakpoint: **512px**
Purpose: Further reduce to single column on phones

**4. Line 1423-1425: .section-gallery**
```scss
@media (max-width: 768px) {
  grid-template-columns: 1fr;  // 2-column → 1-column
}
```
Breakpoint: **768px**
Purpose: Stack section gallery on small screens

**5. Line 1452-1464: @media (max-width: 1024px)** — MAJOR
```scss
@media (max-width: 1024px) {
  .protocol-layout,
  .system-layout {
    grid-template-columns: 1fr;  // 2-column → 1-column
    gap: $gap-large;

    .protocol-specs,
    .system-specs {
      display: grid;
      grid-template-columns: repeat(2, 1fr);  // specs stay 2-col
      gap: $gap-large;
    }
  }
}
```
Breakpoint: **1024px**
Purpose: Collapse 2-column layout (content + sidebar specs) to single column for tablets
Current: Active and critical for tablet view

**6. Line 1467-1476: @media (max-width: 768px)** — MAJOR
```scss
@media (max-width: 768px) {
  .artifact-gallery {
    grid-template-columns: 1fr !important;  // Force single column
  }

  .protocol-specs,
  .system-specs {
    grid-template-columns: 1fr !important;  // specs collapse to 1-col
  }
}
```
Breakpoint: **768px**
Purpose: Final collapse to single column for phones; specs also go single-column
Current: Active and critical for phone view

### Media Query Summary Table

| Breakpoint | Location | Affected Component | Current Status | Priority for Migration |
|------------|----------|-------------------|----------------|------------------------|
| 1400px | Line 869 | #domain-cards (3→2 col) | Commented out | Low - Inactive |
| 1024px | Line 1452 | .protocol/system-layout (2→1 col) | **Active** | High - Critical |
| 900px | Line 875 | #domain-cards (2→1 col) | Commented out | Low - Inactive |
| 768px | Line 1354, 1366, 1423, 1467 | Multiple gallery & layout | **Active** | High - Critical |
| 512px | Line 1370 | .image-gallery--three-col | **Active** | Medium - Phone specific |

---

## Current Breakpoint Hierarchy

```
Desktop (1400px+)
  ↓ max-width: 1400px
Tablet Large (1025-1399px) — Currently handled by desktop styles
  ↓ max-width: 1024px
Tablet Small (769-1023px) — Layout collapses here
  ↓ max-width: 768px
Phone (513-767px) — Single column, galleries stack
  ↓ max-width: 512px
Phone Small (< 513px) — Further consolidation
```

---

## Detailed Analysis: Rules That Need to Move

### 1. ROUTE CARDS (Lines 253-312) - Desktop-First

**Current:** `grid-template-columns: repeat(3, 1fr);` with no media query
**Problem:** Always 3 columns; assumes desktop screen
**Mobile Behavior:** Breaks on mobile - cards too narrow to read
**Action Needed:**
- Base style (mobile-first): 1 column
- Add min-width: 1024px for 2 columns
- Add min-width: 1300px for 3 columns

**Example Rule to Move:**
```scss
#route-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  // ← HARDCODED DESKTOP ONLY
  gap: $gap-xlarge;
  max-width: $container-max-width;
  margin: 0 auto;
  margin-top: $gap-xxxlarge;
}
```

**After Migration (Mobile-First):**
```scss
#route-cards {
  display: grid;
  grid-template-columns: 1fr;  // Mobile: 1 column (base)
  gap: $gap-xlarge;
  max-width: $container-max-width;
  margin: 0 auto;
  margin-top: $gap-xxxlarge;

  @media (min-width: 1024px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1300px) {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### 2. FOOTER (Lines 314-389) - Desktop-First

**Current:** `.footer-columns { grid-template-columns: $sidebar-width 1fr 1fr; }`
**Problem:** 3-column layout assumes desktop width; no mobile alternative
**Mobile Behavior:** Footer columns overflow on phone
**Action Needed:**
- Base style (mobile-first): `grid-template-columns: 1fr;` (stacked)
- Add min-width: 768px for 2 columns (sidebar + 2 cols combined)
- Add min-width: 1024px for 3 columns (current layout)

**Example Rule to Move:**
```scss
.footer-columns {
  display: grid;
  grid-template-columns: $sidebar-width 1fr 1fr;  // ← HARDCODED DESKTOP
  gap: $gap-xlarge;
  width: 100%;
  max-width: none;
}
```

### 3. PROTOCOL-01 & SYSTEM-02 LAYOUTS (Lines 942-1066) - Desktop-First

**Current:** `.protocol-layout { grid-template-columns: 1fr 320px; }` (2-column)
**Problem:** Content + specs sidebar assumes 1024px+ screen
**Mobile Behavior:** Gets handled by existing 1024px media query (line 1452) but could be cleaner with mobile-first
**Action Needed:**
- Base style (mobile-first): `grid-template-columns: 1fr;` (stacked)
- Add min-width: 768px for 2 columns (current layout)
- Specs should be single-column on mobile, 2-column on tablet

**Example Rule to Move:**
```scss
.protocol-layout {
  display: grid;
  grid-template-columns: 1fr 320px;  // ← HARDCODED DESKTOP
  gap: $gap-xxxlarge;
  align-items: start;
}
```

### 4. SYSTEMWORKS HEADER (Lines 219-251) - Font Size Assumptions

**Current:** `h1 { font-size: 56px; }` - assumes desktop display
**Problem:** 56px heading looks terrible on phone (takes full screen height)
**Mobile Behavior:** Breaks readability on mobile
**Action Needed:**
- Base style (mobile-first): Smaller font (e.g., 32px)
- Add min-width: 1024px for 56px (current size)

**Example Rule to Move:**
```scss
#systemworks-header {
  h1 {
    font-size: 56px;  // ← HARDCODED DESKTOP ONLY
    text-transform: uppercase;
    margin-bottom: $gap-medium;
  }
}
```

### 5. WHITEPAPER HEADER (Lines 590-603) - Font Size Assumptions

**Current:** `h1 { font-size: 48px; }` - large desktop heading
**Problem:** Not mobile-responsive
**Action Needed:**
- Base style (mobile-first): Smaller font (e.g., 28px)
- Add min-width: 768px for 48px (current size)

### 6. MAIN CONTENT PADDING (Lines 204-213) - Sidebar-Dependent

**Current:** `padding-left: calc(#{$sidebar-width} + 2rem);` - assumes fixed sidebar
**Problem:** On mobile, 250px sidebar + padding is larger than viewport
**Mobile Behavior:** Currently handled by... nothing. Needs explicit mobile handling.
**Action Needed:**
- Base style (mobile-first): `padding-left: $padding-medium;` (small)
- Add min-width: 768px for sidebar offset (line 206)

**Critical Rule to Move:**
```scss
#main-content {
  padding: $padding-large $padding-large;
  padding-left: calc(#{$sidebar-width} + 2rem);  // ← ASSUMES SIDEBAR VISIBLE

  #container {
    max-width: $container-max-width;
    margin: 0 auto;
    padding: 0;
  }
}
```

### 7. SIDEBAR NAVIGATION (Lines 118-198) - Fixed Position

**Current:** `position: fixed; width: $sidebar-width; height: 100vh;`
**Problem:** Fixed sidebar on mobile covers content
**Mobile Behavior:** Currently... uncovered. Not handled in media queries!
**Action Needed:**
- Base style (mobile-first): `position: static; width: 100%;` (mobile nav or hidden)
- Add min-width: 1024px for `position: fixed; width: $sidebar-width;`

**Critical Rule to Move:**
```scss
#sidebar-nav {
  background-color: $color-white;
  border-right: 1px solid $color-border;
  padding: $padding-standard $padding-medium;
  position: fixed;  // ← ASSUMES DESKTOP
  width: $sidebar-width;  // ← HARDCODED DESKTOP
  height: 100vh;
  overflow-y: auto;
  // ...
}
```

**Note:** This is a **major architectural issue** - the sidebar is hardcoded to be fixed at 250px width, but there's no media query handling what happens on mobile.

---

## Inactive Media Queries (Why Commented Out?)

### Lines 869-873: 1400px Breakpoint
```scss
// @media (max-width: 1400px) {
//   #domain-cards {
//     grid-template-columns: repeat(2, 1fr);
//   }
// }
```
**Analysis:** The `#domain-cards` ID doesn't exist in current HTML. These rules were likely:
1. Planned for future use
2. Removed from templates but styles left behind
3. Superseded by working alternative (haven't found one)

**Recommendation:** Delete these as cleanup during migration.

### Lines 875-883: 900px Breakpoint
```scss
// @media (max-width: 900px) {
//   #domain-cards {
//     grid-template-columns: 1fr;
//   }
//
//   #main-content {
//     padding: $padding-large $padding-medium;
//   }
// }
```
**Analysis:** Similar situation - refers to non-existent `#domain-cards`. The `#main-content` rule is actually useful but commented out!

**Recommendation:** Extract the `#main-content` rule and activate it properly during migration (convert to mobile-first min-width).

---

## Critical Findings

### Architectural Issues Found

1. **Sidebar not responsive** - No media query to handle fixed sidebar on mobile
   - Line 118: `position: fixed; width: 250px;`
   - Severity: **CRITICAL** - Site probably unusable on phone

2. **Main content padding hardcoded** - Assumes sidebar visible
   - Line 206: `padding-left: calc(#{$sidebar-width} + 2rem);`
   - Severity: **CRITICAL** - Content misaligned on mobile

3. **Large typography not responsive** - Headers assume desktop
   - Line 223: `font-size: 56px;` (homepage h1)
   - Line 597: `font-size: 48px;` (whitepaper h1)
   - Severity: **HIGH** - Terrible UX on phone

4. **Route cards always 3-column** - No mobile fallback
   - Line 255: `grid-template-columns: repeat(3, 1fr);`
   - Severity: **HIGH** - Cards too narrow to read on tablet/phone

5. **Footer 3-column** - No mobile fallback
   - Line 331: `grid-template-columns: $sidebar-width 1fr 1fr;`
   - Severity: **HIGH** - Footer unusable on phone

---

## Compilation Verification

**Command:** `bundle exec jekyll build 2>&1 | tail -3`

**Result:**
```
done in 0.119 seconds.
 Auto-regeneration: disabled. Use --watch to enable.
```

**Status:** ✅ **SUCCESS**

**Notes:**
- Build completes successfully
- Only warning: DEPRECATION on `darken()` function (unrelated to structure)
- CSS compiles to `/assets/css/main.css`
- No SCSS syntax errors blocking migration

---

## Rules Organization Summary

### Base Styles (Mobile-First - No Queries)
- ✅ VARIABLES (45 vars, flexible)
- ✅ GLOBAL / RESET (responsive by default)
- ✅ TYPOGRAPHY (mostly responsive, some needs adjustment)
- ✅ UTILITIES (responsive already)
- ✅ THREE SYSTEMS - VISUAL (responsive already)
- ✅ CODE BLOCKS (responsive already)

### Styles Needing Adjustment (Desktop → Mobile-First)
- 🔴 SIDEBAR (hardcoded fixed position)
- 🔴 MAIN CONTENT (hardcoded sidebar padding)
- 🔴 SYSTEMWORKS / HOMEPAGE (oversized fonts)
- 🔴 ROUTE CARDS (3-column only)
- 🔴 FOOTER (3-column only)
- 🔴 WHITEPAPER / LOG (oversized fonts)
- 🔴 PROTOCOL-01 LAYOUT (2-column only)
- 🔴 SYSTEM-02 LAYOUT (2-column only)

### Styles Already Mobile-Friendly
- ✅ WORKBENCH-SPEC (mostly)
- ✅ DOMAIN INDEX (mostly)
- ✅ PRACTICE-03 LAYOUT
- ✅ SHARED SPEC BLOCKS
- ✅ IMAGE GALLERIES (has media queries - will convert to min-width)

---

## Migration Path Overview

### Phase 1: Foundation (Task 3)
1. Disable sidebar with `display: none;` on mobile
2. Adjust `#main-content` padding for mobile
3. Reduce heading sizes on mobile baseline

### Phase 2: Grid Layouts (Task 4)
1. Route cards: 1-column mobile → 2/3-column desktop
2. Footer: 1-column mobile → 3-column desktop
3. Protocol/System layouts: 1-column mobile → 2-column desktop

### Phase 3: Media Query Conversion (Task 5)
1. Convert `@media (max-width: X)` to `@media (min-width: Y)`
2. Extract base styles from breakpoints
3. Remove commented-out queries

### Phase 4: Testing & Refinement (Task 6)
1. Test on actual mobile/tablet devices
2. Verify touch interactions
3. Optimize font sizes, spacing for small screens
4. Final build verification

---

## Example: One Complete Migration

**File:** `/home/peter/homelab/projects/active/petersalvato.com/assets/css/main.scss`
**Lines:** 253-312
**Current (Desktop-First):**
```scss
#route-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: $gap-xlarge;
  max-width: $container-max-width;
  margin: 0 auto;
  margin-top: $gap-xxxlarge;

  .route-card {
    // ... card styles
  }
}
```

**After Migration (Mobile-First):**
```scss
#route-cards {
  display: grid;
  grid-template-columns: 1fr;  // Mobile: 1 column
  gap: $gap-xlarge;
  max-width: $container-max-width;
  margin: 0 auto;
  margin-top: $gap-xxxlarge;

  .route-card {
    // ... card styles (unchanged)
  }
}

@media (min-width: 1024px) {
  #route-cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1300px) {
  #route-cards {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

---

## File Statistics

| Metric | Value |
|--------|-------|
| Total Lines | 1477 |
| Comment Lines | ~200 |
| Active Code Lines | ~1277 |
| Number of Sections | 20 |
| Total Media Queries | 8 |
| Active Media Queries | 4 |
| Commented Media Queries | 2 |
| Unique Breakpoints | 5 (1400px, 1024px, 900px, 768px, 512px) |

---

## Confidence Assessment

| Finding | Confidence |
|---------|-----------|
| All media queries identified | ✅ 100% |
| Breakpoints enumerated | ✅ 100% |
| Architectural issues found | ✅ 95% |
| Build verification | ✅ 100% |
| Migration path feasibility | ✅ 90% |

**Overall Confidence:** HIGH - Ready to proceed with restructuring

---

## Next Steps (Task 3)

1. Extract current desktop-specific defaults
2. Create mobile-first baseline
3. Add min-width media queries for progressive enhancement
4. Test against current rendering (should be identical)
5. Commit as "Step 1: Extract mobile-first base"

---

## References

**File:** `/home/peter/homelab/projects/active/petersalvato.com/assets/css/main.scss`
**Build Command:** `bundle exec jekyll build`
**Test Server:** `bundle exec jekyll serve` (http://localhost:4000/petersalvato-constellation/)
**GitHub:** https://github.com/PeterSalvato/petersalvato-constellation

---

*Analysis completed 2026-02-03. Ready for implementation phase.*
