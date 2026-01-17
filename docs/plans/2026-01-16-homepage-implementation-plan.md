# petersalvato.com Homepage Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task with frontend-design skill on each task for production-grade aesthetics.

**Goal:** Build a production-grade homepage for petersalvato.com with weathered NASA manual aesthetic, left-fixed sidebar navigation, asymmetrical content layout, and responsive design.

**Architecture:** Jekyll-based static site with SCSS variables for cohesive design system. Left sidebar (200px fixed) anchors navigation with domain-colored sections. Main content uses asymmetrical grid layout. Responsive hamburger menu on mobile. All styling through CSS variables for maintainability.

**Tech Stack:** Jekyll (GitHub Pages), HTML, SCSS, vanilla CSS (no JavaScript for core layout), IBM Plex Sans font family, Courier Prime for monospace elements.

---

## Task 1: SCSS Variable System & Base Styling

**Files:**
- Create: `assets/css/_variables.scss`
- Create: `assets/css/style.scss`
- Modify: `_config.yml` (add font imports)

**Step 1: Create SCSS variables file**

```scss
// assets/css/_variables.scss

// Color Palette
$color-white: #ffffff;
$color-charcoal: #2a2a2a;
$color-text: $color-charcoal;

// Domain Colors (Desaturated RGB)
$color-creative: #b8523a;    // Red - Creative/Evidence
$color-systems: #5a8c6f;     // Green - Systems/Labs
$color-technical: #4a6fa5;   // Blue - Technical/Frontend

// Neutral shades
$color-light-gray: #f9f9f9;
$color-border: #e5e5e5;

// Typography
$font-sans: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
$font-mono: 'Courier Prime', 'Courier New', monospace;

$font-size-base: 16px;
$font-size-lg: 18px;
$font-size-xl: 20px;
$font-size-2xl: 24px;
$font-size-3xl: 32px;
$font-size-4xl: 48px;

$line-height-tight: 1.2;
$line-height-normal: 1.6;
$line-height-relaxed: 1.8;

// Spacing Scale
$space-xs: 4px;
$space-sm: 8px;
$space-md: 16px;
$space-lg: 24px;
$space-xl: 32px;
$space-2xl: 48px;
$space-3xl: 64px;

// Sidebar
$sidebar-width: 200px;

// Breakpoints
$bp-mobile: 480px;
$bp-tablet: 768px;
$bp-desktop: 1024px;

// Transitions
$transition-fast: 150ms ease;
$transition-normal: 300ms ease;
```

**Step 2: Create main SCSS file with grain texture**

```scss
// assets/css/style.scss

@import 'variables';

// Grain texture background (subtle, aged paper effect)
@mixin grain-texture {
  background-image:
    repeating-linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.02) 0px,
      rgba(0, 0, 0, 0.02) 1px,
      transparent 1px,
      transparent 2px
    ),
    repeating-linear-gradient(
      90deg,
      rgba(0, 0, 0, 0.03) 0px,
      rgba(0, 0, 0, 0.03) 1px,
      transparent 1px,
      transparent 2px
    );
}

// Reset & Base Styles
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: $font-size-base;
  scroll-behavior: smooth;
}

body {
  font-family: $font-sans;
  font-size: $font-size-base;
  line-height: $line-height-normal;
  color: $color-text;
  background-color: $color-white;
  @include grain-texture;
}

// Typography Defaults
h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  line-height: $line-height-tight;
  margin-bottom: $space-md;
}

h1 {
  font-size: $font-size-4xl;
}

h2 {
  font-size: $font-size-3xl;
  margin-top: $space-2xl;
}

h3 {
  font-size: $font-size-2xl;
  margin-top: $space-xl;
}

p {
  margin-bottom: $space-md;
}

a {
  color: $color-charcoal;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color $transition-fast;

  &:hover {
    border-bottom-color: $color-charcoal;
  }
}

// Page Layout Grid
.page-layout {
  display: grid;
  grid-template-columns: $sidebar-width 1fr;
  min-height: 100vh;

  @media (max-width: $bp-tablet) {
    grid-template-columns: 1fr;
  }
}

// Main Content Wrapper
.content-wrapper {
  padding: $space-2xl;
  max-width: 900px;
  margin: 0 auto;

  @media (max-width: $bp-tablet) {
    padding: $space-xl;
  }

  @media (max-width: $bp-mobile) {
    padding: $space-lg;
  }
}
```

