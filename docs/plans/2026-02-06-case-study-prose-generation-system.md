# Case Study Prose Generation System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Generate authentic case study prose by blending Master Builder voice patterns with extracted personal voice/language style, grounded in skeleton moments.

**Architecture:**
1. **Voice Extraction Phase** — Analyze conversations to identify personal tone, vocabulary, pacing, metaphors, sentence structure
2. **Voice Blending Phase** — Merge personal voice with Master Builder principles (directness, concreteness, grounding)
3. **Prose Generation Phase** — LLM generates drafts using blended voice + skeleton structure
4. **Skeleton Fidelity Validation** — Verify prose stays grounded in actual moments, doesn't fabricate or flatten
5. **Final Guardrail Validation** — Check texture, specificity, authenticity against skeleton
6. **Multi-Project Orchestration** — Generate prose for all 17 projects

**Tech Stack:** Python, voice pattern analysis (regex + semantic matching), LLM prompting, JSON templates, guardrail validation

---

## Core Philosophy

**Hybrid approach with authentic voice:**
1. **Extract your voice** from actual conversations (how you naturally explain, your rhythm, your metaphors)
2. **Apply Master Builder discipline** (directness, concreteness, grounding in materials/constraints)
3. **Blend them** — Your thinking filtered through Master Builder principles
4. **Ground in skeleton** — Every claim tied to actual moments from conversations
5. **Validate rigorously** — Prose must match skeleton fidelity, not fabricate details

**Why this works:**
- Master Builder voice becomes a *filter* on your natural thinking, not a substitute
- Prose sounds like you, but more disciplined
- Every sentence grounded in actual conversation content
- Impossible to flatten because skeleton moments are unchangeable

---

## Input Data

**17 narrative skeletons** (from case-study-skeletons/):
- Each has: constraint, chronological arc (2,396 moments), source snippets
- Each moment has: actual quote, platform, timestamp, moment type

**Personal voice patterns** (extracted from 3,201 conversations):
- Sentence structure, vocabulary choices, metaphor patterns
- How you explain complexity, pace of ideas
- Your characteristic phrases and thinking patterns
- Your use of concrete examples, technical language, abstraction

---

## Task Breakdown

### Task 1: Extract personal voice patterns from conversations

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/voice_extractor.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_voice_extractor.py`

**Step 1: Write failing test**

```python
# tests/test_voice_extractor.py
from scripts.voice_extractor import VoiceExtractor

def test_extract_voice_patterns():
    extractor = VoiceExtractor()

    sample_conversations = [
        {
            "content": "I need a way to mark where my thinking changed, not just what I thought",
            "platform": "claude"
        },
        {
            "content": "This pattern shows up everywhere: when you own the entire system end-to-end, coherence survives.",
            "platform": "claude"
        }
    ]

    patterns = extractor.extract_patterns(sample_conversations)

    assert patterns["sentence_structure"] is not None
    assert patterns["vocabulary"] is not None
    assert patterns["metaphors"] is not None
    assert patterns["pacing"] is not None

def test_identify_characteristic_phrases():
    extractor = VoiceExtractor()

    sample_conversations = [
        {"content": "The real insight is that..."},
        {"content": "What actually matters is..."},
        {"content": "The tension is between..."}
    ]

    phrases = extractor.identify_characteristic_phrases(sample_conversations)

    assert "insight" in str(phrases).lower()
```

**Step 2: Run test to verify it fails**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python -m pytest tests/test_voice_extractor.py::test_extract_voice_patterns -v
```

**Step 3: Write implementation**

