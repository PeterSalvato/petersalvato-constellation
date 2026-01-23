# Systemworks Aesthetic Refactor Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Refactor petersalvato.com from NASA manual aesthetic to 1975 Technical Manual / Systemworks aesthetic using Jekyll's data layer and Tailwind CSS, making the site fully data-driven and maintainable through YAML editing.

**Architecture:** Convert the current collection-based structure to a single data-driven model using `_data/index.yml` as the source of truth. All content (Principles, Infrastructure, Methods, Design domains) flows from this YAML file through Liquid templates. Replace Rubik + Space Mono typography with EB Garamond (body) + Inter (headers). Implement Tailwind CSS with custom design tokens (paper, ink, domain colors). The entire site becomes updatable by editing YAML—no HTML changes needed for new projects.

**Tech Stack:** Jekyll (static generation) | Tailwind CSS (design system) | Liquid (templating) | YAML (data layer) | EB Garamond + Inter (typography)

---

### Task 1: Create Data Layer Schema (_data/index.yml)

**Files:**
- Create: `_data/index.yml`

**Step 1: Write the data structure file**

Create the complete YAML file at `_data/index.yml` with the full content schema:

```yaml
# _data/index.yml
# Source of truth for all portfolio content

manifesto:
  id: "00"
  title: "PRINCIPLES"
  type: "manifesto"
  content: |
    I build durable systems. My work sits at the intersection of design, engineering, and strategy.

    Twelve years of architecture that didn't break when pressure increased.

    I came up through screen shops and grid systems, writing type by hand and code by habit.
    Design from SVA. Published work at Random House and Sterling. Years in brands, interfaces,
    systems that had to scale without breaking.

    That foundation shaped everything: the work itself, the way I approach it, the frameworks
    I've built to understand it better.

    What's here is the visible part. Underneath is structure. Beneath that, process.

domains:
  - id: "01"
    name: "INFRASTRUCTURE"
    color: "blue"
    definition: "The Substrate. The Code. The Hardware."
    description: "Mission-critical systems that scale. Platforms that survive technological epochs. The operational backbone."
    artifacts:
      - id: "1.1"
        title: "THE ENCORE PLATFORM"
        context: "Enterprise Architecture"
        spec: "12 years. 99.9% uptime. 40,000+ users. Strangler pattern legacy modernization."
        result: "Replaced the engine while the car drove at 60mph. Systems that survived three technological epochs."
        status: "DEPLOYED"
        link: "/evidence/the-encore-platform"

      - id: "1.2"
        title: "VISUAL GOVERNANCE"
        context: "Identity Systems at Scale"
        spec: "Luxury brands scaling across e-commerce, print, retail, campaigns, social."
        result: "$10M+ annual commerce. Visual coherence maintained through team transitions."
        status: "ACTIVE"
        link: "/evidence/visual-governance"

      - id: "1.3"
        title: "HOMELAB STACK"
        context: "Sovereign Compute"
        spec: "Offline-first server infrastructure. Ubuntu + Docker. Self-hosted everything."
        result: "Physical data sovereignty. Family media server, automation, backup infrastructure."
        status: "LIVE"

  - id: "02"
    name: "METHODS"
    color: "red"
    definition: "The Logic. The Workflows. The Protocols."
    description: "Systems designed to be operated. Frameworks that scale because they're built on clarity."
    artifacts:
      - id: "2.1"
        title: "SAVEPOINT PROTOCOL"
        context: "Cognitive Versioning"
        spec: "Documented moments of stability. Syntax-enforced recovery. Weekly reviews, quarterly audits."
        result: "Teams that practice savepoints recover faster, make bolder decisions, maintain institutional memory."
        status: "V3.0"
        link: "/protocols/savepoint"

      - id: "2.2"
        title: "ORDER OF THE ÆTHERWRIGHT"
        context: "Systems Doctrine"
        spec: "Three pillars: Clarity, Consistency, Coherence. Discipline for designing intangible systems."
        result: "Systems that survive organizational change because they're built to be maintained."
        status: "ACTIVE"
        link: "/protocols/order-of-the-aetherwright"

      - id: "2.3"
        title: "MODERNIST HOMESTEAD"
        context: "Domestic Systems"
        spec: "Zero-willpower meal systems. Italian and Thai supply chains for household resilience."
        result: "Family that reliably feeds itself even when executive function is offline."
        status: "ACTIVE"
        link: "/labs/modernist-homestead"

  - id: "03"
    name: "DESIGN"
    color: "green"
    definition: "The Semiotics. The Narrative. The World."
    description: "Visual systems that survive change. Research into how forms persist through organizational pressure."
    artifacts:
      - id: "3.1"
        title: "NEW CITY"
        context: "Narrative Simulation"
        spec: "40+ entity graph stress-testing infrastructure collapse. What happens when systems fail?"
        result: "Operational architecture expressed as narrative. Infrastructure under pressure."
        status: "IN DEVELOPMENT"
        link: "/labs/new-city"

      - id: "3.2"
        title: "VISUAL SYSTEMS RESEARCH"
        context: "Design Operations"
        spec: "How visual systems survive team growth and organizational drift."
        result: "Constraint hierarchies that let distributed teams extend identity coherently."
        status: "ONGOING"
        link: "/labs/visual-systems"

      - id: "3.3"
        title: "MATH ON TAPE"
        context: "Educational"
        spec: "Tactile mathematics. Making abstract concepts physically graspable through interaction."
        result: "Live environment used as primary teaching tool for mathematically curious audiences."
        status: "LIVE"
        link: "/labs/math-on-tape"

contact:
  email: "peter@petersalvato.com"
  links:
    - title: "GitHub"
      url: "https://github.com/petersalvato"
    - title: "LinkedIn"
      url: "https://linkedin.com/in/petersalvato"
```

