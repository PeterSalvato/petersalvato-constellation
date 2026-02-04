# Responsive Design Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make petersalvato.com responsive across mobile, tablet, and desktop using modern CSS patterns (clamp, mobile-first, details/summary).

**Architecture:** Mobile-first CSS with three breakpoints: mobile (< 600px, hamburger menu via `<details>`), vertical tablet (600-900px, sidebar narrows), horizontal tablet+ (900px+, full layout). Typography uses CSS `clamp()` for fluid scaling. Sidebar auto-closes on link click.

**Tech Stack:** Jekyll 4.4.1, SCSS (native compilation), HTML `<details>/<summary>`, CSS `clamp()`, CSS Grid

---

## Task 1: Update default.html Layout with Details/Summary Hamburger

**Files:**
- Modify: `_layouts/default.html` (entire structure)

**Step 1: Read current default.html to understand structure**

Run: `head -50 _layouts/default.html`

Expected: See current sidebar and main-content structure

**Step 2: Add details/summary hamburger before sidebar**

Replace the opening structure with semantic details/summary toggle. The checkbox becomes a `<details>` element, hamburger label becomes `<summary>`, and sidebar gets a close button inside.

```html
<body>
  <!-- Details toggle for mobile hamburger menu -->
  <details id="sidebar-toggle" class="sidebar-toggle">
    <summary class="hamburger-icon" aria-label="Toggle navigation">
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </summary>

    <!-- Sidebar Navigation -->
    <aside id="sidebar-nav" aria-label="Main site navigation">
      <!-- existing sidebar content here -->
    </aside>
  </details>

  <!-- Main Content -->
  <main id="main-content">
    <!-- existing content -->
  </main>

  <!-- Footer -->
  <footer>
    <!-- existing footer -->
  </footer>
</body>
```

**Step 3: Verify the HTML is valid**

Run: `bundle exec jekyll build 2>&1 | tail -3`

Expected: `done in X seconds` (no errors)

**Step 4: Check built output**

Run: `grep -c "sidebar-toggle" _site/*/index.html | head -5`

Expected: Multiple pages have the hamburger structure

**Step 5: Commit**

```bash
git add _layouts/default.html
git commit -m "refactor: replace sidebar with details/summary hamburger menu

- Use semantic HTML <details>/<summary> instead of checkbox hack
- Hamburger icon visible on mobile only (CSS controlled)
- Sidebar wraps in details for native browser toggle
- Auto-closes on navigation (details closes when link clicked)

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Restructure main.scss to Mobile-First Architecture

**Files:**
- Modify: `assets/css/main.scss` (major restructuring)

**Step 1: Read current scss to identify sections**

Run: `grep -n "^//" assets/css/main.scss | head -20`

Expected: See section headers and current organization

**Step 2: Reorganize main.scss with mobile-first structure**

The file should follow this structure:
1. Variables & utilities (unchanged)
2. Base styles (mobile-first, no media queries)
3. `@media (min-width: 600px)` - vertical tablet adjustments
4. `@media (min-width: 900px)` - horizontal tablet+ adjustments

Move all current desktop styles to `@media (min-width: 900px)` block. Keep mobile styles outside media queries.

**Step 3: Identify current `@media` statements to migrate**

Run: `grep -n "@media" assets/css/main.scss`

Expected: See all existing media queries (currently 768px and 1024px breakpoints)

**Step 4: Delete old media query breakpoints**

Remove/comment out all `@media (max-width: 768px)` and `@media (max-width: 1024px)` blocks. We'll rebuild them mobile-first.

**Step 5: Commit reorganization checkpoint**

```bash
git add assets/css/main.scss
git commit -m "refactor: prepare main.scss for mobile-first restructuring

- Identify all media query blocks for migration
- Mark old breakpoints (768px, 1024px) for removal
- Structure: base mobile → 600px tablet → 900px desktop

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Implement CSS Clamp for Fluid Typography

**Files:**
- Modify: `assets/css/main.scss` (typography section)

**Step 1: Find typography section in scss**

Run: `grep -n "^h1\|^body\|^font-size" assets/css/main.scss | head -10`

Expected: See current font-size declarations

**Step 2: Replace fixed font-sizes with clamp()**

Update these rules with fluid typography:

```scss
// Base font
body {
  font-size: clamp(0.9rem, 1vw + 0.5rem, 1rem);
  line-height: 1.6;
}

// Headings
h1 {
  font-size: clamp(1.1rem, 5vw, 1.3rem);
  line-height: 1.1;
}

h2 {
  font-size: clamp(1rem, 4vw, 1.2rem);
  line-height: 1.2;
}

h3 {
  font-size: clamp(0.95rem, 3vw, 1.1rem);
  line-height: 1.3;
}
```

**Step 3: Build and test typography in browser**

Run: `bundle exec jekyll serve`

Open: `http://localhost:4000/petersalvato-constellation/`

Resize browser from 320px to 1400px. Typography should scale smoothly without jarring jumps.

**Step 4: Test at 200% zoom (WCAG accessibility)**

In browser DevTools: Ctrl+0, then Ctrl++ multiple times to 200%

Expected: Text remains readable, no overflow, no layout break

**Step 5: Commit**

```bash
git add assets/css/main.scss
git commit -m "feat: implement fluid typography with CSS clamp()

- h1: clamp(1.1rem, 5vw, 1.3rem)
- h2: clamp(1rem, 4vw, 1.2rem)
- h3: clamp(0.95rem, 3vw, 1.1rem)
- body: clamp(0.9rem, 1vw + 0.5rem, 1rem)

Maintains accessibility (respects user zoom up to 200%)
Eliminates media query breakpoints for typography
Responsive from mobile to widescreen

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Add Mobile Hamburger Menu Styling (CSS Only)

**Files:**
- Modify: `assets/css/main.scss` (new mobile section)

**Step 1: Add hamburger icon styles for mobile only**

In the RESPONSIVE section of main.scss, add:

```scss
// ============================================================================
// MOBILE HAMBURGER MENU (< 600px)
// ============================================================================