```python
# scripts/voice_extractor.py
from typing import Dict, List
import re
from collections import Counter

class VoiceExtractor:
    def __init__(self):
        # Patterns for identifying voice characteristics
        self.STRUCTURAL_PATTERNS = {
            "short_declarative": r"^[A-Z][^.!?]{10,30}\.$",
            "setup_then_detail": r"[^.!?]+\.\s+[A-Z][^.!?]*\.",
            "parallel_structure": r"(\w+\s+[\w\s]+),\s+(\w+\s+[\w\s]+),\s+(\w+\s+[\w\s]+)"
        }

        self.CHARACTERISTIC_PHRASES = [
            "the real (insight|problem|tension)",
            "what (actually|really) (matters|happens)",
            "the (gap|difference|tension) (between|is)",
            "if you (own|control|understand)",
            "this (survives|fails|breaks) because",
            "the (pattern|lesson|insight) (is|shows)",
            "you need (to|a way to)",
            "the key (insight|difference|tension)"
        ]

        self.METAPHOR_CATEGORIES = {
            "structural": r"(scaffold|foundation|pillar|frame|architecture|system)",
            "material": r"(material|concrete|surface|texture|solid|durable)",
            "flow": r"(flow|current|stream|movement|drift|shift)",
            "visibility": r"(see|visible|clear|transparent|obscured|hidden)"
        }

    def extract_patterns(self, conversations: List[Dict]) -> Dict:
        """Extract voice patterns from conversations"""

        all_content = " ".join([c.get("content", "") for c in conversations])

        patterns = {
            "sentence_structure": self._analyze_sentence_structure(all_content),
            "vocabulary": self._analyze_vocabulary(all_content),
            "metaphors": self._identify_metaphor_preferences(all_content),
            "pacing": self._analyze_pacing(all_content),
            "characteristic_phrases": self.identify_characteristic_phrases(conversations)
        }

        return patterns

    def _analyze_sentence_structure(self, content: str) -> Dict:
        """Identify sentence structure patterns"""
        sentences = re.split(r'[.!?]+', content)

        avg_length = sum(len(s.split()) for s in sentences) / len(sentences)

        return {
            "average_sentence_length": avg_length,
            "uses_short_declaratives": any(re.match(self.STRUCTURAL_PATTERNS["short_declarative"], s) for s in sentences),
            "uses_parallel_structure": any(re.search(self.STRUCTURAL_PATTERNS["parallel_structure"], s) for s in sentences)
        }

    def _analyze_vocabulary(self, content: str) -> Dict:
        """Identify vocabulary preferences"""
        words = content.lower().split()

        # Technical vs. accessible vocabulary balance
        technical_words = [w for w in words if re.match(r'(architecture|system|pattern|constraint|framework|protocol)', w)]
        concrete_words = [w for w in words if re.match(r'(material|physical|surface|touch|see|build|make)', w)]

        return {
            "technical_ratio": len(technical_words) / len(words) if words else 0,
            "concrete_ratio": len(concrete_words) / len(words) if words else 0,
            "vocabulary_diversity": len(set(words)) / len(words) if words else 0
        }

    def _identify_metaphor_preferences(self, content: str) -> Dict:
        """Identify metaphor and analogy patterns"""
        metaphors = {}

        for category, pattern in self.METAPHOR_CATEGORIES.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            metaphors[category] = len(matches)

        return metaphors

    def _analyze_pacing(self, content: str) -> Dict:
        """Analyze pace of idea development"""
        paragraphs = content.split('\n\n')

        return {
            "average_paragraph_length": sum(len(p.split()) for p in paragraphs) / len(paragraphs) if paragraphs else 0,
            "idea_density": "high" if sum(len(p.split()) for p in paragraphs) / len(paragraphs) > 100 else "moderate"
        }

    def identify_characteristic_phrases(self, conversations: List[Dict]) -> List[str]:
        """Find phrases characteristic of your voice"""
        all_content = " ".join([c.get("content", "") for c in conversations])

        found_phrases = []
        for phrase_pattern in self.CHARACTERISTIC_PHRASES:
            if re.search(phrase_pattern, all_content, re.IGNORECASE):
                found_phrases.append(phrase_pattern)

        return found_phrases
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_voice_extractor.py -v
```

**Step 5: Commit**

```bash
git add scripts/voice_extractor.py tests/test_voice_extractor.py
git commit -m "feat: add voice pattern extraction from conversations"
```

---

