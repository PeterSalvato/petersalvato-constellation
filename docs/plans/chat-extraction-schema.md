# Chat Export Schema and Semantic Indexing Strategy

## Overview

This schema defines how three heterogeneous chat export platforms (Gemini, ChatGPT, Claude) are normalized into a unified structure, then semantically indexed by project mention, enabling chronological reconstruction of project evolution across all platforms.

**Source of Truth:** Chat exports are the authoritative record of project thinking and development.

---

## Part 1: Normalized Schema

### Common Fields

All chats, regardless of source platform, normalize to these core fields:

```json
{
  "id": "platform-specific-unique-id",
  "timestamp": "ISO-8601 formatted datetime",
  "title": "user-provided subject or conversation topic",
  "content": "plain text body of conversation",
  "platform": "gemini | chatgpt | claude",
  "raw_export": {
    "original": "platform-native structure preserved for validation"
  }
}
```

#### Field Definitions

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `id` | string | Yes | Platform-specific unique ID (varies by source format) |
| `timestamp` | ISO-8601 | Yes | Consistent format across all platforms for chronological sorting |
| `title` | string | Yes | Chat title, conversation subject, or user's initial prompt |
| `content` | string | Yes | Plain text of full conversation (HTML/formatting stripped) |
| `platform` | enum | Yes | Must be one of: `gemini`, `chatgpt`, `claude` |
| `raw_export` | object | Yes | Unmodified platform export (enables format validation) |

### Semantic Indexing Fields (Added During Processing)

```json
{
  "detected_projects": {
    "project-id": {
      "confidence": "high | medium",
      "matched_patterns": ["pattern1", "pattern2"],
      "section_references": [
        {
          "content_snippet": "text excerpt containing mention",
          "character_position": 1234
        }
      ]
    }
  },
  "semantic_keywords": [
    "keyword1",
    "keyword2"
  ]
}
```

---

## Part 2: Platform-Specific Handling

### Gemini Exports

**Source:** `/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json`

**Native Structure:**
```json
{
  "title": "User's chat subject",
  "time": "2026-01-26T13:04:42.022Z",
  "safeHtmlItem": [
    {
      "html": "<p>HTML-formatted conversation content</p>"
    }
  ]
}
```

**Extraction Rules:**
1. **Title:** Use `title` field directly
2. **Timestamp:** Map `time` to ISO-8601 (usually already compliant)
3. **Content:**
   - Extract HTML from `safeHtmlItem[0].html`
   - Strip all HTML tags using HTMLParser
   - Preserve text content and whitespace structure
   - Handle edge case: empty or missing `safeHtmlItem` → content is empty string
4. **ID:** Hash of title + timestamp (no native unique ID)

**Gemini-Specific Challenges:**
- HTML formatting requires conversion to plain text
- Some conversations may have multiple `safeHtmlItem` entries (use first only)
- Time format is already ISO-8601, no conversion needed
- No native conversation ID; use deterministic hash

### ChatGPT Exports

**Source:** `/home/peter/homelab/knowledge/exports/data-2026-01-26-15-50-54-batch-0000/conversations.json` (20.5MB)

**Expected Structure (subject to verification):**
- Likely array of conversations
- Each with unique `id` field
- Title/subject field
- Timestamp (Unix epoch or ISO-8601)
- Message array with role + content structure

**Extraction Rules (To Be Refined After File Inspection):**
1. **Title:** Extract from conversation title field
2. **Timestamp:** Convert from platform format to ISO-8601
3. **Content:**
   - Concatenate all messages (role: "user" + role: "assistant")
   - Format as plain text, preserving turn structure
   - Strip markdown formatting or preserve for semantic clarity (TBD)
4. **ID:** Use ChatGPT's native conversation ID

**ChatGPT-Specific Challenges:**
- Large file (20.5MB) may require streaming parse
- Timestamp format verification needed
- Message structure validation needed

### Claude Exports

**Source:** `/home/peter/homelab/knowledge/exports/7bb7d7448a4fe8b37c10d84958a3011b01d3dc5d3b4a88cb8a89ceea3ebda027-2026-01-22-18-47-51-f068f48a77d44e359188dc77169ae29d/conversations.json`

**Expected Structure (subject to verification):**
- Likely array of conversations
- Each with unique `id` field
- Title/subject field
- Timestamp (Unix epoch or ISO-8601)
- Message array with role + content structure