**Step 3: Update _config.yml to import fonts**

Add to top of `_config.yml`:

```yaml
# Google Fonts Import
google_fonts:
  - IBM Plex Sans:400,700
  - Courier Prime:400
```

**Step 4: Verify compilation**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && jekyll serve`

Expected: Server starts, SCSS compiles to CSS without errors.

**Step 5: Commit**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
git add assets/css/_variables.scss assets/css/style.scss _config.yml
git commit -m "feat: add SCSS variables and base styling with grain texture"
```

---

## Task 2: Sidebar Navigation Component

**Files:**
- Create: `_includes/sidebar-nav.html`
- Modify: `assets/css/style.scss` (add sidebar styling)

**Step 1: Create sidebar include**

```html
<!-- _includes/sidebar-nav.html -->

<aside class="sidebar-nav">
  <div class="sidebar-header">
    <h1 class="sidebar-title">PETER<br>SALVATO</h1>
  </div>

  <nav class="sidebar-menu">
    <!-- Evidence Section -->
    <div class="nav-section">
      <h3 class="nav-section-title nav-section-title--creative">EVIDENCE</h3>
      <ul class="nav-list">
        <li><a href="/evidence/enterprise-systems">Enterprise Systems</a></li>
        <li><a href="/evidence/brand-systems">Brand Systems</a></li>
      </ul>
    </div>

    <!-- Labs Section -->
    <div class="nav-section">
      <h3 class="nav-section-title nav-section-title--systems">LABS</h3>
      <ul class="nav-list">
        <li><a href="/labs/visual-research">Visual Research</a></li>
        <li><a href="/labs/external">External Nodes</a></li>
      </ul>
    </div>

    <!-- System Section -->
    <div class="nav-section">
      <h3 class="nav-section-title nav-section-title--technical">SYSTEM</h3>
      <ul class="nav-list">
        <li><a href="/system/doctrine">Doctrine</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </div>
  </nav>
</aside>
```

**Step 2: Add sidebar styling to SCSS**

```scss
// Sidebar Navigation
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
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;

  @include grain-texture;

  @media (max-width: $bp-tablet) {
    display: none; // Hidden on mobile, will be toggled by hamburger
    position: fixed;
    width: 250px;
    background: $color-white;
    z-index: 999;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);

    &.active {
      display: block;
    }
  }
}

.sidebar-header {
  margin-bottom: $space-2xl;
  padding-bottom: $space-lg;
  border-bottom: 1px solid $color-border;
}

.sidebar-title {
  font-size: 14px;
  font-weight: 700;
  line-height: $line-height-tight;
  letter-spacing: 1px;
  margin: 0;
}

.sidebar-menu {
  list-style: none;
}

.nav-section {
  margin-bottom: $space-xl;

  &:last-child {
    margin-bottom: 0;
  }
}

.nav-section-title {
  font-size: 10px;
  font-weight: 700;
  margin: 0 0 $space-sm 0;
  padding-left: $space-sm;
  border-left: 3px solid $color-border;
  letter-spacing: 1px;
  color: $color-charcoal;

  &.nav-section-title--creative {
    border-left-color: $color-creative;
    color: $color-creative;
  }

  &.nav-section-title--systems {
    border-left-color: $color-systems;
    color: $color-systems;
  }

  &.nav-section-title--technical {
    border-left-color: $color-technical;
    color: $color-technical;
  }
}

.nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-list li {
  margin-bottom: $space-sm;

  a {
    font-size: 11px;
    color: $color-charcoal;
    text-decoration: none;
    border: none;
    display: block;
    padding: 2px $space-sm;
    transition: color $transition-fast;

    &:hover {
      color: $color-creative;
    }
  }
}
```

**Step 3: Adjust main layout for sidebar**

