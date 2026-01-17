# Task 2 Code Quality Fixes Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Resolve 7 code quality issues in the sidebar component to meet production deployment standards.

**Architecture:** Fix accessibility (ARIA labels), design system consistency (font variables), code cleanup (redundant rules), and responsive design strategy (nested media queries). All changes maintain visual consistency and improve maintainability without breaking existing functionality.

**Tech Stack:** Jekyll site, SCSS with variables/mixins, HTML5, CSS3 media queries.

---

## Task 1: Add ARIA Labels to Sidebar HTML

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/_includes/sidebar-nav.html:1-6`

**Step 1: Add aria-label to aside element**

Replace line 1:
```html
<aside class="sidebar-nav">
```

With:
```html
<aside class="sidebar-nav" aria-label="Main site navigation">
```

**Step 2: Add aria-label to nav element**

Replace line 6:
```html
  <nav class="sidebar-menu">
```

With:
```html
  <nav class="sidebar-menu" aria-label="Site sections">
```

**Step 3: Verify changes**

Run:
```bash
grep -n "aria-label" /home/peter/homelab/projects/active/petersalvato.com/_includes/sidebar-nav.html
```

Expected: Should show 2 matches with aria-label attributes on lines 1 and 6.

---

## Task 2: Add Sidebar Font Size Variables to SCSS

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/assets/css/_variables.scss:26-27`

**Step 1: Add sidebar font size variables**

After line 26 (`$font-size-4xl: 48px;`), add these three lines:

```scss
// Sidebar-specific font sizes
$font-size-sidebar-base: 12px;
$font-size-sidebar-title: 14px;
$font-size-sidebar-link: 11px;
```

**Step 2: Verify additions**

Run:
```bash
grep "font-size-sidebar" /home/peter/homelab/projects/active/petersalvato.com/assets/css/_variables.scss
```

Expected: Should show 3 new variables defined.

---

## Task 3: Replace Hardcoded Font Sizes in style.scss

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss:120`, `147`, `201`

**Step 1: Replace font-size on line 120**

Find: `font-size: 12px;` (in `.sidebar-nav` selector)

Replace with: `font-size: $font-size-sidebar-base;`

**Step 2: Replace font-size on line 147**

Find: `font-size: 14px;` (in `.sidebar-title` selector)

Replace with: `font-size: $font-size-sidebar-title;`

**Step 3: Replace font-size on line 201**

Find: `font-size: 11px;` (in `.nav-list li a` selector)

Replace with: `font-size: $font-size-sidebar-link;`

**Step 4: Verify replacements**

Run:
```bash
grep -n "font-size:" /home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss | grep -E "(12px|14px|11px)"
```

Expected: No matches (all hardcoded font sizes converted to variables).

---

## Task 4: Remove Redundant Media Query Rules in Sidebar

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss:107-138`

**Step 1: Replace the entire .sidebar-nav block**

Replace lines 107-138 with:

```scss
// ===== SIDEBAR NAVIGATION =====

.sidebar-nav {
  position: fixed;
  left: 0;
  top: 0;
  width: $sidebar-width;
  height: 100vh;
  background-color: $color-white;
  border-right: 1px solid $color-border;
  padding: $space-xl $space-md;
  overflow-y: auto;
  font-family: $font-mono;
  font-size: $font-size-sidebar-base;
  text-transform: uppercase;
  letter-spacing: 0.5px;

  @include grain-texture;

  @media (max-width: $bp-tablet) {
    display: none;
    width: 250px;
    z-index: 999;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);

    &.active {
      display: block;
    }

    @media (max-width: $bp-mobile) {
      width: 100%;
      max-width: 300px;
    }
  }
}
```

**Step 2: Verify structure**

Run:
```bash
sed -n '107,150p' /home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss
```

Expected: Should show cleaned up block without redundant `position: fixed` and `background` in media query. Nested mobile media query should be present.

---

## Task 5: Add Comment Documenting Hover Color Strategy

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss:197-213`

**Step 1: Add explanatory comment**

Find the `.nav-list li a` block and add comment before `&:hover`:

Replace lines 209-211:
```scss
    &:hover {
      color: $color-creative;
    }
