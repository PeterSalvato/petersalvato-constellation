# Narrative Reposition Corrective Plan (Proper IA)

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Apply the Cognitive Exoskeleton narrative positioning to the existing multi-page site structure WITHOUT destroying the sidebar nav, collections, or granular project pages.

**Architecture:** Preserve the working multi-page IA (sidebar nav + case-study pages + category indexes). Convert data layer from YAML to JSON. Apply strategic positioning copy to homepage and project pages. Maintain mid-century textbook aesthetic.

**Tech Stack:** Jekyll 4.3 | JSON data layer | Liquid templating | Case-study collections | Mid-century typography

**Key Constraint:** The multi-page structure with sidebar navigation is correct. Do not modify it. Only update copy and strategic positioning within this structure.

---

## Task 1: Convert Data Layer from YAML to JSON

**Files:**
- Convert: `_data/navigation.yml` → `_data/navigation.json`
- Convert: `_data/index.yml` → `_data/index.json`
- Convert: `_data/brand_systems.yml` → `_data/brand_systems.json`
- Convert: `_data/enterprise_systems.yml` → `_data/enterprise_systems.json`
- Convert: `_data/lab_projects.yml` → `_data/lab_projects.json`

**Step 1: Read current YAML files**

Run: `cat _data/navigation.yml && echo "---" && cat _data/index.yml | head -30`

Expected: YAML structure visible.

**Step 2: Convert navigation.yml to navigation.json**

Read the YAML structure and convert to JSON maintaining identical data:

```json
{
  "navigation": {
    "sections": [
      {
        "id": "intro",
        "title": "Introduction",
        "label": "The Work"
      },
      {
        "id": "evidence",
        "title": "Evidence",
        "label": "Case Studies"
      },
      {
        "id": "protocols",
        "title": "Protocols",
        "label": "Systems"
      },
      {
        "id": "labs",
        "title": "Labs",
        "label": "Research"
      }
    ]
  }
}
```

Create `_data/navigation.json` with this structure.

**Step 3: Convert index.yml to index.json**