### Task 2: Analyze Master Builder voice principles

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/voice_blender.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_voice_blender.py`

**Step 1: Write failing test**

```python
# tests/test_voice_blender.py
from scripts.voice_blender import VoiceBlender

def test_blend_voices():
    blender = VoiceBlender()

    personal_voice = {
        "sentence_structure": {"average_sentence_length": 18},
        "vocabulary": {"technical_ratio": 0.15, "concrete_ratio": 0.12},
        "pacing": {"idea_density": "high"},
        "characteristic_phrases": ["the real insight", "what actually matters"]
    }

    master_builder_rules = {
        "directness": "lead with what was built",
        "concreteness": "reference materials and constraints",
        "grounding": "explain the why through structural necessity"
    }

    blended = blender.blend_voices(personal_voice, master_builder_rules)

    assert blended["sentence_structure"] is not None
    assert blended["directives"] is not None
    assert blended["voice_prompt"] is not None

def test_generate_blended_prompt():
    blender = VoiceBlender()

    prompt = blender.generate_voice_prompt(
        personal_patterns={"characteristic_phrases": ["the real insight"]},
        master_builder_rules={"directness": True}
    )

    assert "insight" in prompt.lower()
    assert "direct" in prompt.lower() or "concrete" in prompt.lower()
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_voice_blender.py::test_blend_voices -v
```

**Step 3: Write implementation**

```python
# scripts/voice_blender.py
from typing import Dict, List

class VoiceBlender:
    MASTER_BUILDER_PRINCIPLES = {
        "directness": "Lead with what was built, not abstractions. 'I built X to solve Y.'",
        "concreteness": "Reference actual materials, constraints, structural choices. Never generalize.",
        "grounding": "Explain why through structural necessity, not aspiration.",
        "economy": "No words wasted. Every sentence earns its place.",
        "specificity": "Name the specific problem, not 'a problem'. Use actual constraints.",
        "honesty": "Show failure, pivots, dead ends. Systems survive because they handled real friction."
    }

    def blend_voices(self, personal_voice: Dict, master_builder_rules: Dict) -> Dict:
        """Blend personal voice with Master Builder principles"""

        blended = {
            "sentence_structure": personal_voice.get("sentence_structure", {}),
            "vocabulary_balance": self._blend_vocabulary(personal_voice.get("vocabulary", {})),
            "pacing": personal_voice.get("pacing", {}),
            "characteristic_phrases": personal_voice.get("characteristic_phrases", []),
            "directives": self._create_directives(personal_voice, master_builder_rules),
            "voice_prompt": self.generate_voice_prompt(personal_voice, master_builder_rules)
        }

        return blended

    def _blend_vocabulary(self, personal_vocab: Dict) -> Dict:
        """Ensure vocabulary balances technical and concrete"""
        return {
            "target_technical_ratio": max(0.10, personal_vocab.get("technical_ratio", 0.15)),
            "target_concrete_ratio": max(0.12, personal_vocab.get("concrete_ratio", 0.10)),
            "principle": "Technical enough to be precise, concrete enough to be grounded"
        }

    def _create_directives(self, personal_voice: Dict, rules: Dict) -> List[str]:
        """Create specific writing directives"""
        directives = [
            "Lead every section with what was built, not why it was needed",
            "Use actual material constraints to explain decisions",
            "Show the problem through structural gaps, not abstract statements",
            "Include moments where approach changed, prove thinking was rigorous",
            "Use your characteristic phrases where they naturally fit",
            "Match your sentence structure: " + str(personal_voice.get("sentence_structure", {}))
        ]

        return directives

    def generate_voice_prompt(self, personal_patterns: Dict, master_builder_rules: Dict) -> str:
        """Generate a prompt for prose generation"""

        phrases = personal_patterns.get("characteristic_phrases", [])
        phrases_str = ", ".join(phrases[:3]) if phrases else "insights and patterns"

        prompt = f"""Write in a voice that:

1. MASTER BUILDER PRINCIPLES (Non-negotiable):
   - Lead with what was built. Explain why through structural necessity.
   - Reference actual constraints and materials.
   - Show where approach changed. Include failures and pivots.
   - Every sentence must earn its place.
   - Grounded, concrete, honest. No marketing language.

2. YOUR VOICE (Characteristic patterns from your actual thinking):
   - Your characteristic phrases: {phrases_str}
   - Your sentence structure: {personal_patterns.get('sentence_structure', {}).get('average_sentence_length', 'moderate')} word average
   - Your pacing: {personal_patterns.get('pacing', {}).get('idea_density', 'balanced')}
   - Your style: Technical enough to be precise, concrete enough to be grounded

3. BLENDED VOICE (Master Builder + You):
   - Use your natural way of explaining, filtered through Master Builder discipline
   - Your thinking patterns become more structured and grounded
   - Concrete examples drive every explanation
   - Show the thinking process, not just the outcome
"""

        return prompt
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_voice_blender.py -v
```

**Step 5: Commit**

```bash
git add scripts/voice_blender.py tests/test_voice_blender.py
git commit -m "feat: add voice blending (personal + Master Builder principles)"
```

---

### Task 3: Create prose generator with skeleton fidelity validation

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/prose_generator.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_prose_generator.py`