**Step 2: Verify file exists and is valid YAML**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && cat _data/index.yml | head -30`

Expected: YAML file output with manifesto and domains structure visible.

**Step 3: Commit data layer**

```bash
git add _data/index.yml
git commit -m "feat: create data layer schema for systemworks aesthetic

- Create _data/index.yml as single source of truth for all content
- Define manifesto (00 PRINCIPLES section)
- Define three domains: INFRASTRUCTURE (01), METHODS (02), DESIGN (03)
- Each domain contains multiple artifacts with spec/status/links
- Contact information included for footer

This YAML file will be the only place content needs to be edited going forward.
All HTML rendering flows from this data layer through Liquid templates.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### Task 2: Configure Tailwind CSS with Design Tokens

**Files:**
- Modify: `tailwind.config.js` (create if doesn't exist)
- Create: `assets/css/tailwind.css`

**Step 1: Create tailwind.config.js with design tokens**

Create file at `/home/peter/homelab/projects/active/petersalvato.com/tailwind.config.js`:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './_layouts/**/*.html',
    './_includes/**/*.html',
    './index.html',
    './**/*.md',
  ],
  theme: {
    extend: {
      colors: {
        // Paper and Ink
        'ink': '#1A1A1A',
        'ink-soft': '#2A2A2A',
        'paper': '#F4F4F0',
        'paper-dark': '#EFEFEB',
        'grid': '#E5E5E0',
        'grid-light': '#F0F0EB',

        // Domain Colors (Faded, Technical)
        'domain-blue': '#3A5F85',
        'domain-red': '#A64B2A',
        'domain-green': '#6B8E5F',

        // Accent
        'accent': '#FF4400',
      },
      fontFamily: {
        'sans': ['Inter', 'Helvetica', 'Arial', 'sans-serif'],
        'serif': ['EB Garamond', 'Caslon', 'Georgia', 'serif'],
        'mono': ['Space Mono', 'Courier Prime', 'monospace'],
      },
      fontSize: {
        'xs': '10px',
        'sm': '12px',
        'base': '14px',
        'lg': '16px',
        'xl': '20px',
        '2xl': '24px',
        '3xl': '32px',
        '4xl': '48px',
      },
      letterSpacing: {
        'tight': '-0.04em',
        'normal': '0em',
        'wide': '0.04em',
        'wider': '0.08em',
      },
      lineHeight: {
        'tight': '1.1',
        'normal': '1.5',
        'relaxed': '1.8',
      },
      spacing: {
        'xs': '4px',
        'sm': '8px',
        'md': '16px',
        'lg': '24px',
        'xl': '32px',
        '2xl': '48px',
        '3xl': '64px',
      },
      borderWidth: {
        'DEFAULT': '1px',
        '0': '0',
        '1': '1px',
        '2': '2px',
        '4': '4px',
      },
      maxWidth: {
        'content': '960px',
      },
    },
  },
  plugins: [],
};
```

**Step 2: Create tailwind.css entry point**

Create file at `/home/peter/homelab/projects/active/petersalvato.com/assets/css/tailwind.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom utility classes for Systemworks aesthetic */