@media (max-width: 600px) {
  // Hide sidebar by default on mobile
  #sidebar-nav {
    position: fixed;
    left: -250px;
    top: 0;
    width: 250px;
    height: 100vh;
    transition: left 0.3s ease;
    z-index: 1000;
    background-color: #fff;
    border-right: 1px solid #e5e5e0;
  }

  // Show sidebar when details is open
  #sidebar-toggle[open] #sidebar-nav {
    left: 0;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }

  // Hamburger icon visible only on mobile
  .hamburger-icon {
    display: flex;
    flex-direction: column;
    gap: 4px;
    padding: 16px;
    cursor: pointer;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1001;
    background: white;
    border-bottom: 1px solid #e5e5e0;
    width: 100%;
  }

  .hamburger-line {
    width: 24px;
    height: 2px;
    background-color: #1a1a1a;
    transition: all 0.3s ease;
  }

  // Overlay backdrop when menu is open
  #sidebar-toggle[open]::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999;
  }

  // Main content adjusts on mobile
  #main-content {
    padding: 40px 20px;
    padding-top: 70px; // Space for hamburger
  }
}
```

**Step 2: Build and verify hamburger appears**

Run: `bundle exec jekyll build`

Run: `grep -c "hamburger-icon" _site/*/index.html | head -1`

Expected: Hamburger appears in built HTML

**Step 3: Test hamburger visually**

Run: `bundle exec jekyll serve`

Open browser: `http://localhost:4000/petersalvato-constellation/`

Resize to < 600px (mobile). Verify hamburger icon appears.

**Step 4: Test menu open/close**

In browser DevTools mobile view: Click hamburger → sidebar should slide in
Click sidebar link → sidebar should close (this is automatic with `<details>`)

**Step 5: Commit**

```bash
git add assets/css/main.scss
git commit -m "feat: add mobile hamburger menu styling

- Sidebar hidden off-screen by default on mobile (< 600px)
- Hamburger icon fixed position in header
- Slides sidebar in from left when open
- Dark overlay backdrop shows when menu active
- Auto-closes when user clicks a link (<details> native behavior)

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Implement Vertical Tablet Breakpoint (600-900px)

**Files:**
- Modify: `assets/css/main.scss` (add 600px media query)

**Step 1: Add tablet vertical breakpoint styles**

```scss
// ============================================================================
// VERTICAL TABLET (600px - 900px)
// ============================================================================

@media (min-width: 600px) and (max-width: 900px) {
  // Sidebar narrows but stays visible
  #sidebar-nav {
    width: 200px; // narrower than 250px
    padding: 24px 16px;
  }

  #main-content {
    padding: 40px 40px;
    padding-left: calc(200px + 2rem); // adjust for narrower sidebar
  }

  #sidebar-title {
    font-size: 1rem; // smaller title
  }

  .nav-list a {
    font-size: 10px; // slightly smaller nav text
  }

  // Specs sidebars stack to single column
  .protocol-specs,
  .system-specs {
    grid-template-columns: 1fr;
  }

  // Route cards stay single column (wait for 900px to go multi-column)
  #route-cards {
    grid-template-columns: 1fr;
  }

  // Hamburger icon hidden (sidebar is visible)
  .hamburger-icon {
    display: none;
  }
}
```

**Step 2: Build and verify tablet layout**

Run: `bundle exec jekyll build`

**Step 3: Test in browser at tablet size**

Run: `bundle exec jekyll serve`

Open browser DevTools, set width to 750px (vertical tablet)

Expected: Sidebar visible but narrower, main content adjusted, no hamburger icon

**Step 4: Verify no text wrapping in narrower sidebar**

Check nav links in sidebar: should not wrap to multiple lines

If wrapping occurs, reduce font-size further or narrow text

**Step 5: Commit**

```bash
git add assets/css/main.scss
git commit -m "feat: add vertical tablet breakpoint (600-900px)

- Sidebar narrows to 200px but stays visible
- Main content padding adjusts
- Navigation text scales smaller
- Specs sidebars stack to single column
- Route cards remain single column
- Hamburger icon hidden (sidebar visible)

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Implement Horizontal Tablet+ Breakpoint (900px+)

**Files:**
- Modify: `assets/css/main.scss` (add 900px media query)

**Step 1: Add desktop-and-up styles**

```scss
// ============================================================================
// HORIZONTAL TABLET / DESKTOP (900px+)
// ============================================================================

@media (min-width: 900px) {
  // Sidebar returns to full width and padding
  #sidebar-nav {
    width: 250px;
    padding: 32px 24px;
  }

  #main-content {
    padding: 64px 64px;
    padding-left: calc(250px + 2rem);
  }

  #sidebar-title {
    font-size: 1.25rem; // full size
  }

  .nav-list a {
    font-size: 11px; // full size
  }

  // Specs sidebars return to two-column grid
  .protocol-specs,
  .system-specs {
    grid-template-columns: repeat(2, 1fr);
  }

  // Route cards return to 3-column grid
  #route-cards {
    grid-template-columns: repeat(3, 1fr);
  }

  // Gallery grids expand
  .artifact-gallery {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }
}
```

**Step 2: Build and verify desktop layout**

Run: `bundle exec jekyll build`

**Step 3: Test at multiple desktop sizes**

Run: `bundle exec jekyll serve`

Open browser at:
- 1024px (small desktop) - should look good
- 1200px (standard desktop) - should look good
- 1400px (large desktop) - should look good

Expected: Full spacing restored, sidebar 250px, route cards 3-column, etc.

**Step 4: Test responsive flow**

Resize browser from 300px → 1500px smoothly

Expected: Breakpoints transition smoothly at 600px and 900px boundaries

**Step 5: Commit**

```bash
git add assets/css/main.scss
git commit -m "feat: add desktop breakpoint (900px+)

- Sidebar returns to 250px width and full padding
- Main content full 64px padding on both sides
- Specs sidebars display 2-column grid
- Route cards display 3-column grid
- Gallery grids expand with auto-fit

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 7: Remove Old Media Queries and Clean Up SCSS

**Files:**
- Modify: `assets/css/main.scss` (cleanup)

**Step 1: Find and remove old media queries**

Run: `grep -n "@media (max-width:" assets/css/main.scss`

Expected: See old 768px and 1024px breakpoints

**Step 2: Delete old @media blocks**

Remove all:
- `@media (max-width: 768px)`
- `@media (max-width: 1024px)`
- `@media (max-width: 512px)`

Keep only the new mobile-first structure:
- No media query (mobile base)
- `@media (min-width: 600px)` (tablet)
- `@media (min-width: 900px)` (desktop)

**Step 3: Verify no duplicate media queries**

Run: `grep "@media" assets/css/main.scss`

Expected: Only three blocks (600px, 900px, and maybe one for print if exists)

**Step 4: Build and test full responsive flow**

Run: `bundle exec jekyll build 2>&1 | tail -3`

Expected: `done in X seconds` (no errors)

**Step 5: Verify site still works at all breakpoints**

Run: `bundle exec jekyll serve`

Test at: 400px (mobile), 700px (tablet), 1000px (desktop)

Expected: All breakpoints work correctly

**Step 6: Commit**

```bash
git add assets/css/main.scss
git commit -m "refactor: remove old media queries, clean up SCSS

- Delete old max-width: 768px and 1024px breakpoints
- Keep only modern mobile-first structure
- Verify no duplicate or conflicting rules
- Confirm all breakpoints (600px, 900px) working

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 8: Test Accessibility & Final Verification

**Files:**
- No code changes (testing only)

**Step 1: Test at 200% zoom**

Run: `bundle exec jekyll serve`

Open browser: `http://localhost:4000/petersalvato-constellation/`

Press: `Ctrl+0` then `Ctrl++` multiple times to reach 200% zoom

Expected: 
- Text readable, no overflow
- Layout doesn't break
- Hamburger menu still accessible
- Navigation still works

**Step 2: Test keyboard navigation**

Press: `Tab` repeatedly through page

Expected: 
- Hamburger icon focusable
- Sidebar links focusable
- All interactive elements reachable
- Focus indicators visible

**Step 3: Test touch targets on mobile**

In DevTools mobile view (< 600px):
- Hamburger icon tappable (should be 24x24px minimum, ideally 44x44px)
- Sidebar links tappable
- All buttons/links easily tappable (48px+ recommended)

**Step 4: Test on actual mobile device (if available)**

Use phone or tablet browser:
- Load site at `http://[your-ip]:4000/petersalvato-constellation/`
- Test hamburger menu opens/closes
- Navigate through pages
- Test landscape/portrait orientation
- Verify touch interactions work

**Step 5: Final build for deployment**

Run: `bundle exec jekyll build`

Verify: `ls -lh _site/assets/css/main.css`

Expected: CSS file exists and has reasonable size (shouldn't be huge)

**Step 6: Commit (if any tweaks were needed)**

```bash
git add -A
git commit -m "test: verify responsive design accessibility and functionality

- Tested at 200% zoom (WCAG 1.4.4 compliant)
- Keyboard navigation verified
- Mobile touch targets adequate
- All breakpoints (mobile, tablet, desktop) confirmed working

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 9: Deploy and Final Review

**Files:**
- No code changes (deployment only)

**Step 1: Push to GitHub**

```bash
git push origin main
```

Expected: All commits pushed successfully

**Step 2: Wait for GitHub Pages build**

GitHub Actions will build automatically. Wait ~30 seconds.

**Step 3: Test on live site**

Open: `https://petersalvato.github.io/petersalvato-constellation/`

Test at mobile, tablet, desktop sizes:
- Hamburger menu works
- Sidebar narrows on tablet
- Layout expands on desktop
- Typography scales smoothly

**Step 4: Final verification checklist**

- [ ] Mobile (< 600px): Hamburger menu visible, auto-closes on link click
- [ ] Vertical tablet (600-900px): Sidebar visible and narrow, no text wrapping
- [ ] Horizontal tablet+ (900px+): Full layout with 250px sidebar
- [ ] Typography scales with clamp() (no jarring jumps)
- [ ] 200% zoom accessibility test passes
- [ ] All three route cards visible on desktop, stacked on mobile
- [ ] Footer responsive on all sizes
- [ ] Case study layouts responsive

**Step 5: Commit final status**

```bash
git add -A
git commit -m "deploy: responsive design complete and live

Responsive breakpoints:
- Mobile (< 600px): Hamburger menu, hamburger auto-closes
- Tablet (600-900px): Sidebar visible, narrowed
- Desktop (900px+): Full layout

Typography: Fluid scaling with CSS clamp()
Navigation: Semantic <details>/<summary> hamburger
Architecture: Mobile-first CSS organization

All sizes tested. Ready for image integration.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Summary

**9 tasks, all focused on incremental, testable changes:**

1. Update HTML with `<details>/<summary>` hamburger
2. Reorganize SCSS for mobile-first architecture
3. Implement CSS `clamp()` for typography
4. Add mobile hamburger styling
5. Add tablet (600-900px) breakpoint
6. Add desktop (900px+) breakpoint
7. Remove old media queries
8. Test accessibility and responsiveness
9. Deploy and verify

**Commit frequency:** One commit per task
**Testing:** Visual testing at each breakpoint
**Modern patterns:** `<details>`, `clamp()`, mobile-first CSS, no heavy JavaScript

