# Narrative Architecture: petersalvato.com

## Master Narrative (The Through-Line)

**"I solve problems by deconstructing to first principles and rebuilding systems from scratch."**

Not crisis-driven. Not reactive. Intentional architecture. The site proves this works at every scale:
- When I design from scratch (Protocols)
- When I deploy under constraint (Applied Systems)
- When I research (Practice)

The visitor's journey: **Understand the methodology → See proof it works → Explore how it applies**

---

## Three Sub-Narratives (By Tier)

### Tier 01: PROTOCOLS
**"Here's what I designed from first principles."**

Each protocol is an original conception. Not a response to crisis. Deliberate architecture.

**The story each protocol tells:**
1. **The Conception** — What problem does this solve? Why did I design it this way?
2. **The Thinking** — What principles underlie the structure? Why this approach?
3. **The Architecture** — How is it actually built? What are the mechanisms?
4. **The Proof** — What does it prove about how systems work? What survives?

**What this proves:** First-principles thinking produces durable systems.

**Tier structure in JSON:**
```
- collectionCopy: "These aren't theories..."
- collectionTemplate: How to render /protocols/ landing
- artifacts: Each protocol as a complete system design
```

---

### Tier 02: APPLIED SYSTEMS
**"Here's proof the methodology works everywhere."**

This tier shows the methodology in action:
- **Original builds** (Aiden-Jae, Everyday Gold, Modernist Homestead) — Proof from-scratch design holds
- **Enterprise scale** (Encore, 12 years, 99.9% uptime) — Proof it works long-term, under load
- **Client rebrand** (Altrueism) — Proof it works reconceiving broken systems

The story is: **Same methodology, different constraints. Works every time.**

**Each artifact tells:**
1. **The Constraint** — What problem did the client/context present?
2. **The Reconception** — How did I deconstruct and rebuild?
3. **The Implementation** — What's the actual system?
4. **The Proof** — What does this prove about the methodology?

**What this proves:** The methodology is universally applicable. Works at scale. Works on rebrands. Works on originals.

**Tier structure in JSON:**
```
- collectionCopy: "A system is only valid at scale..."
- collectionTemplate: How to render /systems/ landing
- artifacts: Each system as proof of methodology
  - Encore: proves scale + longevity
  - Altrueism: proves methodology works on rebrands
  - Aiden-Jae, Everyday Gold, etc: prove original builds
```

---

### Tier 03: PRACTICE
**"Here's where I research and stress-test the principles."**

Not finished work. Active exploration. Lower stakes. But testing whether the principles hold.

**The story each practice project tells:**
1. **The Question** — What principle am I exploring?
2. **The Experiment** — How am I testing it?
3. **The Learning** — What's the system revealing?
4. **The Recursion** — How does this inform the protocols?

**What this proves:** The principles are portable. They work across domains (narrative, music, photography, game design, typography).

**Tier structure in JSON:**
```
- collectionCopy: "These are laboratories..."
- collectionTemplate: How to render /practice/ landing
- artifacts: Each project as active research
  - New City: narrative systems at scale
  - MathOnTape: systems thinking applied to music
  - Photogeography: format as constraint
  - Echo & Bone: archetypal systems
  - etc.
- colophon: Meta-documentation of the methodology
```

---

## Micro-Narrative (Individual Artifact Arc)

Every artifact follows this narrative structure:

### For Protocols:
1. **Problem/Conception** — "Here's the gap I saw. Here's what I designed."
2. **Thinking** — "Here's why this structure. Here's the principles."
3. **Structure** — "Here's how it's built. Here's the mechanism."
4. **Proof** — "Here's what it proves. Here's what survived."

### For Applied Systems:
1. **Constraint/Context** — "Here's what needed solving."
2. **Reconception** — "Here's how I deconstructed and rebuilt."
3. **Implementation** — "Here's the actual system."
4. **Proof** — "Here's what this proves about the methodology."

### For Practice:
1. **Question** — "What am I exploring?"
2. **Experiment** — "How am I testing it?"
3. **Learning** — "What's emerging?"
4. **Recursion** — "How does this feed back?"

