# Process Archive Strategy

**Document Type:** Content Strategy & Template
**Phase:** 2, Week 1, Task 2.2
**Purpose:** Define what goes into each process archive, structure format, and content guidelines
**Status:** Ready for Checkpoint 2.1 Review

---

## Why Process Archives Exist

Process archives answer: **"How was this decision made? What constraints shaped it? What didn't work?"**

They serve practitioners who want to understand methodology, not just results. They show that systems work because they're built on accumulated thinking—not luck or intuition.

The archives are discoverable but secondary. Casual visitors focus on case studies. Builders and designers dig deeper.

---

## Format Decision

**Selected: Option C (Hybrid)**

Why hybrid works:
- **Scannable:** Key decisions visible immediately (bullet format)
- **Readable:** Context and explanation available below (narrative format)
- **Coherent:** Maintains Master Builder voice (direct, grounded, specific)
- **Accessible:** Works for quick scanning and deep reading

Structure:
1. Key decisions (bullets + 2-3 sentence explanation each)
2. What didn't work (narrative + resolution)
3. Technical architecture notes (bullets + explanation)
4. Constraints and how they shaped thinking (narrative)

---

## Content Specification

### Template Structure

```markdown
---
layout: process-archive
title: "PROJECT NAME - Process Archive"
project_url: "/path/to/case-study"
project_title: "PROJECT NAME"
---

## How This Was Built

This archive documents the thinking, decisions, and constraints behind PROJECT NAME.

### Key Decisions Made

**Decision 1:** [Decision statement]
- Why chosen: [1-2 sentences on reasoning]
- What considered: [Alternatives explored]
- What it solved: [The specific problem it addressed]

**Decision 2:** [Decision statement]
...

### What Didn't Work (and Why We Fixed It)

[Narrative explanation of experiments that failed]

**Experiment 1: [What was tried]**
- Why attempted: [The assumption]
- What happened: [The failure or discovery]
- How resolved: [The fix or pivot]
- What it taught us: [The insight that stuck]

**Experiment 2: [What was tried]**
...

### Technical Architecture Notes

**Platform choice:** [Why selected, what constraints shaped it]
- Technical trade-off: [A vs B and why A won]
- Scaling consideration: [What limits exist, how addressed]
- Integration point: [How systems talk to each other]

**Integration approach:** [How components talk]
...

### The Constraints That Shaped Everything

[Narrative: How specific constraints became the material for design]

**Constraint 1: [The limitation]**
- How it forced clarity: [Why this limitation was actually good]
- How it drove innovation: [What we did differently because of it]
- How it became a feature: [What we'd replicate if starting over]

**Constraint 2: [The limitation]**
...

### What We'd Do Differently

[1-2 paragraphs on retrospective thinking]
- If starting over, what would change?
- What principles held completely?
- What would adjust or be discarded?
- How did this inform other projects?
```

---

## Per-Project Content Specification

### 1. Savepoint Protocol - Process Archive

**Location:** `_process/savepoint-protocol.md`
**Project URL:** `/protocols/savepoint-protocol`
**Target Length:** 2000-2500 words
**Voice:** Direct, technical, grounded in neurodivergent workflow

**Key Decisions to Document:**
1. CLI-first approach (not GUI)
   - Why: Integrates into workflow, not separate tool
   - Alternatives: Electron app, web interface
   - Solved: Tool adoption and context switching

2. Semantic versioning for commits (not datetime)
   - Why: Version number is mnemonic, easier to recall
   - Alternatives: Timestamp-based, hash-based
   - Solved: Memory anchor for context recovery

3. JSON metadata layer (not free-form text)
   - Why: Machine-readable, queryable, structured
   - Alternatives: Markdown only, custom format
   - Solved: Automation and analysis

4. Single responsibility per savepoint (not bulk capture)
   - Why: Forces clarity, prevents dump files
   - Alternatives: Capture everything at once
   - Solved: Maintainability and retrieval speed

5. Off-platform storage (local files, not cloud)
   - Why: Control, speed, reliability
   - Alternatives: Cloud sync, proprietary
   - Solved: Dependency reduction