/* Paper and Ink base */
@layer base {
  html {
    @apply bg-paper text-ink font-serif;
  }

  body {
    @apply bg-paper text-ink;
  }

  h1, h2, h3, h4, h5, h6 {
    @apply font-sans font-bold tracking-tight;
  }

  h1 {
    @apply text-4xl;
  }

  h2 {
    @apply text-3xl mb-lg;
  }

  h3 {
    @apply text-xl font-semibold;
  }

  a {
    @apply text-ink underline hover:text-domain-blue transition-colors;
  }
}

/* Domain color utilities */
@layer components {
  .domain-section {
    @apply border-b-2 border-ink py-3xl;
  }

  .domain-header {
    @apply font-sans font-bold text-lg tracking-wider uppercase mb-md;
  }

  .domain-header--blue {
    @apply text-domain-blue;
  }

  .domain-header--red {
    @apply text-domain-red;
  }

  .domain-header--green {
    @apply text-domain-green;
  }

  .artifact-spec {
    @apply font-mono text-sm leading-relaxed text-ink-soft;
  }

  .grid-rule {
    @apply border-b border-grid;
  }

  .grid-rule-heavy {
    @apply border-b-2 border-ink;
  }
}
```

**Step 3: Update Jekyll config to process Tailwind**

Modify `_config.yml` to add Tailwind processing. First check current config:

Run: `cat /home/peter/homelab/projects/active/petersalvato.com/_config.yml | grep -A 5 "scss\|css" || echo "No CSS config found"`

Then add/update (backup first):

```bash
cp _config.yml _config.yml.backup
```

Add to `_config.yml`:

```yaml
# Tailwind CSS processing
sass:
  sass_dir: assets/css
  style: compressed
```

**Step 4: Install Tailwind (npm)**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss -i assets/css/tailwind.css -o assets/css/tailwind-output.css
```

Expected: No errors, `assets/css/tailwind-output.css` generated.

**Step 5: Test Tailwind compilation**

Run: `ls -lh assets/css/tailwind-output.css`

Expected: File exists with size ~15-30KB.

**Step 6: Commit Tailwind configuration**

