# Narrative Reposition Refactor: Cognitive Exoskeleton Edition

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Reposition petersalvato.com from a standard design systems portfolio to a strategic thesis-driven site that communicates "I build sovereign, high-fidelity systems that filter for autonomy-respecting leadership."

**Architecture:** Rebuild the YAML data layer to emphasize philosophical positioning (Sovereign Systems, Fidelity, Cognitive Exoskeleton) alongside projects. Add new pages for Philosophy and Engagement Models. Rewrite all copy to use strategic language (Luthier, Drift Control, Epistemic Fidelity). Maintain Jekyll static generation and Tailwind CSS styling.

**Tech Stack:** Jekyll 4.3 | Liquid templating | YAML data layer | Tailwind CSS | Strategic copywriting

**Holding Company Structure:** This site (Hub) operates as the Meta-Layer / Command Center. Individual projects (Spokes) remain opaque and standalone. The Hub links to Spokes with architectural context that reveals the systems thinking ("Magic Trick" + "Trapdoor").

---

## Task 0: Establish Holding Company Architecture

**Files:**
- Create: `_data/holding_company.yml` (Hub-and-Spokes metadata)
- Modify: `_data/index.yml` (add spoke references to artifacts)

**Step 1: Create holding company structure file**

Create `_data/holding_company.yml`:

```yaml
holding_company:
  hub:
    name: "petersalvato.com"
    function: "Glass Box / Meta-Layer / Command Center"
    description: "Full transparency. Explains systems thinking, reveals the machinery, aggregates the ecosystem."

  spokes:
    - id: "tasteonomy"
      name: "Tasteonomy"
      type: "Product / Sensory Systems"
      url: "https://tasteonomy.com"
      description: "Algorithmic sensory systems applied to culinary arts."
      hub_framing: "A stress-test of software versioning logic and constraint systems applied to biological recipes."
      hub_artifact_id: "2.3"
      rules:
        - "Operates as independent brand"
        - "Does not mention Peter the Architect"
        - "Does not link back to Hub"
        - "Graduation from side project to venture"

    - id: "joinery"
      name: "Joinery"
      type: "Service / Operational Interface"
      url: "https://joinerysystemworks.com"
      description: "Modular operational architecture and consulting interface."
      hub_framing: "Proof of Headless business logic and API-first organizational design."
      hub_artifact_id: "Overarching"
      rules:
        - "Operates as independent consulting brand"
        - "Does not mention the Hub ecosystem"
        - "Stands alone as complete service offering"
        - "Graduation from internal framework to market offering"

    - id: "savepoint"
      name: "Savepoint"
      type: "Framework / Knowledge Management"
      url: "https://savepoint.systems"
      description: "Zero-latency knowledge engine and cognitive versioning protocol."
      hub_framing: "Proof of Fidelity Preservation in distributed teams and context management at scale."
      hub_artifact_id: "2.1"
      rules:
        - "Operates as open-source framework"
        - "Does not link to consulting practice"
        - "Stands alone as technical tool"
        - "Graduation to independent technical asset"

  bridge_principle: "The Hub reveals the systems thinking. The Spokes prove it works in the wild."
```

**Step 2: Verify YAML validity**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && ruby -e "require 'yaml'; YAML.load_file('_data/holding_company.yml')" && echo "YAML Valid"`

Expected: "YAML Valid"

**Step 3: Add spoke references to artifacts in index.yml**

For each artifact that has a corresponding spoke, add a `spoke_id` field:

```yaml
# Example for MODERNIST HOMESTEAD (Tasteonomy spoke)
- id: "2.3"
  title: "MODERNIST HOMESTEAD"
  # ... existing fields ...
  spoke_id: "tasteonomy"
  spoke_external_url: "https://tasteonomy.com"
  hub_context: "A stress-test of software versioning logic and constraint systems applied to biological recipes."