---

## Story Recursion (How They Nest)

```
Main Narrative: "I solve problems through first-principles design"
  ↓
Sub-Narratives (three tiers):
  ├─ Protocols: "Here's what I conceived from scratch"
  ├─ Applied Systems: "Here's proof it works everywhere"
  └─ Practice: "Here's where I research the principles"
    ↓
Micro-Narratives (within each tier):
  ├─ Tier landing page: "Here's what this tier proves"
  └─ Each artifact: "Here's the story of this specific system"
    ↓
Sub-Sub-Narratives (within each artifact):
  ├─ Problem/Conception/Question
  ├─ Thinking/Experiment
  ├─ Structure/Implementation/Learning
  └─ Proof/Recursion
```

Each level tells a complete story. Each level also serves the larger story.

---

## Information Architecture (What This Means for JSON)

The JSON structure must support this narrative cascade:

```json
{
  "protocols": {
    "collectionCopy": {
      "tier_story": "What does this tier prove?",
      "tier_narrative": "How does this tier serve the main narrative?"
    },
    "collectionTemplate": "How to render tier landing",
    "artifacts": {
      "Template": {
        "sections": ["problem", "thinking", "structure", "proof"],
        "narrative_arc": "How each section tells the story"
      },
      "Savepoint Protocol": {
        "conception": "What I designed from scratch",
        "summary": "Card copy for tier landing",
        "sections": {
          "problem": "The conception — what gap I saw",
          "thinking": "Why this structure",
          "structure": "How it's built",
          "proof": "What it proves"
        }
      }
    }
  }
}
```

---

## UX Implications (How Users Navigate the Story)

### Entry Point (Homepage)
User sees: **"I solve problems by redesigning systems from first principles."**
Action: Choose to explore Protocols, Systems, Practice, or About

### Tier Landing (/protocols/, /systems/, /practice/)
User sees:
- Tier story ("What does this tier prove?")
- Cards for each artifact (summary + image)
- Clear sense of how this tier serves the main narrative

### Artifact Page (/protocols/savepoint-protocol/)
User reads:
- Problem/Conception → Thinking → Structure → Proof
- Arc tells the story of how this system came to be
- Understands both the specific system AND how it proves the methodology

### About Pages (/about/provenance/, /about/three-systems/)
User understands:
- The narrative architecture of the entire site
- How the site documents its own design thinking
- How first-principles thinking applies to the site itself

---

## Colophon Documentation (What Gets Explained)

The Colophon should explain:

1. **The Main Narrative** — "This site tells one story through three sub-stories"
2. **The Tier Structure** — "Each tier proves something different about the methodology"
3. **The Artifact Arc** — "Each project follows problem → thinking → structure → proof"
4. **The Recursion** — "The site documents how it was designed, which is part of the design"
5. **The Information Architecture** — "Why the site is organized this way"
6. **The Voice** — "Why everything is written in first-principles language"

The Colophon becomes **meta-documentation**: It explains the site's narrative structure, which demonstrates the site's design thinking in action.

---

## Master Builder Voice Application

Every section, at every level, should:
- **Lead with the conception, not the crisis**
- **Show the thinking first, then the proof**
- **Use concrete specifics, not abstract theory**
- **Sound like a person explaining their work, not a brand communicating**
- **Treat constraints as design material, not problems**

This voice reinforces the main narrative: deliberate design, first-principles thinking, proven methodology.

---

## Summary: What This Architecture Enables

1. **Clear storytelling** — Visitors understand what you do and why at every level
2. **Proof portfolio** — Each tier proves something specific about the methodology
3. **Narrative coherence** — Micro-stories serve sub-stories serve main story
4. **Self-documentation** — The Colophon explains the site's own design thinking
5. **AI-ready** — Structure enables context-aware content delivery
6. **Recursive design** — The site demonstrates its own principles through its structure

---

**This is the architecture. Everything else (JSON structure, templates, copy, UX) flows from this.**