**What Didn't Work:**
- Early iteration: Storing screenshots alongside metadata (bloated files, slow sync)
- Early iteration: Automated context capture (tried to detect context automatically, failed regularly)
- Early iteration: Complex querying interface (too many options, paralyzed users)

**Technical Architecture:**
- Git-based storage with JSON metadata
- Shell commands wrapping underlying git operations
- Fallback mechanisms for context loss scenarios
- Integration points with existing CLI tools

**Constraints That Shaped Thinking:**
- Neurodivergent attention requires fast recovery, not robust prevention
- Reliability matters more than features
- Operator must understand the system (no magic)
- Must work when internet is unavailable

**Retrospective:**
Would we choose CLI again? Absolutely. Would we simplify the metadata structure? Yes. Would we build more visualization tools? Maybe, but only if they serve the primary use case.

---

### 2. Aiden-Jae - Process Archive

**Location:** `_process/aiden-jae.md`
**Project URL:** `/systems/aiden-jae`
**Target Length:** 2000-2500 words
**Voice:** Direct, technical, focused on handmade vs. mass-production constraint

**Key Decisions to Document:**
1. Photography-as-architecture approach (not decoration)
   - Why: Communication is structural, not cosmetic
   - Alternatives: Standard product photography, lifestyle shots
   - Solved: Authenticity and positioning proof

2. Aspect ratio variance (not grid uniformity)
   - Why: Each piece's visual weight dictates its frame
   - Alternatives: Forced square crops, fixed grid
   - Solved: Respect for craft and visual honesty

3. Custom Liquid templates (not Shopify themes)
   - Why: Standard themes assume volume, not craft
   - Alternatives: Premium themes, custom CSS hacks
   - Solved: Direct control over product presentation

4. Cost transparency in product pages (not hidden markup)
   - Why: Luxury through clarity, not scarcity
   - Alternatives: Aspirational pricing, heritage narrative
   - Solved: Positioning credibility

5. Material sourcing as first-class content (not footnote)
   - Why: Ethical position is structural advantage
   - Alternatives: Greenwashing footnotes, heritage story
   - Solved: Competitive differentiation and brand coherence

**What Didn't Work:**
- Early iteration: Lifestyle photography (contradicted authenticity positioning)
- Early iteration: Single photography grid (diminished craftsmanship visibility)
- Early iteration: Margin-based pricing (customers questioned markup immediately)
- Early iteration: Material sourcing in footer text (invisible to customers)

**Technical Architecture:**
- Shopify platform with custom Liquid templates
- SCSS architecture for responsive grid variance
- Image optimization for high-resolution detail photography
- Product metadata structure linking sourcing to pricing

**Constraints That Shaped Thinking:**
- Shopify as constraint: forced creativity within platform limitations
- DTC model: no retail markup, all positioning through website
- Handmade production: irregular supply, photography timing, inventory uncertainty
- Ethical sourcing: suppliers are partners, not just vendors

**Retrospective:**
The biggest insight: **Constraints became positioning.** We didn't apologize for irregular supply or longer production times. We made those part of the brand story. If we started over, we'd lean even harder into the constraint-as-feature model.

---

### 3. Order of the Aetherwright - Process Archive

**Location:** `_process/aetherwright.md`
**Project URL:** `/protocols/order-of-the-aetherwright`
**Target Length:** 2000-2500 words
**Voice:** Direct, systemic, focused on scale and coherence

**Key Decisions to Document:**
1. Symbolic governance (not procedural governance)
   - Why: Scales with trust, not enforcement
   - Alternatives: Rule-based systems, micromanagement protocols
   - Solved: Coherence without brittleness

2. Frames and Reels structure (not hierarchical org chart)
   - Why: Captures relationship between disciplines, not command chain
   - Alternatives: Traditional org, matrix org, flat org
   - Solved: Cross-functional clarity without silos

3. Story space mapping (not strategy documents)
   - Why: Visual, navigable, remixable
   - Alternatives: Text docs, wikis, presentations
   - Solved: Shared mental model and quick reference