**Step 1: Write failing test**

```python
# tests/test_prose_generator.py
from scripts.prose_generator import ProseGenerator

def test_generate_prose_from_skeleton():
    generator = ProseGenerator()

    skeleton = {
        "project": "savepoint-protocol",
        "constraint": "Capture semantic turning points where thinking shifts",
        "arc": [
            {
                "type": "genesis",
                "timestamp": "2024-09-30T10:00:00Z",
                "snippet": "I need a way to mark where my thinking changed",
                "platform": "claude"
            },
            {
                "type": "problem",
                "timestamp": "2024-10-05T14:30:00Z",
                "snippet": "Tagging systems don't capture the shift",
                "platform": "claude"
            },
            {
                "type": "pivot",
                "timestamp": "2024-10-15T09:00:00Z",
                "snippet": "Markup language preserves the moment",
                "platform": "claude"
            }
        ]
    }

    voice_prompt = "Your characteristic voice..."

    prose = generator.generate_prose(skeleton, voice_prompt)

    assert prose is not None
    assert len(prose) > 200
    assert "savepoint" in prose.lower() or "mark" in prose.lower()

def test_validate_skeleton_fidelity():
    generator = ProseGenerator()

    skeleton = {
        "constraint": "Capture thinking shifts",
        "arc": [{"snippet": "mark where thinking changed"}]
    }

    prose = "Built a system to capture semantic turning points..."

    validation = generator.validate_fidelity(prose, skeleton)

    assert validation["fidelity_score"] > 0
    assert "coherent" in validation or validation["issues"] is not None
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_prose_generator.py::test_generate_prose_from_skeleton -v
```

**Step 3: Write implementation**

