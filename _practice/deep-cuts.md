---
layout: workbench-spec
title: "Deep Cuts: High-Density Concert Poster Series"
drift: "Concert posters typically prioritize atmosphere over information. The data — setlists, song durations, encore sequences — gets discarded. No structural system exists for encoding full performance metadata into a typographic artifact."
scaffold: "Grid-governed typographic system. Each poster encodes complete setlist data. Song titles, durations, encore markers, and set breaks mapped into a fixed-axis layout. Swiss-style hierarchy stress-tested against maximum data density."
fidelity: "Typographic hierarchy holds at maximum density. Grid logic governs every element. Posters function as both visual artifacts and complete performance records."
faculty:
  logic: 40
  utility: 10
  surface: 50
---

## The Work

Concert posters are usually mood boards. Big type, atmospheric graphics, maybe the date and venue. The actual performance data — what was played, in what order, for how long — lives on setlist.fm or in someone's memory.

Deep Cuts treats that data as the primary material. Each poster encodes a complete setlist: song titles, durations, encore markers, set breaks. The typographic system doesn't illustrate the concert — it *is* the concert record.

## The Constraint

Maximum information density without breaking readability. That's the design problem. A typical setlist runs 15–25 songs across 2–3 sets. Each entry carries a title, duration, and positional metadata (opener, closer, encore). All of this has to fit inside a standard poster format and remain legible at reading distance.

The grid can't be decorative. It has to be structural — governing every element's position, size, and relationship to its neighbors. If you remove the grid, the poster should collapse. That's how you know it's load-bearing.

## The System

**Data layer:** Each poster starts with a structured dataset — song title, duration (mm:ss), set number, position (opener/closer/encore), and any notable annotations (debut, cover, rarity).

**Grid:** Fixed-axis layout. Vertical axis maps to set progression (top to bottom = first song to last). Horizontal axis maps to duration (wider = longer song). The grid itself becomes a visual signature of the performance — a long encore reads differently than a tight, fast set.

**Typography:** Three tiers.
- **Primary:** Song titles. Monospaced or fixed-width face. The backbone.
- **Secondary:** Duration, set markers, annotations. Smaller weight, same grid alignment.
- **Tertiary:** Venue, date, artist. Positioned outside the main grid — framing data, not performance data.

**Color:** Minimal. One or two accent colors per poster, derived from the artist or venue identity. The system doesn't depend on color — it works in monochrome. Color is emphasis, not structure.

## The Proof

This is a typographic hierarchy stress test. If the system holds at maximum data density — 25 songs, 3 sets, full metadata — without sacrificing readability, then the grid logic is sound. If it breaks, the grid needs work.

Every poster is a new test case. Different artists produce different data shapes. A jazz set with 8 long improvisations looks structurally different from a punk set with 22 two-minute songs. The system has to accommodate both without special-casing.

## Status

Series in development. Grid system specified. First test posters in production.

---

## Technical Specifications

**Format:** Standard poster (18x24" or 11x17")

**Data per poster:** Complete setlist — song titles, durations, set breaks, encore markers, annotations

**Grid:** Fixed-axis. Vertical = set progression. Horizontal = duration mapping.

**Typography:** Monospaced primary (song titles), proportional secondary (metadata), sans-serif tertiary (framing)

**Color:** 1–2 accent colors per poster. System works in monochrome.

**Production:** Digital first. Print-ready at 300dpi. Potential for letterpress or risograph editions.