```scss
// Update .page-layout in main style.scss
.content-wrapper {
  grid-column: 2;

  @media (max-width: $bp-tablet) {
    grid-column: 1;
  }
}
```

**Step 4: Verify sidebar renders**

Run: `jekyll serve` and check `http://localhost:4000`

Expected: White sidebar visible on left with domain-colored section titles and navigation links.

**Step 5: Commit**

```bash
git add _includes/sidebar-nav.html assets/css/style.scss
git commit -m "feat: add sidebar navigation component with domain color accents"
```

---

## Task 3: Main Layout Grid & Content Wrapper

**Files:**
- Create: `_layouts/default.html`
- Modify: `assets/css/style.scss` (add layout grid)

**Step 1: Create default layout**

```html
<!-- _layouts/default.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if page.title %}{{ page.title }} | {% endif %}Peter Salvato</title>
    <meta name="description" content="{{ page.description | default: site.description }}">

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&family=Courier+Prime:wght@400&display=swap" rel="stylesheet">

    <!-- Main Stylesheet -->
    <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
</head>
<body>

<div class="page-layout">
    {% include sidebar-nav.html %}

    <div class="content-wrapper">
        {{ content }}
    </div>
</div>

</body>
</html>
```

**Step 2: Add asymmetrical grid styling for content sections**

```scss
// Content Section Grid
.content-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: $space-2xl;
  margin-bottom: $space-3xl;
  align-items: start;

  @media (max-width: $bp-tablet) {
    grid-template-columns: 1fr;
    gap: $space-xl;
  }
}

// Asymmetrical positioning helpers
.content-block {
  padding: $space-xl;
  background-color: $color-white;
  border: 1px solid $color-border;

  &.block--featured {
    grid-column: span 2;

    @media (max-width: $bp-tablet) {
      grid-column: span 1;
    }
  }

  &.block--left-accent {
    border-left: 4px solid $color-creative;
  }

  &.block--systems-accent {
    border-left: 4px solid $color-systems;
  }

  &.block--technical-accent {
    border-left: 4px solid $color-technical;
  }
}

.block-title {
  font-size: $font-size-xl;
  font-weight: 700;
  margin-bottom: $space-md;
  margin-top: 0;
}

.block-subtitle {
  font-size: $font-size-lg;
  color: #666;
  margin-bottom: $space-md;
  font-style: italic;
}
```

**Step 3: Verify layout renders**

Run: `jekyll serve`

Expected: Main content area displays to the right of sidebar, white background with grain texture visible.

**Step 4: Commit**

```bash
git add _layouts/default.html assets/css/style.scss
git commit -m "feat: add default layout with asymmetrical content grid"
```

---

## Task 4: Homepage Content Sections

**Files:**
- Create: `index.md`
- Modify: `assets/css/style.scss` (add section-specific styling)

**Step 1: Create homepage markdown**

```markdown
---
layout: default
title: Peter Salvato | Principal Systems Architect
---

# Positioning Statement

I'm a **principal systems architect** who bridges rigorous engineering and visual governance. I don't build products—I architect the systems that sustain them. My work lives at the intersection of creative direction, user experience architecture, and technical implementation.

---

## 1.0 THE EVIDENCE

### Enterprise Systems

#### The Encore Platform
**A 12-Year Longitudinal Study in Sovereign Architecture**

Principal Product Architect & Lead Frontend Engineer for a mission-critical enterprise SaaS platform. 12+ years of continuous architecture, migration, and evolution through technological change.

**Focus**: Decoupled frontend architecture. Component libraries. Routed UI state management. Visual governance at scale.

### Brand Commerce Systems

#### Aiden Jae
**Tokenized Identity System for Fine Jewelry**

Principal Designer / Brand Architect for high-fidelity luxury identity system. Unified typography strategy, material honesty in digital/physical contexts, omnichannel consistency.

#### Altrueism
**Brand Identity System**

Identity systems and visual governance for ethical commerce brand.

#### Everyday Gold
**E-Commerce Platform**

Platform design for direct-to-consumer jewelry commerce.

---

## 2.0 THE LABS

### Visual Research

Proprietary research into the physics of aesthetics and logistics.

- **Echo & Bone** — Typographic research into materiality and memory
- **Photogeography** — Visual studies in place and documentation
- **[More research projects]**

### External Nodes

Autonomous systems exploring different domains:

- **Modernist Homestead** — Biological logistics and land systems
- **3rd Ltd.** — Press and limited artifacts
- **Math on Tape** — Signal processing and audio systems

---

## 3.0 THE OPERATOR

**[Contact Information]**
**[Doctrine Link]**

---

*© 2026 Peter Salvato. Published by Joinery, LLC.*
```