# Example for SAVEPOINT PROTOCOL (Savepoint spoke)
- id: "2.1"
  title: "SAVEPOINT PROTOCOL"
  # ... existing fields ...
  spoke_id: "savepoint"
  spoke_external_url: "https://savepoint.systems"
  hub_context: "Proof of Fidelity Preservation in distributed teams and context management at scale."
```

**Step 4: Update systemworks.html template to show spoke references**

Add this after the artifact metadata and before the "Read more" link (around line 696):

```html
{% if artifact.spoke_id %}
<div style="margin-top: 24px; padding: 16px; border-left: 4px solid #3A5F85; background-color: #F9F9F9;">
  <p style="font-size: 12px; letter-spacing: 0.05em; text-transform: uppercase; color: #2A2A2A; margin-bottom: 12px;">Standalone Spoke</p>
  <p style="font-size: 14px; line-height: 1.6;">{{ artifact.hub_context }}</p>
  <p style="margin-top: 12px;">
    <a href="{{ artifact.spoke_external_url }}" target="_blank" rel="noopener" style="font-size: 12px; letter-spacing: 0.05em; text-transform: uppercase;">Visit {{ artifact.spoke_id }} →</a>
  </p>
</div>
{% endif %}
```

**Step 5: Verify YAML validity**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && ruby -e "require 'yaml'; YAML.load_file('_data/index.yml')" && echo "YAML Valid"`

Expected: "YAML Valid"

**Step 6: Test build**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
bundle exec jekyll build --strict
grep -c "Standalone Spoke\|stress-test" _site/index.html
```

Expected: Output shows 2+ (spoke references appear).

**Step 7: Commit**

```bash
git add _data/holding_company.yml _data/index.yml _layouts/systemworks.html
git commit -m "arch: establish holding company hub-and-spokes structure

- Create _data/holding_company.yml documenting Hub/Spokes architecture
- Add spoke references to artifacts that have external projects
- Update template to display spoke context with links
- Implement 'Glass Box' principle on Hub while keeping Spokes opaque

This establishes the meta-layer structure:
- Hub (this site): Full transparency, reveals systems thinking
- Spokes (independent projects): Opaque, standalone, prove the thesis
- Bridge: Hub links to Spokes with architectural framing

The structure proves autonomy and asset generation, not just consulting.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 1: Rewrite Manifesto and Thesis

**Files:**
- Modify: `_data/index.yml` (manifesto section)

**Step 1: Read current manifesto**

Run: `grep -A 20 "manifesto:" _data/index.yml`

Expected: Current 8-paragraph manifesto about building durable systems.

**Step 2: Replace with strategic thesis**

Update the `manifesto.content` field in `_data/index.yml` to:

```yaml
manifesto:
  id: "00"
  title: "SYSTEMS FOR SOVEREIGNTY"
  content: |
    I build sovereign, high-fidelity systems. Not products. Not SaaS. Systems designed for the gap between chaos and control.

    Most innovation fails because of Fidelity Drift—the growing distance between strategy, design, and implementation. By the time a product ships, the original intention has been compromised by frameworks, dependencies, and architectural shortcuts.

    I work at the seam of Design, Engineering, and AI Infrastructure. I am a Luthier—I build bespoke instruments because standard tools lack the resolution required for deep work.

    My stack is intentionally idiosyncratic. Custom schemas. Local compute. Offline-first architecture. These choices are not over-engineering; they are Cognitive Ergonomics. They are built to scaffold the kind of rigor that prevents drift.

    This site is not a portfolio. It is documentation of how a sovereign systems architect thinks. It is proof that you can build resilience "in a vacuum," without corporate dependencies.

    What's here: Evidence of mastery. Underneath: Architecture. Beneath that: Philosophy.
```

**Step 3: Verify YAML syntax**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && ruby -e "require 'yaml'; YAML.load_file('_data/index.yml')" && echo "YAML Valid"`

Expected: "YAML Valid" message, no errors.

**Step 4: Commit**

```bash
git add _data/index.yml
git commit -m "refactor: rewrite manifesto to emphasize cognitive exoskeleton thesis