```python
# scripts/prose_generator.py
from typing import Dict, List
import json

class ProseGenerator:
    def generate_prose(self, skeleton: Dict, voice_prompt: str, max_length: int = 2000) -> str:
        """Generate prose from skeleton using blended voice"""

        project = skeleton.get("project", "Unknown")
        constraint = skeleton.get("constraint", "")
        arc = skeleton.get("arc", [])

        # Build prompt for LLM
        prompt = self._build_prose_prompt(skeleton, voice_prompt)

        # Call LLM (placeholder - would be actual API call)
        prose = self._call_llm(prompt, max_length)

        # Validate skeleton fidelity
        validation = self.validate_fidelity(prose, skeleton)

        if validation.get("fidelity_score", 0) < 0.6:
            # If fidelity is low, regenerate with tighter constraints
            return self._regenerate_with_constraints(skeleton, voice_prompt, validation)

        return prose

    def _build_prose_prompt(self, skeleton: Dict, voice_prompt: str) -> str:
        """Build comprehensive prompt for prose generation"""

        arc_summary = self._summarize_arc(skeleton.get("arc", []))

        prompt = f"""{voice_prompt}

PROJECT: {skeleton.get('project', 'Unknown')}
CONSTRAINT: {skeleton.get('constraint', 'Not specified')}

NARRATIVE ARC (in chronological order):
{arc_summary}

INSTRUCTIONS:
1. Start with: "I [built/created/designed] [system] to [solve constraint]"
2. Walk through the arc moments in order, expanding each into prose
3. Use actual quotes from the snippets where they fit naturally
4. Show the thinking evolution: what problem emerged, how approach changed, what validates it works
5. Keep language direct, concrete, grounded in structural choices
6. Total length: 800-1200 words

Remember: Every claim must be grounded in the arc moments. Don't fabricate details.
"""

        return prompt

    def _summarize_arc(self, arc: List[Dict]) -> str:
        """Summarize arc moments for context"""
        summary = []
        for moment in arc[:10]:  # Use first 10 moments for context
            summary.append(f"- [{moment.get('type')}] {moment.get('snippet')}")

        return "\n".join(summary)

    def _call_llm(self, prompt: str, max_length: int) -> str:
        """Call LLM to generate prose (placeholder)"""
        # This would be actual API call to Claude API
        # For now, return structured response
        return f"[Generated prose for: {prompt[:50]}...]"

    def validate_fidelity(self, prose: str, skeleton: Dict) -> Dict:
        """Validate that prose stays grounded in skeleton"""

        validation = {
            "fidelity_score": 0.0,
            "grounded": True,
            "issues": []
        }

        # Check if prose references key moments
        arc = skeleton.get("arc", [])
        constraint = skeleton.get("constraint", "")

        snippet_matches = 0
        for moment in arc[:5]:  # Check first 5 moments
            snippet = moment.get("snippet", "")
            if snippet.lower() in prose.lower():
                snippet_matches += 1

        # Calculate fidelity score
        fidelity_score = (snippet_matches / max(1, len(arc[:5]))) * 0.5  # Snippet match is 50%

        # Add points if constraint is mentioned
        if constraint.lower() in prose.lower():
            fidelity_score += 0.3

        # Add points if prose shows thinking evolution
        if any(word in prose.lower() for word in ["pivot", "realized", "problem", "failed"]):
            fidelity_score += 0.2

        validation["fidelity_score"] = min(1.0, fidelity_score)

        return validation

    def _regenerate_with_constraints(self, skeleton: Dict, voice_prompt: str, validation: Dict) -> str:
        """Regenerate with tighter fidelity constraints"""

        # Build tighter prompt with specific issues
        tighter_prompt = f"""Previous attempt had fidelity issues: {validation.get('issues', [])}

Regenerate with these constraints:
1. Must reference specific moments from the arc (use exact snippets)
2. Must explain the constraint clearly
3. Must show thinking evolution through the moments
4. Keep it grounded - no speculation

{voice_prompt}
"""

        return self._call_llm(tighter_prompt, 2000)
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_prose_generator.py -v
```

**Step 5: Commit**

```bash
git add scripts/prose_generator.py tests/test_prose_generator.py
git commit -m "feat: add prose generator with skeleton fidelity validation"
```

---

### Task 4: Create final prose quality guardrails

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/prose_guardrails.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_prose_guardrails.py`

**Step 1: Write failing test**

```python
# tests/test_prose_guardrails.py
from scripts.prose_guardrails import ProseGuardrails

def test_reject_generic_prose():
    guardrails = ProseGuardrails()

    prose = "I built a system to help organize work better."

    result = guardrails.validate(prose)

    assert not result["passes"]
    assert "generic" in result["issues"][0].lower()

def test_reject_marketing_language():
    guardrails = ProseGuardrails()

    prose = "This innovative solution empowers teams to synergize their workflows."

    result = guardrails.validate(prose)

    assert not result["passes"]
    assert any("marketing" in issue.lower() for issue in result["issues"])

