# Claude Context: petersalvato.com

## Project Overview

**Peter Salvato's portfolio site** — a Master Builder's workbench. Jekyll static generation, GitHub Pages hosting.

**Key Concept:** Systems Architect — Design × Engineering × Strategy. Construction-site pragmatism applied to digital architecture. Supporting creative teams and neurodivergent founders.

---

## Tech Stack

- **Generator:** Jekyll 4.4.1 (Ruby)
- **Styling:** SCSS (`assets/css/main.scss`) — Jekyll native compilation
- **Hosting:** GitHub Pages (`petersalvato-constellation` repo)
- **Baseurl:** `/petersalvato-constellation`
- **Data:** JSON (`_data/*.json`)
- **Collections:** `_protocols/`, `_systems/`, `_practice/`

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
| `_data/navigation.json` | Sidebar navigation structure (3 tiers + About) |
| `_data/index.json` | Portfolio content, manifesto, routes, contact |
| `_layouts/systemworks.html` | Homepage layout |
| `_layouts/whitepaper.html` | Case study pages layout |
| `_layouts/log.html` | Protocol pages layout |
| `_layouts/workbench-spec.html` | Detailed spec pages layout |
| `_layouts/domain-index.html` | Tier landing pages layout |
| `_layouts/default.html` | Base layout with sidebar |
| `_includes/sidebar-nav.html` | Sidebar navigation component |
| `_config.yml` | Jekyll config (baseurl, collections, etc.) |

---

## Architecture

### Layout Structure
- **Always side-by-side** (no mobile stacking)
- **Sidebar:** 250px fixed width, always visible
- **Main content:** Offset by sidebar width + padding
- **Responsive:** Only for tablets/mobile (if needed in future)

### 3-Tier Structure

The site organizes work by intent across three tiers, plus a biographical section:

1. **Protocols** (red) — Governing logic and cognitive firmware (`_protocols/`)
2. **Applied Systems** (blue) — Production deployments under constraint (`_systems/`)
3. **Practice** (green) — Systemic research and expression (`_practice/`)
4. **About** (neutral) — Provenance + Colophon (standalone pages)

### Tier Landing Pages
- `/protocols/` — Lists Protocol artifacts (Savepoint, Aetherwright, AI DevOps Workbench, Portable Agency)
- `/systems/` — Lists Applied Systems artifacts (Encore, Joinery, Aiden-Jae, Everyday Gold, Altrueism, Modernist Homestead)
- `/practice/` — Lists Practice artifacts (New City, MathOnTape, Photogeography, The Deep Cuts, Echo & Bone, Versagrams)
- `/provenance/` — Full biographical page (no artifact list)

### Collections
- **_protocols/:** Foundational logic — Savepoint Protocol, Order of the Aetherwright, AI DevOps Workbench, Portable Agency
- **_systems/:** Production deployments — Encore, Joinery, Aiden-Jae, Everyday Gold, Altrueism, Modernist Homestead
- **_practice/:** Creative research — New City, MathOnTape, Photogeography, The Deep Cuts, Echo & Bone, Versagrams, Colophon

### Data Structure
- **navigation.json:** Sidebar sections (3 tiers + About, with color coding)
- **index.json:** Manifesto, three routes with artifacts, contact, legend
- **holding_company.json:** Hub-and-Spokes architecture documentation

---

## Voice & Positioning

**Protocol:** Master Builder voice. Full reference at `/docs/voice-protocol.md`.

**Summary:**
- Direct, concrete, specific. Materials and joints, not abstractions.
- Short declarative sentences. Longer ones only for causal chains.
- Lead with what was built. Then why. Then what it survived.
- No jargon that hasn't been earned through real work.
- No performance, no self-mythologizing.
- Every sentence must pass: "Would you say this out loud to a peer you respect?"

**Key vocabulary:** Build, hold, structure, durable, constraint, govern, fabrication, scaffold, stable
**Never use:** Paradigm, leverage, passionate, innovative, synergy, empower, journey

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
1. Create file: `_protocols/project-name.md` (or `_systems/` or `_practice/`)
2. Add frontmatter:
   ```yaml
   ---
   layout: whitepaper
   title: "Title"
   client: "Client Name"
   tags: [tag1, tag2]
   ---
   ```
3. Write markdown content in Master Builder voice
4. Push to deploy

### Update Homepage Content
Edit: `_data/index.json`
- `manifesto.content` — Opening statement
- `routes[].artifacts[]` — Project listings

---

## Workflow Rules

**Always:**
- Run `bundle exec jekyll build` after pulling to regenerate CSS
- Edit only `main.scss`, never `main.css` (auto-generated)
- Use `{{ '/' | relative_url }}` for internal links (respects baseurl)
- Test locally with `jekyll serve` before pushing
- Write all copy in Master Builder voice (see `/docs/voice-protocol.md`)