- Replace generic 'durable systems' framing with strategic positioning
- Introduce 'Fidelity Drift' as core problem statement
- Position author as 'Luthier' building bespoke instruments
- Explain idiosyncratic stack as intentional Cognitive Ergonomics
- Clarify site purpose: documentation of sovereign thinking, not portfolio

This establishes the thesis that underpins all projects and differentiates
the positioning from standard design systems architects.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Reframe Domains as Philosophical Pillars

**Files:**
- Modify: `_data/index.yml` (domains section, top-level structure)

**Step 1: Understand current domains**

Run: `grep -A 5 "domains:" _data/index.yml | head -20`

Expected: Three domains (INFRASTRUCTURE, METHODS, DESIGN).

**Step 2: Add domain descriptions to clarify philosophical intent**

Update each domain to clarify its role in the "Sovereignty" thesis:

```yaml
domains:
  - id: "01"
    name: "INFRASTRUCTURE"
    color: "blue"
    definition: "The Substrate. The Sovereign Stack. The Proof."
    description: "Mission-critical systems that survive without external dependencies. Platforms that maintain integrity across technological epochs. The operational proof that sovereignty is achievable at scale."
    artifacts:
      # (keep existing artifacts unchanged)

  - id: "02"
    name: "METHODS"
    color: "red"
    definition: "The Logic. The Protocols. The Discipline."
    description: "Systems designed to be operated. Frameworks that scale because they're built on clarity and constraint. Evidence that rigor is the antidote to chaos."
    artifacts:
      # (keep existing artifacts unchanged)

  - id: "03"
    name: "DESIGN"
    color: "green"
    definition: "The Semiotics. The Narrative. The Tangibility."
    description: "Visual systems that survive organizational pressure. Research into how forms persist through change. Proof that Taste is not subjective—it is a system of variables."
    artifacts:
      # (keep existing artifacts unchanged)
```

**Step 3: Verify YAML validity**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && ruby -e "require 'yaml'; YAML.load_file('_data/index.yml')" && echo "YAML Valid"`

Expected: "YAML Valid"

**Step 4: Commit**

```bash
git add _data/index.yml
git commit -m "refactor: reframe domains as philosophical pillars

- Update domain definitions to emphasize sovereignty, discipline, and rigor
- Clarify each domain's role in the 'Cognitive Exoskeleton' thesis
- Maintain all artifacts and technical content unchanged
- Position domains as evidence of mastery, not just project categories

Domains now communicate:
- INFRASTRUCTURE: Proof of sovereignty at scale
- METHODS: Evidence of discipline and rigor
- DESIGN: Demonstration that Taste is systematic

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Add Strategic Copy Section (Philosophy)

**Files:**
- Create: `_data/philosophy.yml`
- Modify: `_data/index.yml` (add reference to philosophy data)
- Modify: `_layouts/systemworks.html` (add philosophy section rendering)

**Step 1: Create philosophy data file**

Create `_data/philosophy.yml`:

```yaml
philosophy:
  sections:
    - id: "drift-control"
      title: "FIDELITY DRIFT: The Core Problem"
      content: |
        Most enterprises lose their original intent between strategy and execution. Slack erodes context. Jira obscures vision. Documentation rots.

        I use AI not to generate content, but to maintain cognitive context across massive datasets. Every system I build includes Drift Control: mechanisms to preserve fidelity from concept through implementation.

    - id: "sovereignty"
      title: "SOVEREIGNTY: Independence Over Convenience"
      content: |
        Renting infrastructure creates fragility. Cloud-dependent systems fail when connectivity breaks. SaaS platforms diverge from your actual needs.

        I build Offline-First architectures. Systems that work without the grid. This is not anachronistic; it is resilience.

    - id: "neuro-ergonomics"
      title: "NEURO-ERGONOMICS: Designing for Cognition"
      content: |
        Most interfaces are designed for mass adoption. They create noise to maximize engagement.

        I design for signal. Interfaces that reduce cognitive load. High information density without overwhelm. Tools that scaffold rather than distract.

    - id: "luthier"
      title: "THE LUTHIER MODEL: Building Custom Instruments"
      content: |
        A luthier doesn't build guitars with SaaS APIs and off-the-shelf electronics. They understand wood, acoustics, and the specific needs of the musician.

        I build software the same way. Custom schemas. Tailored constraints. Bespoke architectures.

        The complexity is not over-engineering. It is resolution.

  engagement:
    - title: "Who I Work With"
      content: |
        - Founders building Zero-to-One systems who need an architect that can scaffold culture and infrastructure simultaneously.
        - Complex Domain Leaders (BioTech, AI, Logistics, Infrastructure) who need interfaces that reduce risk and error.
        - R&D Labs that need to bridge Research Papers and Working Prototypes.

    - title: "My Constraints"
      content: |
        - I value Async & Deep Work over Always-On availability.
        - I prioritize System Integrity over Quick Hacks.
        - I work best when given Autonomy to solve the problem, not execute tickets.
        - I filter for leadership that respects the complexity of deep work.
```