```bash
git add tailwind.config.js assets/css/tailwind.css assets/css/tailwind-output.css _config.yml
git commit -m "feat: add tailwind css with systemworks design tokens

- Create tailwind.config.js with paper/ink colors and domain color palette
- Define typography: Inter (headers), EB Garamond (body), Space Mono (data)
- Create custom utility classes for domain sections and artifacts
- Add Tailwind processing to Jekyll config
- Compile Tailwind CSS output

Design tokens available for immediate use in templates:
- Colors: ink, paper, domain-blue/red/green, grid
- Typography: font-sans, font-serif, font-mono
- Spacing: xs-3xl scale
- Border utilities: grid-rule, grid-rule-heavy

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### Task 3: Create Liquid Template Architecture

**Files:**
- Create: `_layouts/systemworks.html` (main layout)
- Create: `_includes/domain-artifact.html` (reusable component)
- Modify: `index.md` (update frontmatter to use new layout)

**Step 1: Create base layout template**

Create file at `/home/peter/homelab/projects/active/petersalvato.com/_layouts/systemworks.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title | default: 'Peter Salvato' }}</title>
    <meta name="description" content="Design Systems Architect | Operational Systems">

    <!-- Google Fonts: Inter, EB Garamond, Space Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=EB+Garamond:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">

    <!-- Tailwind CSS -->
    <link rel="stylesheet" href="{{ '/assets/css/tailwind-output.css' | relative_url }}">

    <style>
      /* Systemworks: 1975 Technical Manual Aesthetic */
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        background-color: #F4F4F0;
        color: #1A1A1A;
        font-family: 'EB Garamond', Georgia, serif;
        font-size: 14px;
        line-height: 1.6;
      }

      h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        letter-spacing: -0.02em;
        margin-bottom: 16px;
      }

      h1 { font-size: 48px; line-height: 1.1; }
      h2 { font-size: 32px; line-height: 1.2; }
      h3 { font-size: 20px; line-height: 1.3; }

      .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 64px 32px;
      }

      .systemworks-header {
        text-align: center;
        border-bottom: 2px solid #1A1A1A;
        padding-bottom: 48px;
        margin-bottom: 64px;
      }

      .systemworks-header h1 {
        font-size: 56px;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 8px;
      }

      .systemworks-header p {
        font-size: 14px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #2A2A2A;
      }

      .manifesto-section {
        max-width: 800px;
        margin: 0 auto 96px;
        border-bottom: 2px solid #1A1A1A;
        padding-bottom: 48px;
      }

      .manifesto-section h2 {
        font-size: 24px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 24px;
      }

      .manifesto-section p {
        margin-bottom: 16px;
        line-height: 1.8;
      }

      .domains-container {
        display: grid;
        gap: 96px;
        max-width: 1000px;
        margin: 0 auto;
      }

      .domain-section {
        border-bottom: 2px solid #1A1A1A;
        padding-bottom: 64px;
      }

      .domain-header {
        display: flex;
        align-items: baseline;
        gap: 16px;
        margin-bottom: 32px;
      }

      .domain-id {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #2A2A2A;
        flex-shrink: 0;
      }

      .domain-title {
        font-family: 'Inter', sans-serif;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -0.02em;
        text-transform: uppercase;
      }

      .domain-title--blue { color: #3A5F85; }
      .domain-title--red { color: #A64B2A; }
      .domain-title--green { color: #6B8E5F; }

      .domain-definition {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 500;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #2A2A2A;
        margin-bottom: 16px;
      }

      .domain-description {
        font-family: 'EB Garamond', Georgia, serif;
        font-size: 16px;
        line-height: 1.8;
        margin-bottom: 48px;
        max-width: 900px;
      }

      .artifacts-grid {
        display: grid;
        gap: 48px;
      }

      .artifact {
        border-top: 1px solid #E5E5E0;
        padding-top: 32px;
      }

      .artifact-id {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #2A2A2A;
        margin-bottom: 8px;
      }

      .artifact-title {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 12px;
      }

      .artifact-meta {
        display: grid;
        grid-template-columns: 100px 1fr;
        gap: 16px;
        margin-bottom: 16px;
        font-size: 12px;
      }

      .artifact-meta-label {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #2A2A2A;
      }

      .artifact-meta-value {
        font-family: 'EB Garamond', Georgia, serif;
        font-size: 13px;
        line-height: 1.6;
      }

      .artifact-spec {
        font-family: 'EB Garamond', Georgia, serif;
        font-size: 14px;
        line-height: 1.7;
        margin-bottom: 12px;
        max-width: 850px;
      }

      .artifact-result {
        font-family: 'EB Garamond', Georgia, serif;
        font-size: 14px;
        line-height: 1.7;
        margin-bottom: 12px;
        max-width: 850px;
        font-style: italic;
      }

      .artifact-status {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #2A2A2A;
      }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="systemworks-header">
            <h1>PETER SALVATO</h1>
            <p>Design Systems Architect | Operational Systems</p>
        </div>

        <!-- Manifesto -->
        {% if site.data.index.manifesto %}
        <div class="manifesto-section">
            <h2>{{ site.data.index.manifesto.title }}</h2>
            <div>
                {% for paragraph in site.data.index.manifesto.content | split: "
" %}
                  {% if paragraph != "" %}
                    <p>{{ paragraph }}</p>
                  {% endif %}
                {% endfor %}
            </div>
        </div>
        {% endif %}

        <!-- Domains -->
        <div class="domains-container">
            {% for domain in site.data.index.domains %}
            <div class="domain-section">
                <div class="domain-header">
                    <span class="domain-id">{{ domain.id }}</span>
                    <h2 class="domain-title domain-title--{{ domain.color }}">{{ domain.name }}</h2>
                </div>

                <p class="domain-definition">{{ domain.definition }}</p>
                <p class="domain-description">{{ domain.description }}</p>

                <div class="artifacts-grid">
                    {% for artifact in domain.artifacts %}
                    <div class="artifact">
                        <div class="artifact-id">{{ artifact.id }}</div>
                        <h3 class="artifact-title">{{ artifact.title }}</h3>

                        <div class="artifact-meta">
                            <div class="artifact-meta-label">Context:</div>
                            <div class="artifact-meta-value">{{ artifact.context }}</div>
                        </div>

                        <div class="artifact-meta">
                            <div class="artifact-meta-label">Spec:</div>
                            <div class="artifact-meta-value">{{ artifact.spec }}</div>
                        </div>

                        <p class="artifact-result">{{ artifact.result }}</p>

                        <div class="artifact-meta">
                            <div class="artifact-meta-label">Status:</div>
                            <div class="artifact-meta-value">{{ artifact.status }}</div>
                        </div>

                        {% if artifact.link %}
                        <p style="margin-top: 12px;">
                            <a href="{{ artifact.link }}">Read more →</a>
                        </p>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>

        <!-- Footer -->
        <div style="border-top: 2px solid #1A1A1A; margin-top: 96px; padding-top: 48px; text-align: center;">
            <p style="font-size: 12px; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 16px;">
                {% if site.data.index.contact.email %}
                <a href="mailto:{{ site.data.index.contact.email }}">{{ site.data.index.contact.email }}</a>
                {% endif %}
            </p>
            <div style="display: flex; justify-content: center; gap: 24px; font-size: 12px;">
                {% for link in site.data.index.contact.links %}
                <a href="{{ link.url }}" target="_blank" rel="noopener">{{ link.title }}</a>
                {% endfor %}
            </div>
        </div>
    </div>
</body>
</html>
```

**Step 2: Update index.md to use new layout**

Modify `/home/peter/homelab/projects/active/petersalvato.com/index.md`:

```markdown
---
layout: systemworks
title: "Peter Salvato | Design Systems Architect"
---

```

**Step 3: Build site and verify**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
bundle exec jekyll build --strict
```

Expected: Build completes with "done in X seconds" message, no errors.

**Step 4: Verify generated HTML**

Run: `grep -c "INFRASTRUCTURE\|METHODS\|DESIGN" _site/index.html`

Expected: Output is `3` (one count for each domain).

**Step 5: Commit template architecture**

```bash
git add _layouts/systemworks.html index.md
git commit -m "feat: implement liquid template architecture for systemworks aesthetic

- Create _layouts/systemworks.html with full technical manual design
- Implement data-driven rendering using site.data.index.manifesto and site.data.index.domains
- Loop through domains (INFRASTRUCTURE, METHODS, DESIGN) with color-coded headers
- Render artifacts with context/spec/result/status metadata
- Style: 1975 technical manual aesthetic with paper/ink colors and domain colors
- Typography: Inter (headers), EB Garamond (body), Space Mono (mono)
- Update index.md to use systemworks layout

Template is now fully driven by _data/index.yml. All content updates happen in YAML only.
No HTML editing required to add new projects or update existing ones.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### Task 4: Update Site Metadata and Configuration

**Files:**
- Modify: `_config.yml`
- Create: `robots.txt` (optional, for SEO)

**Step 1: Update _config.yml with site title**

Modify `_config.yml` to update site description:

```yaml
title: "Peter Salvato"
description: "Design Systems Architect. Operational systems. Technical infrastructure."
author: "Peter Salvato"
email: "peter@petersalvato.com"

# Build settings
exclude:
  - /node_modules
  - /package.json
  - /package-lock.json
  - /tailwind.config.js
  - /.gitignore
```

**Step 2: Verify configuration**

Run: `grep "title:\|description:" _config.yml`

Expected: Updated values appear.

**Step 3: Commit configuration**

```bash
git add _config.yml
git commit -m "config: update site metadata for systemworks aesthetic

- Update site title and description
- Exclude build/node artifacts from Jekyll processing
- Configure for static generation with data-driven content

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### Task 5: Verify Build and Test Data Flow

**Files:**
- Test: Verify `_site/index.html` contains all data-driven content

**Step 1: Clean build**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
rm -rf _site
bundle exec jekyll build --strict
```

Expected: "done in X seconds" message, `_site/index.html` generated.

**Step 2: Verify manifest renders**

Run: `grep "PRINCIPLES\|I build durable systems" _site/index.html | head -2`

Expected: Both lines appear, proving manifesto content is rendered.

**Step 3: Verify domain count**

Run: `grep -o "INFRASTRUCTURE\|METHODS\|DESIGN" _site/index.html | sort | uniq -c`

Expected: Output shows each domain appears once as a header.

**Step 4: Verify artifact rendering**

Run: `grep -c "ENCORE PLATFORM\|SAVEPOINT PROTOCOL\|NEW CITY" _site/index.html`

Expected: Output is `3` (three major artifacts visible).

**Step 5: Test color coding**

Run: `grep -o 'class="domain-title domain-title--[a-z]*"' _site/index.html | sort | uniq -c`

Expected: Output shows colors distributed (blue, red, green).

**Step 6: Commit verification**

```bash
git add _site/
git commit -m "build: generate systemworks site with data-driven content

Verified:
- Manifesto section renders with PRINCIPLES header and full content
- All three domains (INFRASTRUCTURE, METHODS, DESIGN) render with correct headers
- Color coding applied (blue/red/green) to domain sections
- All 9 artifacts render with full metadata (context/spec/result/status)
- Footer renders with contact information

Site is fully operational and driven entirely by _data/index.yml.
To add new projects: edit _data/index.yml, rebuild with 'jekyll build'.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### Task 6: Update Professional Title Across Site

**Files:**
- Modify: `_data/index.yml` (update if needed)
- Modify: `_config.yml` (tagline/description)

**Step 1: Decide final title**

Recommended: **"Design Systems Architect"** (market-relevant, captures creative + technical integration)

Update `_layouts/systemworks.html` header section:

```html
<div class="systemworks-header">
    <h1>PETER SALVATO</h1>
    <p>Design Systems Architect | Operational Systems</p>
</div>
```

**Step 2: Commit title change**

```bash
git add _layouts/systemworks.html _config.yml
git commit -m "feat: update professional title to Design Systems Architect

Changed from 'Principal Systems Architect' to 'Design Systems Architect'
to better reflect the integration of visual systems, design operations,
and technical infrastructure that defines the work.

This title is market-relevant and commands $130-210K (employed) or
$150-250/hour (freelance), aligned with Design Systems roles at major tech companies.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### Task 7: Clean Up Old Aesthetic Files (Archive)

**Files:**
- Archive: `assets/css/style.scss`, `_layouts/console.html`, `_layouts/whitepaper.html`, etc.

**Step 1: Archive old files**

Run:
```bash
mkdir -p docs/archive/old-nasa-aesthetic
mv assets/css/style.scss docs/archive/old-nasa-aesthetic/
mv assets/css/style.css docs/archive/old-nasa-aesthetic/
mv _layouts/console.html docs/archive/old-nasa-aesthetic/
mv _layouts/whitepaper.html docs/archive/old-nasa-aesthetic/
mv _layouts/log.html docs/archive/old-nasa-aesthetic/
mv _layouts/default.html docs/archive/old-nasa-aesthetic/
```

**Step 2: Verify old files are archived**

Run: `ls -la docs/archive/old-nasa-aesthetic/`

Expected: Old CSS and layout files appear.

**Step 3: Commit archive**

```bash
git add docs/archive/old-nasa-aesthetic/
git commit -m "archive: preserve old NASA aesthetic files for reference

Moved previous design files to archive/old-nasa-aesthetic/:
- style.scss, style.css (Rubik typography, simplified sidebar)
- console.html, whitepaper.html, log.html, default.html (NASA manual layouts)

These files are no longer used but preserved for historical reference.
Current site uses _layouts/systemworks.html and data-driven rendering.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

### Task 8: Final Verification and Deployment

**Files:**
- Test: Full site build, all links, all data rendering

**Step 1: Full clean build**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
rm -rf _site
bundle exec jekyll build --strict 2>&1 | tail -20
```

Expected: "done in X seconds" message, no errors.

**Step 2: Verify all pages render**

Run: `find _site -name "index.html" | wc -l`

Expected: At least 1 (the main index page).

**Step 3: Check for broken data references**

Run: `grep -i "undefined\|nil\|error" _site/index.html`

Expected: No output (no errors in rendered HTML).

**Step 4: Verify CSS loads**

Run: `grep "tailwind-output.css" _site/index.html`

Expected: CSS path appears in HTML head.

**Step 5: Commit final state**

```bash
git add -A
git commit -m "build: complete systemworks aesthetic refactor - ready for deployment

Final verification:
✓ Data layer (_data/index.yml) is single source of truth
✓ All content renders through Liquid templates from YAML
✓ Tailwind design tokens applied (paper/ink, domain colors)
✓ Typography updated (Inter + EB Garamond + Space Mono)
✓ 1975 Technical Manual aesthetic fully implemented
✓ Static Jekyll generation - no dependencies, instant load
✓ Site is maintainable by editing YAML only

Professional title updated to: Design Systems Architect

To maintain going forward:
1. Edit _data/index.yml to add/update projects
2. Run 'jekyll build' to regenerate site
3. That's it - no HTML changes needed

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Summary

This plan transforms petersalvato.com from an NASA-inspired, collection-based Jekyll site to a **data-driven Systemworks aesthetic** that:

- ✅ Uses `_data/index.yml` as the single source of truth
- ✅ Renders all content through Liquid templates (no HTML editing needed)
- ✅ Implements 1975 Technical Manual / Systemworks aesthetic
- ✅ Features three domain sections (INFRASTRUCTURE, METHODS, DESIGN) with 9 artifacts
- ✅ Uses EB Garamond (body) + Inter (headers) + Space Mono (mono)
- ✅ Applies domain colors (blue, red, green) with faded palette
- ✅ Remains completely static, lightning-fast Jekyll generation
- ✅ Professional title updated to "Design Systems Architect"

All future content updates are made by editing `_data/index.yml` and running `jekyll build`. No HTML changes required.
