---
layout: process-archive
title: "Aiden-Jae - Process Archive"
project: "aiden-jae"
permalink: /process-archives/aiden-jae/
---

## How This Was Built

Aiden-Jae is a luxury jewelry brand built on a constraint most brands apologize for: handmade production means inconsistent supply, irregular inventory, and visible imperfection. We didn't hide that constraint. We made it the positioning.

The insight was structural: luxury through transparency. Show the cost breakdown. Explain the design process. Narrate where materials come from. Let customers see exactly why this piece costs this much. That's actually luxurious—not scarcity mythology, but earned understanding.

### Key Decisions Made

**Transparency over aspiration**

- Why chosen: Every luxury brand tells aspirational stories—heritage, exclusivity, mythology. These feel hollow for handmade work. What's actually valuable about handmade is that you can see the thinking. Show that instead of hiding it.
- What considered: Heritage narrative, exclusive positioning, lifestyle marketing
- What it enabled: Positioning that's defensible and coherent. Customers who understand the brand become advocates. They're not buying fantasy—they're buying clarity.

**Material sourcing as first-class content**

- Why chosen: Ethical position isn't a footnote—it's structural to the brand. Show suppliers, explain material choices, narrate the sourcing story. Make it impossible to separate "the brand" from "how it's made."
- What considered: Greenwashing footnotes, hidden complexity, standard product descriptions
- What it solved: Competitive moat. Competitors can copy design, but they can't copy integrated sourcing narrative without completely changing their infrastructure.

**Photography as architecture, not decoration**

- Why chosen: Photography is the primary communication for jewelry. If you're claiming transparency, the photography has to *show* something real. Material texture, actual imperfections, honest light. Not stylized fantasy.
- What considered: Lifestyle photography, professional studio setups, aspirational imagery
- What it enabled: Authentication through visual honesty. Customers see the actual piece. They see material quality. They see care in craft. The photography does the transparency work.

**Custom e-commerce over premium theme**

- Why chosen: Off-the-shelf themes assume volume production. They're built for: click, add to cart, checkout. They hide process. We needed the platform itself to tell the story—each product page as a case study, not a transaction.
- What considered: Premium Shopify theme, custom CSS hacks, standard template with overwrites
- What it solved: Direct control over narrative structure. The platform became part of the brand experience, not separate from it.

**Cost transparency in pricing display**

- Why chosen: Luxury brands hide markup through aspirational pricing. We displayed actual costs: materials, time, overhead, margin. Let customers see exactly what they're paying for.
- What considered: Margin-based pricing, aspiration-based pricing, competitive pricing
- What it enabled: Trust. Customers who see honest cost breakdown don't question the price. They understand it. They defend it to skeptics.

**Aspect ratio variance in product photography grid**

- Why chosen: Every piece has different proportions. Forcing them into uniform squares diminishes visual weight. Use the aspect ratio that respects each piece's form. A long strand looks different from a compact form.
- What considered: Uniform grid, consistent square crops, standard layout
- What it solved: Visual honesty. Each piece gets the frame it deserves. This also signals "we're not templating our work"—each piece is specific.

### What Didn't Work (and Why We Fixed It)

**Early iteration: Lifestyle photography**

We shot pieces being worn—on skin, in contexts, showing lifestyle aspiration. The market response was immediate: customers didn't trust it. The aspirational imagery contradicted our transparency positioning.

People saw the lifestyle shot and thought: "Are you selling the piece or the fantasy of being the person wearing it?" The messaging was split. We were claiming transparency while showing mythology.

How we fixed it: Removed all lifestyle photography. Shoot only: the piece alone, detail photography showing craftsmanship, material closeups. Let the piece stand on its own merit.

The insight that stuck: Coherence beats polish. Mixed messaging loses customer trust faster than simple honesty.

**Early iteration: Single photography grid**

We tried to show all products in a uniform grid—same size, same layout. It looked professional. It looked like nothing.

What happened: The craftsmanship became invisible. All pieces looked equivalent in size and importance. A delicate strand looked as substantial as a cuff. We lost the visual information that actually mattered.

How we fixed it: Variable grid with aspect-ratio photography. Let visual weight dictate frame size. A thin strand gets a tall crop. A broad piece gets width. This required custom CSS, but it communicated craftsmanship.

The insight that stuck: Template solutions hide the work. Craft requires irregular, specific treatment.

**Early iteration: Margin-based pricing**

We calculated cost plus margin (standard retail math: 300% markup). Then we displayed only the final price.

What happened: Customers questioned the markup. Without seeing the cost breakdown, premium pricing felt arbitrary. We looked like we were playing scarcity games.

How we fixed it: Show material cost, time cost (number of hours at rate), overhead allocation, margin. Let customers see the actual economics.

At that point, customers either understood the price or they didn't—but they understood it for *rational* reasons, not emotional ones. This built trust.

The insight that stuck: Transparency doesn't reduce prices, but it validates them.

**Early iteration: Material sourcing in footer text**

We tried to include sourcing information in the footer or product descriptions. Standard placement. It was invisible.