**Never:**
- Edit compiled CSS (`main.css`)
- Break the sidebar + main-content flex layout
- Stack layout on desktop (always side-by-side)
- Change baseurl unless redirecting domain
- Use jargon, aspirational language, or marketing copy

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
- Hub-and-Spokes documentation (currently in `_data/holding_company.json`)

---

## Key Learnings

1. **3-tier structure is intentional** — Protocols / Applied Systems / Practice, organized by intent
2. **250px sidebar is fixed** — All pages always show it (no mobile stacking for now)
3. **Voice matters** — Master Builder: direct, concrete, grounded. See `/docs/voice-protocol.md`
4. **JSON over YAML** — User preference for data layer
5. **Jekyll native SCSS** — No npm watch needed; saves friction for remote development
6. **baseurl requirement** — Deployed at `/petersalvato-constellation/`, affects all links
7. **`routes` not `domains`** — Data key in index.json is `routes`, templates iterate `site.data.index.routes`

---

## See Also

- `/docs/voice-protocol.md` — Full Master Builder voice protocol
- `/DEV.md` — Detailed dev operations guide
- GitHub Repo: https://github.com/PeterSalvato/petersalvato-constellation

---

## Frontmatter Checklist for New Projects

When adding a new project to any collection (`_protocols/`, `_systems/`, `_practice/`), ensure all required fields are present:

### All Projects (minimum)
- `layout`: Choose from `whitepaper` (case study), `workbench-spec` (technical spec), or `log` (protocol/framework)
- `title`: Project/artifact name
- `seo_keywords`: Array of 5-7 searchable terms

### workbench-spec Projects (required fields)
The following fields are required for `layout: workbench-spec` (primary layout for _systems/ and _practice/):

- `altitude`: "01" (Protocol), "02" (Applied System), or "03" (Practice)
  - **01** = Foundational logic, cognitive firmware, governing principles
  - **02** = Production deployment, enterprise/commercial/personal systems
  - **03** = Creative research, systemic expression, practice/exploration
- `context`: The problem or constraint (1-2 sentences)
- `drift`: The gap between intent and execution (1 sentence)
- `scaffold`: The structural solution (1-2 sentences)
- `fidelity`: The validation or result (1 sentence)
- `faculty`: Array of color strings `["red", "blue", "green"]` indicating domain weightings
  - `"red"` = Logic, governing logic, structural principles
  - `"blue"` = Utility, functionality, technical depth
  - `"green"` = Surface, expression, craft, presentation

### Faculty Color Mapping
| Color | Domain | Meaning |
|-------|--------|---------|
| red | Logic | Governing logic, structural rules, conceptual framework |
| blue | Utility | Function, performance, technical depth, operational |
| green | Surface | Craft, expression, aesthetic, presentation |

### Examples

**Aiden-Jae** (workbench-spec with multiple domains):
```yaml
faculty: ["blue", "green"]  # Technical infrastructure + aesthetic/craft
```

**Savepoint Protocol** (workbench-spec with mixed domains):
```yaml
faculty: ["red", "green"]  # Governing logic + expressiveness
```

**Colophon** (workbench-spec demonstrating all three):
```yaml
faculty: ["red", "blue", "green"]
```

### Layout Selection Guide

| Layout | Best For | Example |
|--------|----------|---------|
| `workbench-spec` | Technical systems, architectural details, multi-domain work with drift/scaffold/fidelity | Encore, Aiden-Jae, Modernist Homestead |
| `whitepaper` | Case studies, before/after narratives, design-focused work | (legacy; prefer workbench-spec) |
| `log` | Protocols, frameworks, cognitive systems, open-source tools | Savepoint Protocol, Order of the Aetherwright |

**Note:** All new projects should use `layout: workbench-spec` with complete altitude/drift/scaffold/fidelity/faculty metadata. Whitepaper layout is legacy.

### Verification Checklist

Before committing a new project:
- [ ] File in correct collection folder (`_protocols/`, `_systems/`, `_practice/`)
- [ ] Filename matches URL slug (lowercase, hyphens, no spaces)
- [ ] `layout` specified correctly (prefer workbench-spec)
- [ ] `title` field populated
- [ ] `seo_keywords` populated (5-7 terms) — essential for discoverability
- [ ] If workbench-spec: `altitude`, `context`, `drift`, `scaffold`, `fidelity`, `faculty` all present
- [ ] Content follows Master Builder voice (see `/docs/voice-protocol.md`)
- [ ] Internal links use `{{ '/' | relative_url }}` syntax
- [ ] Run `bundle exec jekyll build` locally to verify rendering
- [ ] Verify altitude marker displays (boxed "01"/"02"/"03")
- [ ] Verify faculty colors render as dots
