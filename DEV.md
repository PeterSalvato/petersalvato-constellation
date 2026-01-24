# Development & Operations Guide

## Project Setup

**Project Root:** `/home/peter/homelab/projects/active/petersalvato.com/`

**Tech Stack:**
- Jekyll 4.4.1 (static site generator)
- Ruby (Gemfile)
- SCSS for styling (`assets/css/main.scss`)
- GitHub Pages for hosting
- Baseurl: `/petersalvato-constellation`

---

## Remote Workflow (Homelab Server via SSH)

### Initial Setup
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
bundle install
```

### Development Process

**1. Build the site**
```bash
bundle exec jekyll build
```
Compiles everything to `_site/`. Builds `main.scss` → `main.css`.

**2. Start local server with live reload**
```bash
bundle exec jekyll serve
```
- Runs at: `http://localhost:4000/petersalvato-constellation/`
- Auto-recompiles on file changes
- Keep this running in one terminal

**3. Edit styles in another terminal**
Edit: `assets/css/main.scss`
- Save file
- Watch terminal shows: `Regenerating: assets/css/main.scss`
- Refresh browser to see changes

**4. Edit content**
- Markdown files: `index.md`, `_evidence/*.md`, `_protocols/*.md`, `_labs/*.md`
- Data files: `_data/*.json`
- Templates: `_layouts/*.html`
- Includes: `_includes/*.html`

**5. Commit and push**
```bash
git add [files]
git commit -m "description"
git push origin main
```
GitHub Pages auto-deploys within 30 seconds.

---

## Local Workflow (Your Machine)

### Initial Setup
```bash
git clone https://github.com/PeterSalvato/petersalvato-constellation.git
cd petersalvato-constellation
bundle install
```

### Development
```bash
bundle exec jekyll serve
```
Visit: `http://localhost:4000/petersalvato-constellation/`

### After Changes
```bash
git add [files]
git commit -m "description"
git push origin main
```

---

## Key Files & Directories

| Path | Purpose |
|------|---------|
| `index.md` | Homepage (layout: systemworks) |
| `assets/css/main.scss` | **All styles go here** |
| `assets/css/main.css` | Compiled CSS (auto-generated) |
| `_layouts/*.html` | Page templates |
| `_includes/sidebar-nav.html` | Sidebar navigation |
| `_data/*.json` | Content data (navigation, projects, etc.) |
| `_evidence/` | Case study projects |
| `_protocols/` | Protocol/framework projects |
| `_labs/` | Lab/research projects |
| `_config.yml` | Jekyll configuration |
| `Gemfile` | Ruby dependencies |

---

## Common Tasks

### Edit Styles
```bash
# Remote or Local
nano/vim assets/css/main.scss
# Save file
# Watch terminal shows recompile
# Refresh browser
```

### Add New Project
1. Create markdown file in appropriate collection:
   - Evidence: `_evidence/project-name.md`
   - Protocols: `_protocols/project-name.md`
   - Labs: `_labs/project-name.md`

2. Add frontmatter:
   ```markdown
   ---
   layout: whitepaper
   title: "Project Title"
   client: "Client Name"
   ---
   ```

3. Write content
4. Push to deploy

### Update Navigation
Edit: `_data/navigation.json`
Changes appear immediately on next build.

### Update Manifesto/Philosophy
Edit: `_data/index.json` (sections: `manifesto` and top-level fields)
Changes appear on next build.

---

## Troubleshooting

**"main.css not found"**
- Run: `bundle exec jekyll build`
- Ensure `assets/css/main.scss` exists with front matter (`---\n---\n`)

**Changes not appearing**
- Refresh browser (hard refresh: Cmd+Shift+R)
- Check terminal shows "Regenerating"
- Rebuild: `bundle exec jekyll build`

**Links broken**
- Check baseurl in `_config.yml` is `/petersalvato-constellation`
- Use `{{ '/' | relative_url }}` for all internal links

---

## Deployment

**Automatic (GitHub Pages)**
- Push to `main` branch
- GitHub Actions auto-builds and deploys
- Live in ~30 seconds at `petersalvato.github.io/petersalvato-constellation`

**Manual (Remote Server)**
- Already pushing to GitHub, so no manual deploy needed
- Server mirrors production at all times

---

## Notes

- **SCSS:** Edit `assets/css/main.scss`, Jekyll compiles automatically
- **No npm required** for SCSS (using Jekyll's native SASS compiler)
- **All data in JSON** for consistency
- **Collections structure** keeps projects organized
- **Multi-page layout** preserved (sidebar + main content always visible)