The homepage manifesto/intro. Convert to JSON while preserving all content. Keep the manifesto text as-is (do NOT update it yet - that's Task 2).

**Step 4: Convert collection YAML files to JSON**

Convert `brand_systems.yml`, `enterprise_systems.yml`, `lab_projects.yml` to JSON equivalents with identical structure.

**Step 5: Update Jekyll templates to use .json instead of .yml**

Update `_layouts/systemworks.html` to reference `site.data.index` (works the same for both YAML and JSON in Jekyll).

**Step 6: Verify JSON syntax**

Run: `ruby -e "require 'json'; JSON.parse(File.read('_data/navigation.json'))" && echo "JSON Valid"`

Expected: "JSON Valid" for all converted files.

**Step 7: Test build**

Run:
```bash
rm -rf _site
bundle exec jekyll build --strict
```

Expected: Build succeeds, all pages render.

**Step 8: Verify navigation works**

Run: `grep -c "The Work\|Case Studies\|Systems" _site/index.html`

Expected: Navigation labels appear in sidebar.

**Step 9: Commit**

```bash
git add _data/*.json
git rm _data/*.yml
git commit -m "refactor: convert data layer from YAML to JSON

- Convert navigation.yml → navigation.json
- Convert index.yml → index.json
- Convert brand_systems.yml → brand_systems.json
- Convert enterprise_systems.yml → enterprise_systems.json
- Convert lab_projects.yml → lab_projects.json
- All data structure preserved, only format changed
- Jekyll processes JSON same as YAML

Maintains full compatibility with existing templates and structure.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Update Homepage Copy with Manifesto and Philosophy

**Files:**
- Modify: `_data/index.json` (manifesto section)
- Modify: `_layouts/systemworks.html` (if needed for philosophy rendering)

**Step 1: Update manifesto in index.json**

Replace the manifesto content with the strategic thesis (from the narrative reposition work):

```json
{
  "manifesto": {
    "id": "00",
    "title": "SYSTEMS FOR SOVEREIGNTY",
    "content": "I build sovereign, high-fidelity systems. Not products. Not SaaS. Systems designed for the gap between chaos and control.\n\nMost innovation fails because of Fidelity Drift—the growing distance between strategy, design, and implementation. By the time a product ships, the original intention has been compromised by frameworks, dependencies, and architectural shortcuts.\n\nI work at the seam of Design, Engineering, and AI Infrastructure. I am a Luthier—I build bespoke instruments because standard tools lack the resolution required for deep work.\n\nMy stack is intentionally idiosyncratic. Custom schemas. Local compute. Offline-first architecture. These choices are not over-engineering; they are Cognitive Ergonomics. They are built to scaffold the kind of rigor that prevents drift.\n\nThis site documents how a sovereign systems architect thinks. It is proof that you can build resilience in a vacuum, without corporate dependencies."
  }
}
```

**Step 2: Add philosophy section to index.json**

Add a new `philosophy` object at the root level:

```json
{
  "philosophy": {
    "title": "THE PHILOSOPHY",
    "sections": [
      {
        "id": "fidelity-drift",
        "title": "FIDELITY DRIFT",
        "content": "Most enterprises lose their original intent between strategy and execution. I use AI not to generate content, but to maintain cognitive context. Every system includes Drift Control mechanisms to preserve fidelity from concept through implementation."
      },
      {
        "id": "sovereignty",
        "title": "SOVEREIGNTY",
        "content": "Renting infrastructure creates fragility. I build Offline-First architectures. Systems that work without the grid. This is not anachronistic; it is resilience."
      },
      {
        "id": "neuro-ergonomics",
        "title": "NEURO-ERGONOMICS",
        "content": "Most interfaces are designed for mass adoption. They create noise. I design for signal. Interfaces that reduce cognitive load, reduce overwhelm."
      },
      {
        "id": "luthier",
        "title": "THE LUTHIER MODEL",
        "content": "A luthier doesn't build guitars with SaaS APIs. They understand wood, acoustics, the specific needs of the musician. I build software the same way. Custom schemas. Tailored constraints. Bespoke architectures."
      }
    ]
  }
}
```

**Step 3: Verify JSON syntax**

Run: `ruby -e "require 'json'; JSON.parse(File.read('_data/index.json'))" && echo "JSON Valid"`

Expected: "JSON Valid"

**Step 4: Test rendering on homepage**

Run:
```bash
rm -rf _site
bundle exec jekyll build --strict
grep "SYSTEMS FOR SOVEREIGNTY\|Fidelity Drift\|SOVEREIGNTY" _site/index.html | head -5
```

Expected: All strategic titles appear.

**Step 5: Commit**

```bash
git add _data/index.json
git commit -m "feat: update homepage manifesto and philosophy with strategic positioning

- Update manifesto with Cognitive Exoskeleton thesis
- Add philosophy section with 4 core concepts
- Keep existing multi-page structure intact
- Maintain sidebar navigation

Homepage now communicates sovereignty thesis without disrupting IA.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Update Case-Study Pages with Strategic Context

**Files:**
- Modify: Individual `.md` files in `_evidence/`, `_protocols/`, `_labs/`
- Modify: `_layouts/case-study.html` (if needed to display new frontmatter fields)

**Step 1: Add frontmatter fields to case-study template**

Update `_layouts/case-study.html` to support new frontmatter fields:
- `case_study_focus`: What does this project prove?
- `strategic_context`: How does this connect to the sovereignty thesis?

**Step 2: Update 3 key case studies**

Update these project pages with strategic positioning:

**_evidence/the-encore-platform.md:**
```markdown
---
layout: case-study
title: "The Encore Platform"
case_study_focus: "Fidelity Preservation Under Pressure"
strategic_context: "Proof that you can maintain operational integrity while completely replacing core infrastructure."
---

[existing content, updated with strategic language]
```

**_protocols/savepoint.md:**
```markdown
---
layout: case-study
title: "Savepoint Protocol"
case_study_focus: "Fidelity Preservation in Teams"
strategic_context: "Mechanism for maintaining epistemic fidelity across distributed teams."
---

[existing content, updated with strategic language]
```

**_labs/modernist-homestead.md:**
```markdown
---
layout: case-study
title: "Modernist Homestead"
case_study_focus: "Constraints Drive Quality"
strategic_context: "Applied constraints producing higher quality outcomes than willpower-dependent systems."
---

[existing content, updated with strategic language]
```

**Step 3: Update case-study.html template to display these fields**

Add sections to render `case_study_focus` and `strategic_context` with proper styling matching the mid-century aesthetic.

**Step 4: Test rendering**

Run:
```bash
bundle exec jekyll build --strict
grep "Fidelity Preservation\|Constraints Drive Quality" _site/evidence/the-encore-platform/index.html
```

Expected: Strategic context appears on individual project pages.

**Step 5: Commit**

```bash
git add _evidence/ _protocols/ _layouts/case-study.html
git commit -m "feat: add strategic context to case-study pages

- Update case-study.html template to display case_study_focus and strategic_context
- Add frontmatter to key projects (Encore Platform, Savepoint, Homelab, Modernist Homestead)
- Each project now explains what it proves about the sovereignty thesis
- Maintains granular multi-page structure

Individual project pages now communicate strategic positioning.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Update Site Metadata and Navigation Labels

**Files:**
- Modify: `_config.yml`
- Modify: `_data/navigation.json`

**Step 1: Update _config.yml**

```yaml
title: "Peter Salvato"
description: "Systems Architect for High-Fidelity Cognition. I build sovereign, resilient systems that treat complexity as a feature."
```

**Step 2: Update navigation labels in navigation.json**

Optionally enhance navigation labels to reflect strategic positioning:

```json
{
  "navigation": {
    "sections": [
      {
        "id": "intro",
        "title": "Sovereignty",
        "label": "The Philosophy"
      },
      {
        "id": "evidence",
        "title": "Infrastructure",
        "label": "Proof at Scale"
      },
      {
        "id": "protocols",
        "title": "Methods",
        "label": "Discipline"
      },
      {
        "id": "labs",
        "title": "Design",
        "label": "Research"
      }
    ]
  }
}
```

**Step 3: Test build**

Run: `bundle exec jekyll build --strict`

Expected: Build succeeds, navigation renders with new labels.

**Step 4: Commit**

```bash
git add _config.yml _data/navigation.json
git commit -m "refactor: update site metadata and navigation labels

- Change site description to 'Systems Architect for High-Fidelity Cognition'
- Update navigation labels to reflect strategic positioning
- Maintain sidebar nav structure and usability

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Establish Holding Company Hub-and-Spokes References

**Files:**
- Create: `_data/holding_company.json`
- Modify: Individual project pages (add spoke references where applicable)

**Step 1: Create holding_company.json**

```json
{
  "holding_company": {
    "hub": {
      "name": "petersalvato.com",
      "function": "Systems Architecture Portfolio"
    },
    "spokes": [
      {
        "id": "tasteonomy",
        "name": "Tasteonomy",
        "url": "https://tasteonomy.com",
        "hub_project": "Modernist Homestead"
      },
      {
        "id": "savepoint",
        "name": "Savepoint",
        "url": "https://savepoint.systems",
        "hub_project": "Savepoint Protocol"
      },
      {
        "id": "joinery",
        "name": "Joinery",
        "url": "https://joinerysystemworks.com",
        "hub_project": "Systems Architecture Practice"
      }
    ]
  }
}
```

**Step 2: Add spoke references to relevant project pages**

Add frontmatter to link projects to external spokes:

**_labs/modernist-homestead.md:**
```markdown
---
spoke_url: "https://tasteonomy.com"
spoke_name: "Tasteonomy"
---
```

**_protocols/savepoint.md:**
```markdown
---
spoke_url: "https://savepoint.systems"
spoke_name: "Savepoint"
---
```

**Step 3: Update case-study.html to render spoke links**

Add template logic to display a "Related Product" or "Standalone Project" link if spoke_url is present.

**Step 4: Commit**

```bash
git add _data/holding_company.json
git commit -m "feat: establish holding company hub-and-spokes references

- Create holding_company.json documenting hub and spokes
- Add spoke references to Modernist Homestead and Savepoint Protocol
- Case-study template displays links to standalone projects

Hub-and-Spokes architecture documented without disrupting main site structure.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Final Verification and Deployment

**Files:**
- Test: Full site build and verification

**Step 1: Clean build**

Run:
```bash
rm -rf _site
bundle exec jekyll build --strict 2>&1 | tail -10
```

Expected: "done in X seconds", no critical errors.

**Step 2: Verify sidebar navigation works**

Run: `grep -c "sidebar-nav\|The Work\|Case Studies\|Systems" _site/index.html`

Expected: Navigation elements present.

**Step 3: Verify collection pages render**

Run:
```bash
ls _site/evidence/ && ls _site/protocols/ && ls _site/labs/
```

Expected: All collection pages built successfully.

**Step 4: Verify strategic positioning on homepage**

Run: `grep "SYSTEMS FOR SOVEREIGNTY\|Fidelity Drift" _site/index.html`

Expected: Strategic title and concepts appear.

**Step 5: Verify individual case-study pages have context**

Run: `grep "case_study_focus" _site/evidence/the-encore-platform/index.html`

Expected: Strategic context rendered on project pages.

**Step 6: Verify no broken links**

Run: `grep -o 'href="[^"]*"' _site/index.html | grep -v "http" | sort -u | head -20`

Expected: Links point to `/evidence/`, `/protocols/`, `/labs/` correctly.

**Step 7: Final commit and deploy**

```bash
git add -A
git commit -m "build: complete narrative reposition with preserved IA

Final verification:
✓ Multi-page structure preserved (sidebar nav + case studies)
✓ Data layer converted from YAML to JSON
✓ Homepage manifesto updated with strategic positioning
✓ Philosophy section added to homepage
✓ Individual case-study pages have strategic context
✓ Collection pages render correctly
✓ Hub-and-Spokes references documented
✓ Mid-century textbook aesthetic maintained

The site now communicates sovereignty thesis while preserving:
- Granular multi-page navigation
- Sidebar navigation structure
- Individual project pages with deep dives
- Working internal links

Ready for evaluation.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"

git push origin main
```

Expected: Commits push successfully to GitHub.

---

## Summary

This plan applies the Cognitive Exoskeleton narrative positioning **without destroying the working IA**:

| Element | Action | Preserved |
|---------|--------|-----------|
| Multi-page structure | Keep intact | ✓ |
| Sidebar navigation | Keep intact | ✓ |
| Collections (_evidence, _protocols, _labs) | Keep intact | ✓ |
| Case-study layout | Keep intact | ✓ |
| Mid-century aesthetic | Keep intact | ✓ |
| Data layer | Convert YAML → JSON | ✓ |
| Homepage manifesto | Update with strategy | New |
| Philosophy section | Add to homepage | New |
| Case-study pages | Add strategic context | Enhanced |
| Hub-and-Spokes | Reference without disruption | New |

The result: **Strategic positioning applied to a working, granular, navigable multi-page site.**