**Extraction Rules (To Be Refined After File Inspection):**
1. **Title:** Extract from conversation title field
2. **Timestamp:** Convert from platform format to ISO-8601
3. **Content:**
   - Concatenate all messages (role: "user" + role: "assistant")
   - Preserve structure, strip markdown if needed
   - Handle code blocks appropriately
4. **ID:** Use Claude's native conversation ID

**Claude-Specific Challenges:**
- Message structure validation needed
- Timestamp format verification needed

---

## Part 3: Semantic Matching Strategy

The system identifies which projects are mentioned in each chat using a two-tier confidence system, grounded in the manifest (`/home/peter/homelab/projects/active/petersalvato.com/docs/mainfest.json`).

### High Confidence Matching

**Rule:** Exact mentions of project names, IDs, or defining characteristics from the manifest.

High confidence rules use exact-match patterns derived directly from manifest data.

**Project Definitions (High Confidence Patterns):**

#### Tier 1: Protocols
1. **Savepoint Protocol** (`savepoint-protocol`)
   - Exact patterns: "Savepoint", "savepoint"
   - Characteristics: "semantic turning point", "realization clicked", "cognitive inflection", "authorship infrastructure"

2. **Order of the Ætherwright** (`order-of-the-aetherwright`)
   - Exact patterns: "Aetherwright", "Ætherwright", "æ", "Order of the"
   - Characteristics: "sovereign cognition", "ritual framework", "symbolic operating system", "aligning tools and thoughts"

3. **AI DevOps Workbench** (`ai-devops-workbench`)
   - Exact patterns: "AI DevOps", "DevOps Workbench", "vibecoding"
   - Characteristics: "architectural decisions", "institutional memory", "conventions", "symbol-index", "drift detection"

4. **Portable Agency** (`portable-agency`)
   - Exact patterns: "Portable Agency", "self-discovering specialists", "Project Manager", "Tech Lead"
   - Characteristics: "automatic verification", "project health", "npm lint", "technology detection"

#### Tier 2: Applied Systems
1. **Encore** (`encore`)
   - Exact patterns: "Encore"
   - Characteristics: "enterprise platform", "Windows Forms to web", "40,000 users", "99.9% uptime", "12 years"

2. **Aiden Jae** (`aiden-jae`)
   - Exact patterns: "Aiden Jae", "Aiden-Jae"
   - Characteristics: "luxury jewelry", "tropical", "South Florida", "organic", "Shopify"

3. **Altrueism** (`altrueism`)
   - Exact patterns: "Altrueism"
   - Characteristics: "brand remediation", "artisanal", "apparel", "handcrafted"

4. **Everyday Gold** (`everyday-gold`)
   - Exact patterns: "Everyday Gold"
   - Characteristics: "natural deodorant", "Aiden Jae", "packaging"

5. **Modernist Homestead** (`modernist-homestead`)
   - Exact patterns: "Modernist Homestead"
   - Characteristics: "neurodivergent", "modernist cooking", "hydroponics", "horticulture", "home lab"

#### Tier 3: Practice
1. **MathOnTape** (`mathontape`)
   - Exact patterns: "MathOnTape", "Math On Tape"
   - Characteristics: "electronic music", "cassette", "dot matrix", "retro-futuristic"

2. **Photogeography** (`photogeography`)
   - Exact patterns: "Photogeography"
   - Characteristics: "poster series", "grid system", "coordinates", "location data", "QR code"

3. **Echo & Bone** (`echo-and-bone`)
   - Exact patterns: "Echo & Bone", "Echo and Bone"
   - Characteristics: "poster series", "Stoic", "philosophy", "engraving", "black letter typography"

4. **Versagrams** (`versagrams`)
   - Exact patterns: "Versagrams"
   - Characteristics: "poster series", "lyrics", "AI artwork", "grid system"

5. **The Deep Cuts** (`the-deep-cuts`)
   - Exact patterns: "The Deep Cuts", "Deep Cuts"
   - Characteristics: "DJ methodology", "music appreciation", "book concept"

6. **New City** (`new-city`)
   - Exact patterns: "New City"
   - Characteristics: "narrative", "marketing", "complex project"

7. **Cryptozoology** (`cryptozoology`)
   - Exact patterns: "Cryptozoology"

8. **Monstrum** (`monstrum`)
   - Exact patterns: "Monstrum"

9. **Motorology** (`motorology`)
   - Exact patterns: "Motorology"