What happened: Customers didn't know materials were ethically sourced. We had the story, but nobody read it.

How we fixed it: Made sourcing a design element—visual prominence on product pages, narrative integration into the page structure, supplier names and stories as content, not afterthought.

The insight that stuck: If it's not visible in the design system, it doesn't exist. Design enforcement is stronger than editorial guidelines.

### Technical Architecture Notes

**Shopify with custom Liquid templates**

Shopify gives you product management, payments, shipping. But standard Shopify assumes you're selling volume. We built custom Liquid templates that turned product pages into narrative-focused experiences.

Each product page isn't a listing—it's a case study: Here's the piece. Here's why it's designed this way. Here's who made it. Here's what it costs and why. Here's the material story.

Trade-off: Custom templates mean you lose automatic Shopify theme updates. You own the maintenance burden. But that's acceptable because the narrative structure is non-negotiable.

**SCSS architecture for responsive variant photography**

We built CSS that handles variable aspect ratios in the product grid. Instead of forcing uniform crops, CSS media queries determine grid column counts and aspect ratios based on device width.

Scaling consideration: Works until you have 200+ products. Then grid performance becomes an issue. Solution: Pagination by collection, lazy loading, or moving to a custom platform. For handmade jewelry (limited inventory), this isn't a problem yet.

**Image optimization for detail photography**

Product photography is high-resolution (2400px+) to show material texture. This requires aggressive optimization: WebP conversion, responsive sizes, lazy loading.

Every product page loads 6-8 high-res images. Without optimization, page weight becomes untenable. With optimization (WebP + srcset), we serve ~300KB for full product photography vs. 1.2MB unoptimized.

**Product metadata structure linking sourcing to pricing**

Behind the scenes: JSON metadata on each product ties together material sourcing, cost breakdown, designer notes, and production time. This metadata feeds the front-end template logic.

A single metadata edit cascades: update material, the cost breakdown recalculates, the sourcing story updates, the page layout adjusts. One source of truth.

### The Constraints That Shaped Everything

**Handmade production as forcing constraint**

Handmade means: supply is irregular, production time is unpredictable, visual imperfection is inevitable. Most brands see this as a problem to hide. We saw it as positioning.

The constraint forced a decision: either compete on consistency (and lose because we can't), or compete on authenticity (and win because we can't fake it). We chose authenticity.

This constraint became structural to everything—the photography style, the transparency messaging, the cost breakdown, the material narrative. We stopped fighting the constraint and built it into the brand identity.

**DTC model with no retail markup**

Direct-to-consumer means no wholesale margin, no distributor cut. The brand carries all economics. This means pricing has to be honest—there's nowhere to hide cost.

Competitors using wholesale have room for margin opacity. We don't. So we leaned into transparency. "Here's why it costs this much" becomes a competitive advantage when it's the truth.

**Ethical sourcing as non-negotiable**

We work with specific suppliers we trust and respect. This isn't a marketing angle—it's an operational requirement. We can't work with everyone; we work with people we can collaborate with.

This constraint cascaded: limited suppliers means limited material options. Limited materials means specific design aesthetic. That aesthetic becomes the brand visual language.

The constraint forced coherence at every level—from supplier relationship to design language to customer positioning.

**Shopify platform as design container**

Shopify's limitations became creative pressure. You can't do custom checkout flows. You can't hide payments behind a portal. Standard features govern what's possible.

Instead of fighting the platform, we designed within it. Custom Liquid lets us do what matters (narrative-focused product pages) while accepting what we can't change (payment systems, shipping calculations).

The constraint: work within the platform, or rebuild everything custom. We chose the former. This meant accepting some limitations while maximizing narrative control where it matters.

### What We'd Do Differently

If we restarted, the core principle would hold: transparency as structural advantage. But implementation adjustments:

The photography investment was enormous. We'd invest even more—quality over quantity. Ten exquisitely documented pieces are more powerful than fifty mediocre ones. We learned this late.

The sourcing story evolved significantly. We'd map that out *before* building the brand—supplier partnerships, material narratives, cost structure. Then build everything else around it. We reverse-engineered this, which created friction.

The custom Liquid approach was right, but we'd invest more in template sophistication earlier. Pagination, filtering, collection-level storytelling—these became obvious needs that we added reactively instead of building initially.

Most importantly: Scale awareness. Handmade at volume becomes different from handmade at small scale. We'd decide: are we scaling production (and accepting loss of specificity) or maintaining craft (and accepting volume limits)? That decision cascades everywhere.

The principle that held: **Constraints are positioning.** Every limitation that we stopped fighting and instead built into the brand became a strength. The brands that fail are the ones trying to copy handmade story while operating at mass-production volume. Coherence between constraint and narrative is unbreakable.

What this taught us: Positioning isn't something you layer on top of operations. It *is* your operations made visible. If there's a gap between what you claim and how you work, customers see it immediately.

---

*Process Archive for Aiden-Jae. See case study at `/systems/aiden-jae` for project overview.*