**Step 2: Add section-specific styling**

```scss
// Homepage Sections
.positioning-statement {
  font-size: $font-size-lg;
  line-height: $line-height-relaxed;
  margin-bottom: $space-3xl;
  max-width: 700px;

  strong {
    font-weight: 700;
  }
}

.evidence-section,
.labs-section,
.operator-section {
  margin-bottom: $space-3xl;
}

.evidence-section h2,
.labs-section h2,
.operator-section h2 {
  color: $color-charcoal;
  border-bottom: 2px solid $color-border;
  padding-bottom: $space-md;
}

.evidence-section h3 {
  color: $color-creative;
  font-size: $font-size-xl;
  margin-top: $space-xl;
}

.labs-section h3 {
  color: $color-systems;
  font-size: $font-size-xl;
  margin-top: $space-xl;
}

.project-block {
  background-color: $color-light-gray;
  padding: $space-lg;
  margin-bottom: $space-lg;
  border-left: 3px solid $color-border;

  h4 {
    margin-top: 0;
    font-size: $font-size-lg;
  }
}
```

**Step 3: Verify homepage renders**

Run: `jekyll serve`

Expected: Homepage displays with positioning statement, Evidence section, Labs section, styled with domain colors and borders.

**Step 4: Commit**

```bash
git add index.md assets/css/style.scss
git commit -m "feat: add homepage content sections with professional styling"
```

---

## Task 5: Mobile Hamburger Menu

**Files:**
- Modify: `_layouts/default.html`
- Modify: `assets/css/style.scss`

**Step 1: Add hamburger toggle to layout**

```html
<!-- Update _layouts/default.html header -->

<body>

<!-- Mobile Hamburger Toggle (visible only on mobile) -->
<div class="mobile-header">
  <button class="hamburger-toggle" onclick="toggleMenu()" aria-label="Toggle menu">
    <span></span>
    <span></span>
    <span></span>
  </button>
</div>

<div class="page-layout">
    {% include sidebar-nav.html %}

    <div class="content-wrapper">
        {{ content }}
    </div>
</div>

<!-- Menu Toggle Script -->
<script>
  function toggleMenu() {
    const sidebar = document.querySelector('.sidebar-nav');
    const toggle = document.querySelector('.hamburger-toggle');
    sidebar.classList.toggle('active');
    toggle.classList.toggle('active');

    // Close sidebar when clicking outside
    document.addEventListener('click', function(event) {
      if (!event.target.closest('.sidebar-nav') && !event.target.closest('.hamburger-toggle')) {
        sidebar.classList.remove('active');
        toggle.classList.remove('active');
      }
    });
  }
</script>

</body>
```

**Step 2: Add hamburger styling**

```scss
// Mobile Header & Hamburger
.mobile-header {
  display: none;

  @media (max-width: $bp-tablet) {
    display: block;
    padding: $space-md;
    background-color: $color-white;
    border-bottom: 1px solid $color-border;
    @include grain-texture;
  }
}

.hamburger-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: $space-sm;
  width: 40px;
  height: 40px;
  position: relative;

  @media (max-width: $bp-tablet) {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 5px;
  }

  span {
    display: block;
    width: 24px;
    height: 2px;
    background-color: $color-charcoal;
    transition: all $transition-normal;
    border-radius: 1px;
  }

  &.active span:nth-child(1) {
    transform: rotate(45deg) translate(8px, 8px);
  }

  &.active span:nth-child(2) {
    opacity: 0;
  }

  &.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -7px);
  }
}

// Update sidebar for mobile
.sidebar-nav {
  @media (max-width: $bp-tablet) {
    display: none;
    position: fixed;
    width: 250px;
    background: $color-white;
    z-index: 998;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);

    &.active {
      display: block;
    }
  }
}

// Update content wrapper for mobile menu
.content-wrapper {
  @media (max-width: $bp-tablet) {
    margin-left: 0;
  }
}
```