**Implementation:**
```regex
# Example: Match "Savepoint" variants (case-insensitive)
(?i)\bsavepoint\b

# Example: Match "Aetherwright" + variants (case-insensitive)
(?i)\b(?:ætherwright|aetherwright|æ)\b

# Example: Match "Encore" (case-insensitive, word boundary)
(?i)\bencore\b
```

### Medium Confidence Matching

**Rule:** Semantic keywords and thematic patterns that suggest project relevance without explicit name mention.

Medium confidence rules capture thematic language unique to each project.

**Thematic Keywords (Medium Confidence Patterns):**

| Project | Keywords | Pattern Context |
|---------|----------|-----------------|
| savepoint-protocol | "turning point", "realization", "inflection", "cognitive shift", "thinking changed", "clicked" | Moments where understanding shifted |
| order-of-the-aetherwright | "ritual", "intention", "sovereignty", "symbolic", "cognitive firmware", "tool alignment" | Intentional practice and symbolic systems |
| ai-devops-workbench | "architectural decision", "institutional memory", "drift", "conventions", "fragile code" | System memory and decision tracking |
| portable-agency | "specialist", "verification", "self-discovering", "automatic", "tool detection" | Autonomous agents with built-in verification |
| encore | "enterprise", "stewardship", "platform", "migration", "durability", "scale" | Long-term system maintenance |
| aiden-jae | "jewelry", "luxury", "organic", "tropical", "brand system", "coherence" | Integrated brand systems |
| altrueism | "brand remediation", "transition", "artisanal", "intentionality" | Brand transformation |
| everyday-gold | "deodorant", "natural", "branding", "packaging", "umbrella" | Product branding |
| modernist-homestead | "neurodivergent", "scaffolding", "system", "homestead", "kitchen", "garden", "hydroponics" | Personal operating systems |
| mathontape | "music", "electronic", "cassette", "retro", "dot matrix", "aesthetic" | Musical branding |
| photogeography | "poster", "grid", "location", "coordinates", "metadata", "spatial" | Spatial information systems |
| echo-and-bone | "poster", "stoic", "philosophy", "typography", "engraving", "grid", "meaning" | Philosophical visual systems |
| versagrams | "poster", "lyrics", "AI art", "constraint", "coherence", "grid" | Constraint-based creative systems |

**Implementation:**
```regex
# Example: Medium confidence for Savepoint
(?i)(turning\s+point|realization\s+clicked|thinking\s+changed|inflection)

# Example: Medium confidence for Aetherwright
(?i)(ritual|symbolic\s+operating|sovereignty|tool\s+alignment)

# Example: Medium confidence for Encore
(?i)(enterprise\s+platform|40,?000\s+users|durability|stewardship)
```

### Confidence Scoring

**High Confidence → Confidence Score: 0.95**
- Exact project name match
- Manifest-defined characteristic mentions
- Direct project ID reference

**Medium Confidence → Confidence Score: 0.60**
- Thematic keywords present but no direct name
- Contextual language consistent with project mission
- Multiple medium-confidence signals can increase to 0.75

**Ambiguous (Flagged for Manual Review) → Confidence Score: < 0.60**
- Generic terminology ("system", "tool", "platform") without specificity
- Keywords that apply to multiple projects
- Unclear reference requiring context reading

---

## Part 4: Extraction Process

### Step 1: Load and Normalize

For each platform:
1. Parse JSON export
2. Extract core fields (id, timestamp, title, content)
3. Apply platform-specific transformations (HTML stripping, timestamp conversion)
4. Normalize to common schema
5. Preserve raw_export for validation

### Step 2: Semantic Indexing

For each normalized chat:
1. Combine title + content into searchable text
2. Apply high confidence regex patterns
3. Record matched patterns and position references
4. Apply medium confidence patterns
5. Calculate confidence scores
6. Flag ambiguous references

### Step 3: Chronological Sorting

For all indexed chats:
1. Extract timestamp
2. Sort by ISO-8601 timestamp (ascending)
3. Group by detected project
4. Build project-specific timelines

### Step 4: Ambiguity Flagging

Chats are flagged for manual review if:
- No projects detected (true negative or missed pattern?)
- Multiple equally confident projects detected (genuine cross-project chat)
- Confidence score 0.60–0.75 (borderline)
- Generic language with insufficient context

### Output Structure