```

With:
```scss
    // Unified hover color for all nav links (creative accent)
    // This creates visual cohesion across domain sections
    &:hover {
      color: $color-creative;
    }
```

**Step 2: Verify comment**

Run:
```bash
sed -n '209,212p' /home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss
```

Expected: Should show the comment lines before the `:hover` rule.

---

## Task 6: Remove Fragile Content-Wrapper Grid Positioning

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss:215-222`

**Step 1: Delete the fragile .content-wrapper rules**

Delete lines 215-222 (the entire `.content-wrapper` grid-column block that references `grid-column: 2`).

These lines should be removed:
```scss
// Update .content-wrapper positioning for sidebar
.content-wrapper {
  grid-column: 2;

  @media (max-width: $bp-tablet) {
    grid-column: 1;
  }
}
```

**Step 2: Verify deletion**

Run:
```bash
grep -n "grid-column: 2" /home/peter/homelab/projects/active/petersalvato.com/assets/css/style.scss
```

Expected: No matches (rule completely removed).

---

## Task 7: Test Build with Jekyll and Verify Sidebar Rendering

**Files:**
- Test: `/home/peter/homelab/projects/active/petersalvato.com/` (entire Jekyll site)

**Step 1: Start Jekyll development server**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com && jekyll serve
```

Expected: Server starts without SCSS compilation errors. Output shows something like:
```
Configuration file: /home/peter/homelab/projects/active/petersalvato.com/_config.yml
            Source: /home/peter/homelab/projects/active/petersalvato.com
       Destination: /home/peter/homelab/projects/active/petersalvato.com/_site
 Incremental build: enabled
      Generating...
       Jekyll Feed: Generating feed for posts
                    done in X.XXX seconds.
 Auto-regeneration: enabled for '/home/peter/homelab/projects/active/petersalvato.com'
    Server address: http://127.0.0.1:4000/
  Server running...
Press Ctrl-C to quit.
```

**Step 2: Verify no SCSS errors**

Inspect console output for any errors like:
- `Sass::SyntaxError`
- `Undefined variable`
- `Invalid CSS`

Expected: No errors in compilation.

**Step 3: Access local site in browser**

Visit: `http://localhost:4000/` and inspect:
- Sidebar displays correctly with no font size issues
- Sidebar positioning is fixed on desktop
- Sidebar is hidden on tablet/mobile viewports
- No layout shifts or grid misalignments

**Step 4: Verify responsive behavior**

Open browser DevTools and test breakpoints:
- At 1024px+: Sidebar visible, fixed left position
- At 768px-1023px: Sidebar hidden by default
- At 480px-767px: When active, sidebar mobile width applied

Expected: All breakpoints render correctly without visual bugs.

**Step 5: Stop Jekyll server**

Press `Ctrl-C` to stop the development server.

---

## Task 8: Commit Changes

**Files:**
- Modified: `_includes/sidebar-nav.html`
- Modified: `assets/css/_variables.scss`
- Modified: `assets/css/style.scss`

**Step 1: Stage all modified files**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com && git add _includes/sidebar-nav.html assets/css/_variables.scss assets/css/style.scss
```

**Step 2: Verify staging**

Run:
```bash
git status
```

Expected: Shows 3 files staged for commit.

**Step 3: Create commit**

Run:
```bash
git commit -m "fix: resolve Task 2 code quality issues - ARIA labels, font variables, responsive strategy"
```

Expected: Commit succeeds with message showing 3 files changed, with insertions and deletions.

**Step 4: Verify commit**

Run:
```bash
git log -1 --stat
```

Expected: Shows latest commit with the fix message and file changes listed.

---

## Summary

This plan systematically addresses all 7 code quality issues:

1. **ISSUE #1** - ARIA labels added to sidebar HTML elements
2. **ISSUE #3** - Sidebar font size variables created and hardcoded values replaced
3. **ISSUE #4** - Redundant media query rules cleaned up, nested mobile query added
4. **ISSUE #5** - Comment added documenting hover color strategy
5. **ISSUE #6** - Responsive strategy completed (addressed in ISSUE #4)
6. **ISSUE #7** - Fragile `.content-wrapper` grid positioning removed

All changes maintain visual consistency, improve code maintainability, and prepare the sidebar component for production deployment.
