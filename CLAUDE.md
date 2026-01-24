# Claude Context: petersalvato.com

## Project Overview

**Peter Salvato's portfolio site** showcasing systems architecture work, using Jekyll for static generation and GitHub Pages for hosting.

**Key Concept:** Cognitive Exoskeleton thesis — building sovereign, high-fidelity systems without SaaS dependencies.

---

## Tech Stack

- **Generator:** Jekyll 4.4.1 (Ruby)
- **Styling:** SCSS (`assets/css/main.scss`) — Jekyll native compilation
- **Hosting:** GitHub Pages (`petersalvato-constellation` repo)
- **Baseurl:** `/petersalvato-constellation`
- **Data:** JSON (`_data/*.json`)
- **Collections:** `_evidence/`, `_protocols/`, `_labs/`

---

## Working With This Project

### For New Sessions

1. **Read:** `/DEV.md` (comprehensive dev guide)
2. **Key command:** `bundle exec jekyll serve` (starts local server at http://localhost:4000/petersalvato-constellation/)
3. **Edit styles:** `assets/css/main.scss` — Jekyll auto-compiles on save
4. **Build:** `bundle exec jekyll build` (compiles SCSS, generates `_site/`)

### Critical Files

| File | Purpose |
|------|---------|
| `assets/css/main.scss` | **All styles** (Jekyll compiles to main.css) |
| `_data/navigation.json` | Sidebar navigation structure |
| `_data/index.json` | Portfolio content, manifesto, projects |
| `_layouts/systemworks.html` | Homepage layout |
| `_layouts/whitepaper.html` | Case study pages layout |
| `_layouts/log.html` | Lab/protocol pages layout |
| `_layouts/default.html` | Base layout with sidebar |
| `_includes/sidebar-nav.html` | Sidebar navigation component |
| `_config.yml` | Jekyll config (baseurl, collections, etc.) |

---

## Architecture

### Layout Structure
- **Always side-by-side** (no mobile stacking)
- **Sidebar:** 350px fixed width, always visible
- **Main content:** calc(100% - 350px)
- **Responsive:** Only for tablets/mobile (if needed in future)

### Collections
- **_evidence/:** Mission-critical infrastructure projects
- **_protocols/:** Methods and frameworks (Savepoint, Order of the Ætherwright)
- **_labs/:** Research and experimental work

### Data Structure
- **navigation.json:** Sidebar sections (Evidence, Protocols, Labs)
- **index.json:** Manifesto, three domains, artifacts, contact
- **holding_company.json:** Hub-and-Spokes architecture documentation

---

## Voice & Positioning

**Tone:** Direct, grounded, no jargon, no performance
**Not:** Self-serious, academic, design cosplay
**Examples:**
- ✓ "Most systems fail because the parts don't talk to each other"
- ✗ "I build sovereign, high-fidelity systems designed for the gap between chaos and control"

**Key Concepts:**
- **Fidelity Drift:** Gap between strategy and implementation
- **Sovereignty:** Independence from SaaS, offline-first
- **Cognitive Ergonomics:** Interfaces designed for signal, not noise
- **Luthier Model:** Bespoke custom systems, not off-the-shelf

---

## Common Tasks

### Edit Styles
```bash
# Terminal: keep running
bundle exec jekyll serve

# Editor: edit and save
assets/css/main.scss
# → Terminal shows: Regenerating: assets/css/main.scss
# → Refresh browser
```

### Add Project
1. Create file: `_evidence/project-name.md` (or `_protocols/` or `_labs/`)
2. Add frontmatter:
   ```yaml
   ---
   layout: whitepaper
   title: "Title"
   client: "Client Name"
   tags: [tag1, tag2]
   ---
   ```
3. Write markdown content
4. Push to deploy

### Update Homepage Content
Edit: `_data/index.json`
- `manifesto.content` — Opening statement
- `domains[].artifacts[]` — Project listings

---

## Workflow Rules

**Always:**
- Run `bundle exec jekyll build` after pulling to regenerate CSS
- Edit only `main.scss`, never `main.css` (auto-generated)
- Use `{{ '/' | relative_url }}` for internal links (respects baseurl)
- Test locally with `jekyll serve` before pushing

**Never:**
- Edit compiled CSS (`main.css`)
- Break the sidebar + main-content flex layout
- Stack layout on desktop (always side-by-side)
- Change baseurl unless redirecting domain

---

## Debugging

**"Styles not applying"**
- Run: `bundle exec jekyll build`
- Check: `assets/css/main.scss` has front matter (`---\n---\n`)
- Verify: `assets/css/main.css` was generated

**"Links broken"**
- Use `{{ '/' | relative_url }}` in layouts
- Check `_config.yml` baseurl matches deployment

**"Collections not showing"**
- Verify collection files have correct `layout:` frontmatter
- Check collection definition in `_config.yml`

---

## Deployment

**Automatic:** Push to `main` → GitHub Pages auto-builds and deploys (~30s)

**Manual check:** `bundle exec jekyll build` generates `_site/` — contents match what deploys

---

## Future Work

- Integrate Itshover icons (semantic + aesthetic use, hover microinteractions)
- Refactor philosophy section if needed
- Hub-and-Spokes documentation (currently in `_data/holding_company.json`)

---

## Key Learnings

1. **Multi-page structure is intentional** — Collections + sidebar nav preserve granular project pages
2. **350px sidebar is fixed** — All pages always show it (no mobile stacking for now)
3. **Voice matters** — Direct, grounded tone. No self-seriousness.
4. **JSON over YAML** — User preference for data layer
5. **Jekyll native SCSS** — No npm watch needed; saves friction for remote development
6. **baseurl requirement** — Deployed at `/petersalvato-constellation/`, affects all links

---

## See Also

- `/DEV.md` — Detailed dev operations guide
- `/README.md` — Project overview (if exists)
- GitHub Repo: https://github.com/PeterSalvato/petersalvato-constellation