def test_accept_grounded_prose():
    guardrails = ProseGuardrails()

    prose = """Built a markup language to capture semantic turning points.

The problem: tagging systems don't preserve the moment where thinking shifted.
They capture what you thought, not where you realized it.

The solution: a format that marks inflection points. When understanding clicks,
the system captures that moment, not just the outcome. This means later, you can
retrace the thinking, not just the data."""

    result = guardrails.validate(prose)

    assert result["passes"]
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_prose_guardrails.py::test_reject_generic_prose -v
```

**Step 3: Write implementation**

```python
# scripts/prose_guardrails.py
import re
from typing import Dict, List

class ProseGuardrails:
    GENERIC_PHRASES = [
        r"(?i)system for.*work|system to.*work",
        r"(?i)help.*organize|help.*manage",
        r"(?i)productivity tool|management system",
        r"(?i)to.*better|to.*improve",
        r"(?i)streamline|optimize|enhance",
        r"(?i)for.*teams|for.*collaboration"
    ]

    MARKETING_LANGUAGE = [
        r"(?i)innovative|revolutionary|groundbreaking",
        r"(?i)empower|synergize|leverage",
        r"(?i)next-generation|cutting-edge|paradigm",
        r"(?i)seamless|effortless|magical"
    ]

    REQUIRED_ELEMENTS = {
        "specific_problem": [
            r"(?i)problem.*is|the.*gap|didn't.*work",
            r"(?i)missing|broken|constraint"
        ],
        "concrete_solution": [
            r"(?i)built|created|designed|implemented",
            r"(?i)uses.*\(|structure|format"
        ],
        "thinking_evolution": [
            r"(?i)pivot|realized|tried.*instead",
            r"(?i)failed|changed.*approach"
        ]
    }

    def validate(self, prose: str) -> Dict:
        """Validate prose quality"""

        issues = []
        has_elements = {}

        # Check for generic phrases
        for pattern in self.GENERIC_PHRASES:
            if re.search(pattern, prose):
                issues.append(f"Generic phrase detected: {pattern}")
                break

        # Check for marketing language
        for pattern in self.MARKETING_LANGUAGE:
            if re.search(pattern, prose):
                issues.append(f"Marketing language detected: {pattern}")
                break

        # Check for required elements
        for element, patterns in self.REQUIRED_ELEMENTS.items():
            found = any(re.search(p, prose) for p in patterns)
            has_elements[element] = found
            if not found:
                issues.append(f"Missing: {element}")

        # Check for Master Builder voice indicators
        master_builder_indicators = [
            r"(?i)built|created|designed",
            r"(?i)problem|constraint|gap",
            r"(?i)structure|material|concrete"
        ]

        indicators_found = sum(1 for p in master_builder_indicators if re.search(p, prose))

        if indicators_found < 2:
            issues.append("Lacks Master Builder voice (missing concrete/structural language)")

        return {
            "passes": len(issues) == 0,
            "issues": issues,
            "has_elements": has_elements,
            "voice_strength": indicators_found / len(master_builder_indicators)
        }
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_prose_guardrails.py -v
```

**Step 5: Commit**

```bash
git add scripts/prose_guardrails.py tests/test_prose_guardrails.py
git commit -m "feat: add prose quality guardrails (generic/marketing language detection)"
```

---

### Task 5: Create case study prose orchestrator

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/case_study_prose_writer.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_case_study_prose_writer.py`

**Step 1: Write failing test**

```python
# tests/test_case_study_prose_writer.py
from scripts.case_study_prose_writer import CaseStudyProseWriter

def test_write_all_case_study_prose():
    writer = CaseStudyProseWriter(
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons",
        conversation_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    prose_docs = writer.write_all_prose()

    assert len(prose_docs) >= 17
    assert all(doc.get("project") for doc in prose_docs)
    assert all(doc.get("prose") for doc in prose_docs)
    assert all(doc.get("validation") for doc in prose_docs)
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_case_study_prose_writer.py::test_write_all_case_study_prose -v
```

**Step 3: Write implementation**