4. Symbolic operating system metaphor (not framework)
   - Why: Familiar to builders, scalable, transferable
   - Alternatives: Business methodology, design system
   - Solved: Adoption and understanding

5. Documented evolution over static dogma
   - Why: Positioning is alive, not frozen
   - Alternatives: Locked brand guidelines, fixed positioning
   - Solved: Relevance and responsiveness

**What Didn't Work:**
- Early iteration: Too much symbolic language (confused stakeholders)
- Early iteration: Hierarchical frame relationships (contradicted intended coherence)
- Early iteration: Annual strategy documents (became outdated immediately)
- Early iteration: Specialist-only governance (excluded non-symbolic thinkers)

**Technical Architecture:**
- JSON structure for story space mapping
- Symbolic notation for frames and reels
- Version control for positioning evolution
- Documentation-as-code approach to governance

**Constraints That Shaped Thinking:**
- Multi-team projects: coherence requires shared language
- Brand evolution: positioning must change without breaking
- Scale: governance must survive delegation
- Complexity: thinking tools must be accessible, not arcane

**Retrospective:**
The symbolic approach works because it's *visual*. Teams can see the story space, not just read about it. We'd double down on visual governance. We might simplify some of the symbolic notation, but the core insight holds: governance is best when it's visual and navigable.

---

### 4. New City - Process Archive

**Location:** `_process/new-city.md`
**Project URL:** `/practice/new-city`
**Target Length:** 1500-2000 words
**Voice:** Reflective, experimental, focused on creative research

**Key Decisions to Document:**
1. Speculative worldbuilding (not product design)
   - Why: Frees thinking from market constraints
   - Alternatives: Commercial game design, portfolio piece
   - Solved: Permission to explore without commercial pressure

2. Modular city systems (not narrative-first design)
   - Why: Emerges from interaction, not predetermined story
   - Alternatives: Character-driven narrative, designer-authored story
   - Solved: Organic complexity and genuine discovery

3. Documentation-as-artifact (not documentation-as-explanation)
   - Why: The system itself is the research output
   - Alternatives: Finished game, design portfolio
   - Solved: Transparency and methodology visibility

4. Constraint-driven generation (not optimization)
   - Why: Constraints produce specific character
   - Alternatives: Maximum flexibility, player choice
   - Solved: Coherent aesthetic and emergent gameplay

5. Multi-platform thinking (not single platform)
   - Why: Constraints vary, solutions differ per platform
   - Alternatives: Platform-agnostic design, single reference
   - Solved: Adaptation and platform-specific depth

**What Didn't Work:**
- Early iteration: Story-first design (constrained emergent gameplay)
- Early iteration: Too many variables (system became opaque)
- Early iteration: Player choice as primary goal (produced incoherent outcomes)
- Early iteration: Single platform implementation (missed platform-specific insights)

**Technical Architecture:**
- Modular system design with clear dependencies
- Constraint propagation through system layers
- Documentation structure capturing decision rationale
- Multi-format output (playable, documented, speculative)

**Constraints That Shaped Thinking:**
- Speculative domain: freedom from market validation
- Research focus: methodology visibility matters more than polish
- Platform diversity: solutions must adapt, not generalize
- Artistic expression: emergence over authorship

**Retrospective:**
The biggest learning: **Constraints are creative fuel, not obstacles.** New City works because we started with specific constraints and let systems emerge. The documentation matters as much as the playable result. If we continued, we'd explore even more platforms and see what that constraint reveals.

---

### 5. Modernist Homestead - Process Archive

**Location:** `_process/modernist-homestead.md`
**Project URL:** `/systems/modernist-homestead`
**Target Length:** 2000-2500 words
**Voice:** Direct, domestic, focused on household operations

**Key Decisions to Document:**
1. Household as organizational unit (not nuclear family as constraint)
   - Why: Operations actually serve five different needs
   - Alternatives: One-size-fits-all system, family consensus
   - Solved: Autonomy within shared infrastructure

2. Physical infrastructure as communication (not hidden utility)
   - Why: Visible systems are auditable and teachable
   - Alternatives: Hidden complexity, magic black boxes
   - Solved: Family literacy and maintenance resilience