```json
{
  "chat_id": "platform-unique-id",
  "timestamp": "2025-06-01T10:00:00Z",
  "title": "Chat subject",
  "content": "Full conversation text",
  "platform": "gemini|chatgpt|claude",
  "detected_projects": {
    "project-id": {
      "confidence": 0.95,
      "confidence_level": "high|medium",
      "matched_patterns": [
        {
          "pattern": "(?i)\\bexact-match\\b",
          "type": "high_confidence"
        }
      ],
      "references": [
        {
          "snippet": "...surrounding context...",
          "position": 1234
        }
      ]
    }
  },
  "needs_manual_review": false,
  "ambiguity_notes": ""
}
```

---

## Part 5: Validation & Quality Checks

### File Format Validation
- [ ] Gemini JSON parses without errors
- [ ] ChatGPT JSON parses without errors (streaming if >100MB)
- [ ] Claude JSON parses without errors
- [ ] No truncated records

### Field Completeness
- [ ] All normalized records have: id, timestamp, title, content, platform
- [ ] Timestamps are valid ISO-8601
- [ ] Content is non-empty for meaningful chats

### Semantic Coverage
- [ ] All manifest projects represented in patterns
- [ ] High confidence patterns are unique to projects (no false positives)
- [ ] Medium confidence patterns capture thematic language

### Chronological Integrity
- [ ] All timestamps parse correctly
- [ ] Timelines sort without errors
- [ ] No future-dated entries (data corruption check)

---

## Part 6: Known Limitations & Future Enhancements

### Current Limitations
1. **Regex-based semantic matching** — Limited to exact keywords and simple patterns
2. **No LLM-based semantic understanding** — Future enhancement for context-aware matching
3. **No cross-project deduplication** — Same topic discussed in multiple projects shows up in all
4. **No conversation threading** — Multi-turn structure is flattened into single content block
5. **Manual review still required** — Ambiguous cases need human judgment

### Future Enhancements
1. **LLM-Enhanced Semantic Matching** — Claude model to understand contextual project relevance
2. **Conversation Threading** — Preserve multi-turn structure for narrative reconstruction
3. **Cross-Project Coherence Analysis** — Detect when a chat genuinely spans multiple projects vs. false positive
4. **Confidence Calibration** — Learn from manual review corrections to improve scoring
5. **Temporal Clustering** — Group semantically related chats by time to detect project phases
6. **Guardrail Integration** — Feed extracted timelines to specificity/texture/distinctiveness checks (see guardrails.py)

---

## Implementation Checklist

**Before running extraction pipeline:**

- [ ] Read all three JSON export files (spot-check a record from each)
- [ ] Verify file paths exist and are readable
- [ ] Confirm manifest.json is current
- [ ] Validate schema against expected platform structures
- [ ] Document any platform-specific irregularities

**During extraction:**

- [ ] Log all parsing errors (mismatched formats, missing fields)
- [ ] Record ambiguous matches for manual review
- [ ] Output raw_export for validation sampling
- [ ] Generate statistics: total chats, projects detected, confidence distribution

**After extraction:**

- [ ] Verify each project has at least one mention (unless legitimately absent)
- [ ] Spot-check high-confidence and medium-confidence samples
- [ ] Review ambiguity flags (should be <5% of total)
- [ ] Validate chronological order per project
- [ ] Check for data corruption (timestamps out of range, truncated content)

---

## Schema Summary Table

| Component | Source | Processing | Output |
|-----------|--------|-----------|--------|
| **Gemini** | HTML in safeHtmlItem | HTML → plain text | Normalized JSON |
| **ChatGPT** | Message array | Concatenate roles | Normalized JSON |
| **Claude** | Message array | Concatenate roles | Normalized JSON |
| **Semantic Indexing** | Title + content | Regex patterns (high/medium) | Project tags + confidence |
| **Chronological Sort** | All timestamps | Sort by ISO-8601 | Per-project timelines |
| **Output** | All above | JSON with validation | Ready for case study extraction |

---

## References

- **Manifest Definition:** `/home/peter/homelab/projects/active/petersalvato.com/docs/mainfest.json`
- **Gemini Export:** `/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json`
- **ChatGPT Export:** `/home/peter/homelab/knowledge/exports/data-2026-01-26-15-50-54-batch-0000/conversations.json`
- **Claude Export:** `/home/peter/homelab/knowledge/exports/7bb7d7448a4fe8b37c10d84958a3011b01d3dc5d3b4a88cb8a89ceea3ebda027-2026-01-22-18-47-51-f068f48a77d44e359188dc77169ae29d/conversations.json`
- **Task Plan:** `/home/peter/homelab/projects/active/petersalvato.com/docs/plans/2026-02-06-case-study-extraction-system.md`