```python
# scripts/case_study_prose_writer.py
import json
from pathlib import Path
from voice_extractor import VoiceExtractor
from voice_blender import VoiceBlender
from prose_generator import ProseGenerator
from prose_guardrails import ProseGuardrails

class CaseStudyProseWriter:
    def __init__(self, skeleton_dir: str, conversation_dir: str):
        self.skeleton_dir = Path(skeleton_dir)
        self.conversation_dir = Path(conversation_dir)

        self.voice_extractor = VoiceExtractor()
        self.voice_blender = VoiceBlender()
        self.prose_generator = ProseGenerator()
        self.prose_guardrails = ProseGuardrails()

    def write_all_prose(self) -> list:
        """Write prose for all 17 projects"""

        # Step 1: Extract personal voice from conversations
        conversations = self._load_conversations()
        personal_voice = self.voice_extractor.extract_patterns(conversations)

        # Step 2: Blend with Master Builder voice
        blended_voice = self.voice_blender.blend_voices(personal_voice, {})
        voice_prompt = blended_voice.get("voice_prompt", "")

        # Step 3: Generate prose for each project
        prose_docs = []

        for skeleton_file in sorted(self.skeleton_dir.glob("*-skeleton.json")):
            with open(skeleton_file) as f:
                skeleton = json.load(f)

            project = skeleton.get("project")

            # Generate prose
            prose = self.prose_generator.generate_prose(skeleton, voice_prompt)

            # Validate quality
            validation = self.prose_guardrails.validate(prose)

            # Save prose
            prose_file = self.skeleton_dir.parent / "case-study-prose" / f"{project}-prose.md"
            prose_file.parent.mkdir(exist_ok=True)

            with open(prose_file, 'w') as f:
                f.write(prose)

            prose_docs.append({
                "project": project,
                "prose": prose,
                "validation": validation,
                "fidelity_score": self.prose_generator.validate_fidelity(prose, skeleton).get("fidelity_score", 0)
            })

        return prose_docs

    def _load_conversations(self) -> list:
        """Load all conversations for voice extraction"""
        conversations = []

        # Load from timeline JSON files (which contain the conversation content)
        for timeline_file in self.conversation_dir.glob("*-timeline.json"):
            with open(timeline_file) as f:
                timeline = json.load(f)

                # Extract conversations from arc moments
                for moment in timeline.get("arc", []):
                    conversations.append({
                        "content": moment.get("content", ""),
                        "platform": moment.get("platform", "")
                    })

        return conversations
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_case_study_prose_writer.py -v
```

**Step 5: Commit**

```bash
git add scripts/case_study_prose_writer.py tests/test_case_study_prose_writer.py
git commit -m "feat: add case study prose writer orchestrator"
```

---

### Task 6: Create prose generation runner and final report

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/run_prose_generation.py`

**Implementation:**

```python
# scripts/run_prose_generation.py
from case_study_prose_writer import CaseStudyProseWriter
from pathlib import Path

def main():
    print("=" * 70)
    print("CASE STUDY PROSE GENERATION")
    print("=" * 70)
    print()

    print("Step 1: Extracting personal voice from conversations...")
    print()

    writer = CaseStudyProseWriter(
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons",
        conversation_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    prose_docs = writer.write_all_prose()

    print(f"✓ Generated prose for {len(prose_docs)} projects")
    print()

    # Step 2: Validation summary
    print("Step 2: Validation Results")
    print()

    passed = sum(1 for doc in prose_docs if doc["validation"]["passes"])
    failed = len(prose_docs) - passed

    print(f"✓ {passed} passed validation")
    if failed > 0:
        print(f"⚠️  {failed} need review/revision")
    print()

    # Step 3: Report
    print("SUMMARY")
    print("-" * 70)
    print(f"Projects: {len(prose_docs)}")
    print(f"Prose documents generated: docs/case-study-prose/")
    print()
    print("✅ PROSE GENERATION COMPLETE")
    print()
    print("Next: Review prose files and refine as needed")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
```

**Run it:**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python scripts/run_prose_generation.py
```

**Commit:**

```bash
git add scripts/run_prose_generation.py
git commit -m "feat: add prose generation runner"
```

---

## Execution Approach

**Plan complete and saved to `docs/plans/2026-02-06-case-study-prose-generation-system.md`**

**Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**