**Step 3: Test hamburger menu**

Run: `jekyll serve`
- Open `http://localhost:4000` on desktop (hamburger hidden, sidebar visible)
- Resize to tablet width (~768px) - hamburger visible, sidebar hidden
- Click hamburger - sidebar slides in
- Click outside sidebar - closes

Expected: Hamburger menu appears on tablet/mobile, toggles sidebar visibility smoothly.

**Step 4: Commit**

```bash
git add _layouts/default.html assets/css/style.scss
git commit -m "feat: add mobile hamburger menu with smooth animations"
```

---

## Task 6: Responsive Refinements & Final Polish

**Files:**
- Modify: `assets/css/style.scss`

**Step 1: Add responsive image and spacing refinements**

```scss
// Add to style.scss

// Responsive Image Handling
img {
  max-width: 100%;
  height: auto;
  display: block;
}

// Fine-tune content padding at different breakpoints
.content-wrapper {
  padding: $space-2xl;

  @media (max-width: $bp-tablet) {
    padding: $space-xl;
    margin-top: 60px; // Account for mobile header height
  }

  @media (max-width: $bp-mobile) {
    padding: $space-lg;
  }
}

// Improve readability on mobile
@media (max-width: $bp-mobile) {
  h1 {
    font-size: $font-size-2xl;
  }

  h2 {
    font-size: $font-size-xl;
  }

  h3 {
    font-size: $font-size-lg;
  }

  .positioning-statement {
    font-size: $font-size-base;
  }
}

// Print styles
@media print {
  .sidebar-nav,
  .mobile-header {
    display: none;
  }

  .content-wrapper {
    grid-column: 1;
    margin: 0;
    padding: 0;
  }

  a {
    border: none;
  }
}
```

**Step 2: Verify all responsive breakpoints**

Run: `jekyll serve`
- Test at 1440px (desktop) - full sidebar, normal spacing
- Test at 1024px (small desktop) - full sidebar, slightly reduced spacing
- Test at 768px (tablet) - hamburger menu, sidebar hidden
- Test at 480px (mobile) - hamburger menu, optimized spacing

Expected: All breakpoints render correctly with proper spacing and hamburger functionality.

**Step 3: Test on multiple devices/browsers**

Use browser dev tools to simulate:
- iPhone 12 (390px)
- iPad (768px)
- Desktop (1440px)

Expected: All sections readable, no overflow, proper touch targets (40px+ buttons).

**Step 4: Commit**

```bash
git add assets/css/style.scss
git commit -m "feat: add responsive refinements and print styles"
```

---

## Task 7: Verify Build & Deploy

**Files:**
- All (verification only)

**Step 1: Clean rebuild**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
jekyll clean
jekyll build
```

Expected: Build completes without errors. `_site/` directory created with all files.

**Step 2: Local serve test**

```bash
jekyll serve --livereload
```

Open `http://localhost:4000` and verify:
- [ ] Sidebar visible on desktop
- [ ] All section headings display correctly
- [ ] Domain colors (red/green/blue) appear as accents
- [ ] Hamburger menu toggles on mobile view
- [ ] No layout shift or overflow
- [ ] Fonts load correctly (IBM Plex Sans)
- [ ] Grain texture visible on background

**Step 3: Commit and verify git log**

```bash
git log --oneline -10
```

Expected: 7 commits showing complete feature build.

**Step 4: Final commit message**

```bash
git commit --allow-empty -m "feat: complete homepage redesign - weathered NASA manual aesthetic with left sidebar and responsive design"
```

---

## Ready for Execution

Now executing with subagent-driven-development.
