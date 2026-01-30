---
layout: whitepaper
title: "Deep Cuts: High-Density Concert Poster Series"
tags: [Typographic Systems, Data Visualization, Grid Architecture]
---

## The Work

Concert posters are usually mood boards. Big type, atmospheric graphics, maybe the date and venue. The actual performance data — what was played, in what order, for how long — lives on setlist.fm or in someone's memory.

Deep Cuts treats that data as the primary material. Each poster encodes a complete setlist: song titles, durations, encore markers, set breaks. The typographic system doesn't illustrate the concert — it *is* the concert record.

## The Approach

**Data Layer.** Each poster starts with a structured dataset — song title, duration (mm:ss), set number, position (opener/closer/encore), and notable annotations (debut, cover, rarity).

**Grid.** Fixed-axis layout. Vertical axis maps to set progression (top to bottom = first song to last). Horizontal axis maps to duration (wider = longer song). The grid becomes a visual signature of the performance — a long encore reads differently than a tight, fast set.

**Typography.** Three tiers. Primary: song titles in monospaced or fixed-width face. Secondary: duration, set markers, annotations at smaller weight, same grid alignment. Tertiary: venue, date, artist — framing data positioned outside the main grid.

**Color.** One or two accent colors per poster, derived from artist or venue identity. The system works in monochrome. Color is emphasis, not structure.

## The Numbers

| | |
|--------|--------|
| Format | Standard poster (18x24" or 11x17") |
| Data per poster | Complete setlist with durations and metadata |
| Typical setlist range | 15--25 songs across 2--3 sets |
| Typography tiers | 3 (primary, secondary, tertiary) |
| Grid type | Fixed-axis (vertical = progression, horizontal = duration) |
| Production | Digital first, 300dpi print-ready |

## What It Proves

This is a typographic hierarchy stress test. If the system holds at maximum data density — 25 songs, 3 sets, full metadata — without sacrificing readability, then the grid logic is sound. Different artists produce different data shapes. A jazz set with 8 long improvisations looks structurally different from a punk set with 22 two-minute songs. The system accommodates both without special-casing.
