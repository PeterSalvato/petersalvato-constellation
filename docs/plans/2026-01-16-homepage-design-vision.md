# petersalvato.com Homepage Design Vision

**Date**: 2026-01-16
**Status**: Vision Locked

---

## Design Direction

**Aesthetic**: Weathered NASA technical manual / academic textbook. Authoritative, scholarly, aged authenticity.

The homepage reads like a **precise technical document** with intellectual rigor as the primary visual language. The whimsy comes from the *quality and intersection of projects and thinking*, not from design embellishment. The form is austere; the content delights.

---

## Visual System

### Background
- **Color**: Pure white (#ffffff)
- **Texture**: Subtle grain overlay (aged paper quality, not noisy)
- **Overall Mood**: Clinical precision meets scholarly authenticity

### Typography
- **Family**: IBM Plex Sans (technical, geometric, precise)
- **Display/Headings**: IBM Plex Sans Bold
- **Body**: IBM Plex Sans Regular
- **Technical Labels**: Courier Prime (monospace, for system UI and navigation)
- **Color**: Dark charcoal (#2a2a2a)
- **Line Height**: Generous spacing for readability

### Color Palette (Desaturated RGB)
Used sparingly for domain signaling, not decoration.

- **Creative/Evidence Domain**: Desaturated Red (#b8523a)
- **Systems/Labs Domain**: Desaturated Green (#5a8c6f)
- **Technical/Frontend Domain**: Desaturated Blue (#4a6fa5)

Accent colors appear as:
- Section labels/category indicators
- Left-side borders on content blocks
- Link accents (muted, not bright)

---

## Layout Structure

### Left Sidebar (Fixed)
- **Width**: 200px
- **Position**: Fixed, full height, left edge
- **Background**: White with subtle grain (matches main)
- **Typography**: Monospace (Courier Prime) for technical feel

**Contents:**
1. Name/Logo Section at top
   - "PETER SALVATO"

2. Navigation Sections with Domain Color Accents
   - **EVIDENCE** (red accent stripe)
     - Enterprise Systems
     - Brand Commerce Systems
   - **LABS** (green accent stripe)
     - Visual Research
     - External Nodes
   - **SYSTEM** (blue accent stripe)
     - Doctrine
     - Contact

### Main Content Area
- **Margin**: Left margin to accommodate fixed sidebar
- **Composition**: Asymmetrical grid-based layout
- **Structure**:
  1. Positioning Statement (opening)
  2. The Evidence (Enterprise + Brand systems)
  3. The Labs (External nodes + visual research)
  4. The Operator (Contact, links, footer)

**Key Principle**: Content blocks positioned asymmetrically to suggest how domains inform each other. No literal Venn diagram. The *layout structure itself* demonstrates systematic thinking through careful composition.

### Responsive Behavior
- **Desktop (≥1024px)**: Full fixed sidebar + main content
- **Tablet (768px–1023px)**: Hamburger menu (sidebar hidden, toggle via icon)
- **Mobile (<768px)**: Hamburger menu, full-width content

---

## Visual Principles

1. **Rigor Through Structure**: Precision in typography, spacing, and grid alignment
2. **Restraint Over Embellishment**: Colors and textures support hierarchy, not decorate
3. **Asymmetrical Composition**: Layout suggests systematic thinking without literal diagrams
4. **Generous Whitespace**: Spacing is intentional and part of the visual message
5. **Content as the Star**: Design gets out of the way; projects and ideas speak for themselves

---

## Technical Constraints

- **Static Site Generator**: Jekyll (GitHub Pages compatible)
- **HTML/CSS**: Pure HTML/CSS (no JavaScript required for core functionality)
- **Includes/Partials**:
  - Sidebar navigation component
  - Content block templates
  - Footer component
- **Data Files**: YAML/JSON for project listings
- **Browser Support**: Modern browsers (no IE legacy support needed)

---

## Next Phase

Ready for implementation planning with bite-sized tasks and complete code.