3. Automation by principle, not convenience
   - Why: Only automate decisions we've already made
   - Alternatives: Automate everything possible, no automation
   - Solved: Clarity and reducibility when systems fail

4. Local-first infrastructure (not cloud-dependent)
   - Why: Resilience and sovereignty matter more than convenience
   - Alternatives: All-cloud, hybrid cloud
   - Solved: Operational continuity and learning

5. Documentation as operational requirement (not nice-to-have)
   - Why: Family has multiple operators at different skill levels
   - Alternatives: Oral knowledge, specialized operators
   - Solved: Sustainability and knowledge transfer

**What Didn't Work:**
- Early iteration: Centralized automation (created single points of failure)
- Early iteration: Cloud-first (too dependent on external providers)
- Early iteration: Hidden complexity (family couldn't maintain or modify)
- Early iteration: Documentation after implementation (gaps emerged immediately)

**Technical Architecture:**
- Docker containerization for modularity
- Local storage with distributed backup
- Homelab compute for media, games, and data
- Documentation-first operations (CONVENTIONS.md as operational contract)

**Constraints That Shaped Thinking:**
- Neurodivergent household: systems must reduce cognitive load, not increase it
- Varying skill levels: everything must be learnable and maintainable
- Multiple use cases: storage, media, gaming, learning, productivity
- Reliability requirement: cannot depend on external providers

**Retrospective:**
The biggest insight: **Household infrastructure is a form of care work.** Systems that reduce friction for people with different abilities and attention patterns are sophisticated. The documentation isn't overhead—it's core infrastructure. We'd invest even more in making systems understandable and modifiable. Knowledge transfer is the actual product.

---

## Voice Guidelines for Process Archives

**Follow the Master Builder voice protocol throughout.** Key rules:

1. **Concrete before abstract**
   - Not: "We employed a paradigm shift in our approach"
   - Yes: "We switched from cloud-first to local-first because provider outages were blocking operations"

2. **Show the constraint**
   - Not: "We made a decision"
   - Yes: "Given that the household has 4 different users with different skill levels, we built documentation as operational requirement"

3. **Name the failure**
   - Not: "Early iterations required refinement"
   - Yes: "We tried lifestyle photography. It contradicted our positioning instantly. Customers saw it and immediately questioned the authenticity."

4. **Respect earned vocabulary**
   - Not: "Leveraging a paradigm shift in our ecosystem"
   - Yes: "We built symbolic governance because scale kills coherence without shared language"

5. **No performance language**
   - Not: "Boldly implemented," "Fearlessly pursued," "Passionately built"
   - Yes: "Implemented," "Chose," "Built"

---

## Length Guidelines

**Target per archive:** 1500-3000 words

**Breakdown:**
- Key Decisions Made: 300-500 words (5-8 decisions × 50-75 words each)
- What Didn't Work: 400-600 words (3-4 experiments × 100-150 words each)
- Technical Architecture: 300-500 words (3-5 technical decisions)
- Constraints and Thinking: 400-600 words (3-5 constraints × 80-120 words each)
- Retrospective: 200-300 words

**Why this length:**
- Respects reader time (read in 15-20 minutes)
- Provides enough detail to understand decisions
- Doesn't overwhelm with unnecessary depth
- Supports scanning and deep reading

---

## Visual/Layout Considerations

**Each process archive should:**
- Lead with short intro (2-3 sentences explaining the archive)
- Use clear section headings (H2 for major sections, H3 for subsections)
- Bullet format for quick-scanning decisions
- Short narrative paragraphs for explanations
- Bold text for key terms and decision names

**Example structure:**
```
## How This Was Built

Brief intro paragraph.

### Key Decisions Made

**Decision 1: [Short statement]**
- Sentence explaining why chosen
- Sentence on alternatives
- Result: What it solved

### What Didn't Work

**Experiment 1: [What was tried]**
Paragraph explaining the attempt, the failure, the resolution.

### Technical Architecture Notes

**Technical decision 1: [Statement]**
Explanation paragraph with technical detail.

### The Constraints That Shaped Everything

**Constraint 1: [The limitation]**
Narrative paragraph on how this constraint drove innovation.

### What We'd Do Differently

Closing retrospective paragraph.
```

---

## Creating Process Archives (Week 2 Implementation)

### Step 1: Research (1 hour per project)
- Review original case study
- Re-read project timeline in `/docs/extraction_timelines/`
- Review project notes and decision history
- Identify 5-8 key decisions

### Step 2: Outline (30 minutes per project)
- List key decisions
- Identify 3-4 failed experiments
- Note technical architecture points
- Identify 3-5 shaping constraints

### Step 3: Write (2-3 hours per project)
- Draft each section
- Use bullet format for decisions
- Use narrative for explanations
- Keep voice direct and grounded
- Read aloud to test voice consistency

### Step 4: Review (1 hour per project)
- Check for Master Builder voice violations
- Verify no jargon without earning
- Remove throat-clearing paragraphs
- Test readability at multiple speeds (scanning vs. deep reading)

---

## Integration with Case Study Pages

**Sidebar Widget (to be added to case study layouts):**

```html
<aside class="process-archive-link">
  <h3>How This Was Built</h3>
  <p>Interested in the decisions, failed experiments, and constraints behind this work?</p>
  <a href="/process-archives/{{ page.slug }}">Read the Process Archive</a>
</aside>
```

**Visual Treatment:**
- Subtle styling (reduced opacity, secondary color)
- Positioned below main article
- Not inline with main content
- Clear link to full archive

---

## Success Criteria - Process Archives

✓ 5 archives written (one per core case study)
✓ Each 1500-3000 words
✓ Each follows hybrid format (decisions + narrative)
✓ Each maintains Master Builder voice
✓ Each document key decisions, failures, constraints
✓ All archives discoverable via index page
✓ All case studies link to their archive
✓ Read-aloud test passes (voice consistent)
✓ No jargon without earning
✓ No marketing language or performance

---

## Template File

See end of document for blank template to copy for each project.

---

## BLANK TEMPLATE: Copy and customize per project

```markdown
---
layout: process-archive
title: "PROJECT_NAME - Process Archive"
project_url: "/path/to/case-study"
project_title: "PROJECT_NAME"
---

## How This Was Built

[2-3 sentence intro explaining what this archive documents]

### Key Decisions Made

**Decision 1: [Short statement of what was decided]**
- Why chosen: [1-2 sentences on reasoning and the problem it solved]
- What considered: [Alternatives explored or discarded]
- What it enabled: [What became possible because of this choice]

**Decision 2: [Short statement of what was decided]**
- Why chosen: [explanation]
- What considered: [alternatives]
- What it enabled: [result]

[Repeat for 5-8 decisions total]

### What Didn't Work (and Why We Fixed It)

**Experiment 1: [Brief description of what was attempted]**

[Narrative paragraph explaining the assumption, why we thought it would work, what actually happened, and how we resolved it. Include the insight that stuck.]

**Experiment 2: [Brief description of what was attempted]**

[Narrative paragraph explaining the attempt, the failure, the resolution, the lesson.]

[Repeat for 3-4 experiments total]

### Technical Architecture Notes

**[Technical component 1]: [Decision statement]**

[Paragraph explaining the technical choice, trade-offs considered, constraints that shaped it, how it integrates with other components]

**[Technical component 2]: [Decision statement]**

[Paragraph on technical choice and rationale]

[Repeat for 3-5 technical components]

### The Constraints That Shaped Everything

**Constraint 1: [The specific limitation or requirement]**

[Paragraph explaining how this constraint forced clarity, drove innovation, or became a feature. How would we replicate this in future work?]

**Constraint 2: [The specific limitation]**

[Paragraph on how the constraint shaped design and thinking]

[Repeat for 3-5 constraints total]

### What We'd Do Differently

[1-2 paragraph retrospective addressing:]
- If starting over, what would change?
- What principles held completely?
- What would be discarded?
- How did this inform other projects or future work?

---

*Process Archives maintain Master Builder voice: direct, concrete, grounded in actual decisions and constraints. See `/docs/voice-protocol.md` for guidelines.*
```