**Step 2: Verify YAML validity**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && ruby -e "require 'yaml'; YAML.load_file('_data/philosophy.yml')" && echo "YAML Valid"`

Expected: "YAML Valid"

**Step 3: Update _layouts/systemworks.html to render philosophy section**

Add this section after the manifesto section and before the domains container (around line 657):

```html
<!-- Philosophy Section -->
{% if site.data.philosophy %}
<div class="philosophy-section">
  <h2 style="font-size: 32px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 48px; border-bottom: 2px solid #1A1A1A; padding-bottom: 24px;">THE PHILOSOPHY</h2>

  <div class="philosophy-subsections" style="display: grid; gap: 64px; max-width: 1000px; margin: 0 auto 96px;">
    {% for section in site.data.philosophy.sections %}
    <div class="philosophy-subsection" style="border-bottom: 1px solid #E5E5E0; padding-bottom: 48px;">
      <h3 style="font-size: 20px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;">{{ section.title }}</h3>
      <div style="font-size: 14px; line-height: 1.8; max-width: 900px;">
        {% for paragraph in section.content | split: "
" %}
          {% if paragraph != "" %}
            <p style="margin-bottom: 16px;">{{ paragraph }}</p>
          {% endif %}
        {% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>

  <!-- Engagement Section -->
  <div class="engagement-section" style="max-width: 1000px; margin: 0 auto; border-top: 2px solid #1A1A1A; padding-top: 48px;">
    <h2 style="font-size: 28px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 48px;">ENGAGEMENT MODELS</h2>

    {% for engagement in site.data.philosophy.engagement %}
    <div style="margin-bottom: 48px;">
      <h3 style="font-size: 16px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 16px;">{{ engagement.title }}</h3>
      <div style="font-size: 14px; line-height: 1.8; max-width: 900px;">
        {% for line in engagement.content | split: "
" %}
          {% if line != "" %}
            <p style="margin-bottom: 12px;">{{ line }}</p>
          {% endif %}
        {% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>
{% endif %}
```

**Step 4: Test template rendering**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
bundle exec jekyll build --strict
grep -c "FIDELITY DRIFT\|SOVEREIGNTY\|ENGAGEMENT MODELS" _site/index.html
```

Expected: Output shows 3 (each section appears once).

**Step 5: Commit**

```bash
git add _data/philosophy.yml _layouts/systemworks.html
git commit -m "feat: add philosophy section with strategic positioning

- Create _data/philosophy.yml with core concepts (Fidelity Drift, Sovereignty, etc.)
- Add Philosophy section rendering to systemworks.html
- Add Engagement Models section explaining who I work with and constraints
- Sections positioned between Manifesto and Domains

This transforms the site from project-focused to thesis-focused, establishing
the philosophical foundation that underpins all work.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Rewrite Project Descriptions as Case Studies

**Files:**
- Modify: `_data/index.yml` (all artifact descriptions)

**Step 1: Reframe each artifact in INFRASTRUCTURE domain**

Update artifacts in the INFRASTRUCTURE (01) domain:

**THE ENCORE PLATFORM:**
```yaml
- id: "1.1"
  title: "THE ENCORE PLATFORM"
  context: "Enterprise Architecture & Sovereignty"
  spec: "12 years. 99.9% uptime. 40,000+ users. Strangler pattern legacy modernization maintaining system fidelity across technological epochs."
  result: "Replaced the engine while the car drove at 60mph. Proof that you can maintain operational integrity while completely replacing core infrastructure. Systems that survived three technological epochs without drift."
  status: "DEPLOYED"
  link: "/evidence/the-encore-platform"
  case_study_focus: "Fidelity Preservation Under Pressure"
```

**VISUAL GOVERNANCE:**
```yaml
- id: "1.2"
  title: "VISUAL GOVERNANCE"
  context: "Identity Systems at Scale & Organizational Resilience"
  spec: "Luxury brands scaling across e-commerce, print, retail, campaigns, social. Constraint hierarchies enabling distributed teams to extend identity coherently."
  result: "$10M+ annual commerce. Visual coherence maintained through team transitions, market pressure, and organizational change. Proof that Taste is systematic, not decorative."
  status: "ACTIVE"
  link: "/evidence/visual-governance"
  case_study_focus: "Taste as Engineering Constraint"
```

**HOMELAB STACK:**
```yaml
- id: "1.3"
  title: "HOMELAB STACK"
  context: "Sovereign Infrastructure & Offline Autonomy"
  spec: "Offline-first server infrastructure. Ubuntu + Docker + custom monitoring. Self-hosted everything: media server, automation, backup. Physical data sovereignty."
  result: "Family media server, automated backups, AI compute, knowledge systems—all running on local hardware. Zero cloud dependencies. Proof of concept for truly sovereign infrastructure."
  status: "LIVE"
  case_study_focus: "Independence Over Convenience"
```

**Step 2: Reframe each artifact in METHODS domain**

**SAVEPOINT PROTOCOL:**
```yaml
- id: "2.1"
  title: "SAVEPOINT PROTOCOL"
  context: "Cognitive Versioning & Drift Control"
  spec: "Documented moments of stability. Syntax-enforced recovery. Weekly reviews, quarterly audits. Mechanism for maintaining epistemic fidelity across time."
  result: "Teams using Savepoint protocol recover 40% faster from context loss, make bolder architectural decisions, maintain institutional memory across team turnover."
  status: "V3.0 - Open Source"
  link: "/protocols/savepoint"
  case_study_focus: "Fidelity Preservation in Teams"
```

**ORDER OF THE ÆTHERWRIGHT:**
```yaml
- id: "2.2"
  title: "ORDER OF THE ÆTHERWRIGHT"
  context: "Systems Doctrine & Organizational Design"
  spec: "Three pillars: Clarity, Consistency, Coherence. Discipline for designing intangible systems that survive organizational pressure."
  result: "Framework for building systems that scale without drift. Used by early-stage founders and design leaders to architect culture and infrastructure simultaneously."
  status: "ACTIVE"
  link: "/protocols/order-of-the-aetherwright"
  case_study_focus: "Systems Survive When Built for Change"
```

**MODERNIST HOMESTEAD:**
```yaml
- id: "2.3"
  title: "MODERNIST HOMESTEAD"
  context: "Applied Constraints & Resilience"
  spec: "Zero-willpower meal systems. Italian and Thai supply chains for household resilience. Chemical constraints (Celiac + allergies) as design parameters."
  result: "Family that reliably feeds itself even when executive function is offline. Proof that rigorous constraints produce higher quality outcomes than willpower-dependent systems."
  status: "ACTIVE"
  link: "/labs/modernist-homestead"
  case_study_focus: "Constraints Drive Quality"
```

**Step 3: Reframe each artifact in DESIGN domain**

**NEW CITY:**
```yaml
- id: "3.1"
  title: "NEW CITY"
  context: "Narrative Simulation & Systems Under Pressure"
  spec: "40+ entity graph stress-testing infrastructure collapse. Modeling: What happens when systems fail? How do humans respond? What breaks first?"
  result: "Operational architecture expressed as interactive narrative. Research into how systems maintain integrity under pressure. Foundation for understanding resilience in design."
  status: "IN DEVELOPMENT"
  link: "/labs/new-city"
  case_study_focus: "Resilience is Designable"
```

**VISUAL SYSTEMS RESEARCH:**
```yaml
- id: "3.2"
  title: "VISUAL SYSTEMS RESEARCH"
  context: "Design Operations & Organizational Scaling"
  spec: "How visual systems survive team growth and organizational drift. Constraint hierarchies. Distributed autonomy. Typographic governance."
  result: "Framework for teams to extend design coherence without centralized control. Proof that 'Taste' can be systematized for scale."
  status: "ONGOING"
  link: "/labs/visual-systems"
  case_study_focus: "Taste Scales Through Constraints"
```

**MATH ON TAPE:**
```yaml
- id: "3.3"
  title: "MATH ON TAPE"
  context: "Tangible Cognition & Educational Design"
  spec: "Tactile mathematics. Making abstract concepts physically graspable through interaction. Converting symbolic representation into sensory experience."
  result: "Live environment used as primary teaching tool. Proof that understanding deepens when systems map to multiple cognitive channels."
  status: "LIVE"
  link: "/labs/math-on-tape"
  case_study_focus: "Cognition Through Design"
```

**Step 4: Verify YAML validity**

Run: `cd /home/peter/homelab/projects/active/petersalvato.com && ruby -e "require 'yaml'; YAML.load_file('_data/index.yml')" && echo "YAML Valid"`

Expected: "YAML Valid"

**Step 5: Test template rendering**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
bundle exec jekyll build --strict
grep -c "Fidelity Preservation\|Taste as Engineering Constraint\|Sovereign Infrastructure" _site/index.html
```

Expected: Output shows 3+ (case study focus language appears throughout).

**Step 6: Commit**

```bash
git add _data/index.yml
git commit -m "refactor: rewrite all artifacts as strategic case studies

- Reframe ENCORE PLATFORM as 'Fidelity Preservation Under Pressure'
- Reframe VISUAL GOVERNANCE as 'Taste as Engineering Constraint'
- Reframe HOMELAB STACK as 'Independence Over Convenience'
- Reframe SAVEPOINT PROTOCOL as 'Fidelity Preservation in Teams'
- Reframe ORDER OF THE ÆTHERWRIGHT as 'Systems Survive When Built for Change'
- Reframe MODERNIST HOMESTEAD as 'Constraints Drive Quality'
- Reframe NEW CITY as 'Resilience is Designable'
- Reframe VISUAL SYSTEMS RESEARCH as 'Taste Scales Through Constraints'
- Reframe MATH ON TAPE as 'Cognition Through Design'

Each artifact now includes:
- Strategic context focusing on thesis relevance
- Case study focus highlighting what the work proves
- Language emphasizing sovereignty, fidelity, and rigor

Projects become proof-of-concept for the Cognitive Exoskeleton thesis.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Update Site Metadata and Title

**Files:**
- Modify: `_config.yml`
- Modify: `_layouts/systemworks.html` (header)

**Step 1: Update site metadata**

Read current config and update:

```yaml
title: "Peter Salvato"
description: "Systems Architect for High-Fidelity Cognition. I build sovereign, resilient systems that treat complexity as a feature."
author: "Peter Salvato"
email: "peter@petersalvato.com"
```

**Step 2: Update header in _layouts/systemworks.html (line ~641)**

Change from:
```html
<p>Design Systems Architect | Operational Systems</p>
```

To:
```html
<p>Systems Architect for High-Fidelity Cognition</p>
```

**Step 3: Verify changes**

Run:
```bash
grep "description:" _config.yml
grep "Systems Architect for High-Fidelity Cognition" _layouts/systemworks.html
```

Expected: Both updated values appear.

**Step 4: Commit**

```bash
git add _config.yml _layouts/systemworks.html
git commit -m "refactor: update site title and positioning statement

- Update site description to emphasize sovereignty and high-fidelity cognition
- Change header from 'Design Systems Architect' to 'Systems Architect for High-Fidelity Cognition'
- Positioning now reflects the thesis-driven narrative

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Build, Verify, and Deploy

**Files:**
- Test: `_site/index.html` (generated output)

**Step 1: Clean build**

Run:
```bash
cd /home/peter/homelab/projects/active/petersalvato.com
rm -rf _site
bundle exec jekyll build --strict
```

Expected: "done in X seconds", no errors.

**Step 2: Verify all new sections render**

Run:
```bash
grep -c "SYSTEMS FOR SOVEREIGNTY\|FIDELITY DRIFT\|SOVEREIGNTY\|LUTHIER\|THE PHILOSOPHY" _site/index.html
```

Expected: Output shows 5+ (all new sections appear).

**Step 3: Verify case study language**

Run:
```bash
grep -c "Fidelity Preservation\|Taste as Engineering\|Sovereign Infrastructure\|Case Study" _site/index.html
```

Expected: Output shows 3+ (strategic language appears throughout).

**Step 4: Verify no broken references**

Run:
```bash
grep -i "undefined\|nil\|error" _site/index.html
```

Expected: No output.

**Step 5: Commit and push to deployment**

```bash
git add -A
git commit -m "build: complete narrative reposition refactor - cognitive exoskeleton thesis

Final Verification:
✓ Manifesto rewritten to emphasize Fidelity Drift and Sovereignty
✓ Domains reframed as philosophical pillars
✓ Philosophy section added with core concepts (Drift Control, Sovereignty, Neuro-Ergonomics, Luthier)
✓ All 9 artifacts rewritten as strategic case studies
✓ Site metadata and title updated to reflect high-fidelity positioning
✓ All strategic language integrated (Cognitive Exoskeleton, Epistemic Fidelity, etc.)

The site now communicates:
- This is not a portfolio; it is proof of sovereign thinking
- Complexity is intentional, not over-engineering
- The stack filters for autonomy-respecting leadership
- Each project demonstrates mastery in fidelity preservation

To maintain:
1. Edit _data/index.yml to add new case studies
2. Edit _data/philosophy.yml to evolve the thesis
3. Run 'jekyll build' to regenerate
4. Deploy

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"

git push origin main
```

Expected: Commits accepted, pushed to GitHub.

---

## Summary

This refactor transforms petersalvato.com from a project portfolio into a strategic positioning document. The key shifts:

| Before | After |
|--------|-------|
| "Design Systems Architect" | "Systems Architect for High-Fidelity Cognition" |
| Projects organized by domain | Projects positioned as case studies in sovereignty |
| Generic descriptions | Strategic focus: what each project proves |
| Information-heavy | Thesis-driven |
| "Here's what I built" | "Here's how I think. Here's why that matters." |

The site now filters for:
- Founders who need architects, not executors
- Leaders who respect complexity as a feature
- Organizations that value autonomy and fidelity over convenience

**All future content updates happen in YAML.** No HTML editing required. The structure is maintainable and extensible.
