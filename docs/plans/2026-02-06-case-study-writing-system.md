# Case Study Writing System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Extract key thinking moments from 2,448 timeline entries and assemble narrative skeletons for all 17 projects, ready for human refinement.

**Architecture:**
1. **Moment Extraction Phase** — Identify inflection points in each timeline (genesis, pivots, failures, refinements)
2. **Narrative Assembly Phase** — Build skeleton from moments (constraint → problem → approach → outcome)
3. **Voice Integration Phase** — Preserve Master Builder voice from actual conversations
4. **Guardrail Validation Phase** — Ensure no flattening, texture preserved, specificity maintained
5. **Human Refinement Ready** — Output narrative skeletons with source quotations for final editing

**Tech Stack:** Python, JSON timelines, narrative analysis, Master Builder voice patterns

---

## Core Philosophy

**Extraction + Assembly approach (NOT AI generation):**
1. Machine finds key moments (where thinking shifted, problems emerged, solutions evolved)
2. Machine assembles skeleton (linking moments chronologically)
3. Machine preserves actual words/thinking from conversations
4. **Human refines** (you decide final narrative, voice, emphasis)

**Why this prevents flattening:**
- Grounded in actual thinking inflection points
- Source material visible (quotations)
- Machine can't genericize what's already specific
- You maintain creative control

---

## Input Data

**17 project timelines** (from docs/extraction-output/):
- savepoint-protocol: 548 entries
- order-of-the-aetherwright: 351 entries
- monstrum: 295 entries
- modernist-homestead: 220 entries
- mathontape: 185 entries
- aiden-jae: 177 entries
- photogeography: 150 entries
- altrueism: 89 entries
- portable-agency: 80 entries
- echo-and-bone: 71 entries
- the-deep-cuts: 69 entries
- cryptozoology: 53 entries
- ai-devops-workbench: 42 entries
- encore: 38 entries
- everyday-gold: 37 entries
- motorology: 34 entries
- versagrams: 9 entries

---

## Task Breakdown

### Task 1: Create moment extraction framework

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/moment_extractor.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_moment_extractor.py`

**Step 1: Define moment types**

```python
# scripts/moment_extractor.py
from typing import Dict, List
from enum import Enum

class MomentType(Enum):
    GENESIS = "genesis"           # First mention, origin
    REALIZATION = "realization"   # Insight, understanding shift
    PROBLEM = "problem"           # What broke, what was missing
    PIVOT = "pivot"               # Changed approach
    REFINEMENT = "refinement"     # Iterative improvement
    INTEGRATION = "integration"   # Connecting with other systems
    VALIDATION = "validation"     # Proof, testing, confirmation
    ARTIFACT = "artifact"         # Tangible output, deliverable

class Moment:
    def __init__(self, moment_type: MomentType, timestamp: str, content: str,
                 platform: str, snippet: str):
        self.type = moment_type
        self.timestamp = timestamp
        self.content = content  # Full message
        self.platform = platform  # gemini/chatgpt/claude
        self.snippet = snippet  # Key quote (50-150 chars)
```

**Step 2: Write failing test**

```python
# tests/test_moment_extractor.py
from scripts.moment_extractor import MomentExtractor, MomentType

def test_extract_genesis_moment():
    extractor = MomentExtractor()
    timeline = [
        {
            "title": "First idea about Savepoint",
            "timestamp": "2024-09-30T10:00:00Z",
            "content": "I need a way to mark where my thinking changed, not just what I thought",
            "platform": "claude"
        }
    ]

    moments = extractor.extract_moments(timeline)

    assert len(moments) > 0
    assert moments[0].type == MomentType.GENESIS
    assert "mark where" in moments[0].snippet.lower()

def test_detect_pivot_keyword():
    extractor = MomentExtractor()
    content = "I tried tagging first, but that didn't work. Then I realized it should be markup language."

    moment_type = extractor.detect_moment_type(content)

    assert moment_type == MomentType.PIVOT
```

**Step 3: Write implementation**

```python
# Add to scripts/moment_extractor.py
import re
from typing import Dict, List

class MomentExtractor:
    MOMENT_PATTERNS = {
        MomentType.GENESIS: [
            r"(?i)first.*thought|initial.*idea|started.*with|began.*as",
            r"(?i)origin.*of|where.*began|started.*building"
        ],
        MomentType.REALIZATION: [
            r"(?i)realized|clicked|understood|dawned|insight",
            r"(?i)then.*i.*saw|finally.*understood|it.*hit.*me"
        ],
        MomentType.PROBLEM: [
            r"(?i)didn't.*work|broke|failed|missing|gap|problem|issue",
            r"(?i)couldn't.*handle|limitation|constraint"
        ],
        MomentType.PIVOT: [
            r"(?i)pivot|changed.*approach|tried.*instead|switched.*to",
            r"(?i)instead.*of|different.*approach|new.*direction"
        ],
        MomentType.REFINEMENT: [
            r"(?i)improved|refined|polished|iterated|enhanced",
            r"(?i)better.*version|next.*iteration|took.*further"
        ],
        MomentType.INTEGRATION: [
            r"(?i)connected.*with|integrat|works.*with|alongside",
            r"(?i)ecosystem|unified|together.*as"
        ],
        MomentType.VALIDATION: [
            r"(?i)tested|verified|confirmed|works|proved|validate",
            r"(?i)showed.*that|demonstrates|evidence.*of"
        ],
        MomentType.ARTIFACT: [
            r"(?i)built|created|deployed|shipped|released|published",
            r"(?i)made.*system|wrote.*code|designed.*interface"
        ]
    }

    def extract_moments(self, timeline: List[Dict]) -> List[Moment]:
        """Extract key moments from timeline"""
        moments = []

        for entry in timeline:
            moment_type = self.detect_moment_type(entry.get("content", ""))

            if moment_type:
                snippet = self._extract_snippet(entry.get("content", ""), 100)
                moment = Moment(
                    moment_type=moment_type,
                    timestamp=entry.get("timestamp", ""),
                    content=entry.get("content", ""),
                    platform=entry.get("platform", ""),
                    snippet=snippet
                )
                moments.append(moment)

        return moments

    def detect_moment_type(self, content: str) -> MomentType:
        """Detect moment type from content"""
        for moment_type, patterns in self.MOMENT_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, content):
                    return moment_type

        return None

    def _extract_snippet(self, content: str, max_length: int) -> str:
        """Extract meaningful snippet from content"""
        # Find first sentence or up to max_length
        sentences = content.split(". ")
        snippet = sentences[0]

        if len(snippet) > max_length:
            snippet = snippet[:max_length].rsplit(" ", 1)[0] + "…"

        return snippet
```

**Step 4: Run tests**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python -m pytest tests/test_moment_extractor.py -v
```

**Step 5: Commit**

```bash
git add scripts/moment_extractor.py tests/test_moment_extractor.py
git commit -m "feat: add moment extraction framework for narrative analysis"
```

---

### Task 2: Create narrative skeleton builder

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/narrative_builder.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_narrative_builder.py`

**Step 1: Write failing test**

```python
# tests/test_narrative_builder.py
from scripts.narrative_builder import NarrativeBuilder, NarrativeSkeleton

def test_build_narrative_skeleton():
    builder = NarrativeBuilder()

    moments = [
        {
            "type": "genesis",
            "timestamp": "2024-09-30T10:00:00Z",
            "snippet": "I need to mark where my thinking changed"
        },
        {
            "type": "problem",
            "timestamp": "2024-10-05T14:30:00Z",
            "snippet": "Tagging systems don't capture the shift"
        },
        {
            "type": "pivot",
            "timestamp": "2024-10-15T09:00:00Z",
            "snippet": "Markup language preserves the moment"
        },
        {
            "type": "validation",
            "timestamp": "2024-11-01T16:00:00Z",
            "snippet": "This approach captures inflection points"
        }
    ]

    skeleton = builder.build_skeleton("savepoint-protocol", moments)

    assert skeleton.project == "savepoint-protocol"
    assert skeleton.constraint is not None
    assert skeleton.arc is not None
    assert len(skeleton.arc) >= 3  # At least genesis → problem → solution

def test_skeleton_has_quotations():
    builder = NarrativeBuilder()

    moments = [{"type": "genesis", "timestamp": "2024-09-30T10:00:00Z",
                "snippet": "First idea"}]

    skeleton = builder.build_skeleton("test-project", moments)

    # Check that skeleton includes source quotations
    assert any(m.get("snippet") for m in skeleton.arc)
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_narrative_builder.py::test_build_narrative_skeleton -v
```

**Step 3: Write implementation**

```python
# scripts/narrative_builder.py
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class NarrativeSkeleton:
    project: str
    constraint: str  # What problem does this system solve?
    arc: List[Dict]  # Chronological moments with snippets
    platforms: Dict[str, int]  # Count by platform
    timeline_span: str  # From X to Y
    texture_score: float  # Complexity (0-1)
    source_snippets: List[str]  # Actual quotes from timeline

class NarrativeBuilder:
    def build_skeleton(self, project_id: str, moments: List[Dict]) -> NarrativeSkeleton:
        """Build narrative skeleton from extracted moments"""

        # Identify constraint from genesis + problem moments
        constraint = self._identify_constraint(moments)

        # Build chronological arc
        arc = self._build_arc(moments)

        # Count platforms
        platforms = self._count_platforms(moments)

        # Calculate texture score (presence of pivots, failures, complexity)
        texture = self._calculate_texture(moments)

        # Extract source snippets
        snippets = [m.get("snippet") for m in moments if m.get("snippet")]

        # Timeline span
        timestamps = [m.get("timestamp") for m in moments if m.get("timestamp")]
        span = f"{timestamps[0][:10]} to {timestamps[-1][:10]}" if timestamps else ""

        return NarrativeSkeleton(
            project=project_id,
            constraint=constraint,
            arc=arc,
            platforms=platforms,
            timeline_span=span,
            texture_score=texture,
            source_snippets=snippets
        )

    def _identify_constraint(self, moments: List[Dict]) -> str:
        """Extract constraint from genesis + problem moments"""
        genesis_moments = [m for m in moments if m.get("type") == "genesis"]
        problem_moments = [m for m in moments if m.get("type") == "problem"]

        if genesis_moments and problem_moments:
            # Combine to form constraint statement
            return f"Solving: {problem_moments[0].get('snippet', 'undefined problem')}"

        return "Constraint to be extracted"

    def _build_arc(self, moments: List[Dict]) -> List[Dict]:
        """Build narrative arc from moments"""
        # Sort by timestamp
        sorted_moments = sorted(moments, key=lambda m: m.get("timestamp", ""))

        # Return with structure for narrative assembly
        arc = []
        for m in sorted_moments:
            arc.append({
                "type": m.get("type"),
                "timestamp": m.get("timestamp"),
                "snippet": m.get("snippet"),
                "platform": m.get("platform")
            })

        return arc

    def _count_platforms(self, moments: List[Dict]) -> Dict[str, int]:
        """Count moments by platform"""
        platforms = {}
        for m in moments:
            p = m.get("platform", "unknown")
            platforms[p] = platforms.get(p, 0) + 1
        return platforms

    def _calculate_texture(self, moments: List[Dict]) -> float:
        """Calculate texture score (0-1, higher = more complex)"""
        types = [m.get("type") for m in moments]

        # Texture increases with diversity and presence of pivots/failures
        has_pivot = "pivot" in types
        has_problem = "problem" in types
        has_refinement = "refinement" in types
        unique_types = len(set(types))

        score = 0.0
        if has_pivot: score += 0.3
        if has_problem: score += 0.2
        if has_refinement: score += 0.2
        score += min(0.3, unique_types / 8 * 0.3)  # Diversity bonus

        return min(1.0, score)
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_narrative_builder.py -v
```

**Step 5: Commit**

```bash
git add scripts/narrative_builder.py tests/test_narrative_builder.py
git commit -m "feat: add narrative skeleton builder from extracted moments"
```

---

### Task 3: Create multi-project extraction orchestrator

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/case_study_writer.py`
- Modify: `scripts/moment_extractor.py` and `scripts/narrative_builder.py`

**Step 1: Write failing test**

```python
# tests/test_case_study_writer.py
from scripts.case_study_writer import CaseStudyWriter
import json

def test_write_all_case_study_skeletons():
    writer = CaseStudyWriter(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    skeletons = writer.write_all_skeletons()

    assert len(skeletons) >= 17
    assert all(s.project for s in skeletons)
    assert all(s.constraint for s in skeletons)
    assert all(s.arc for s in skeletons)

def test_skeleton_has_texture():
    writer = CaseStudyWriter(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    skeletons = writer.write_all_skeletons()

    # All skeletons should have texture score > 0
    assert all(s.texture_score > 0 for s in skeletons)
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_case_study_writer.py::test_write_all_case_study_skeletons -v
```

**Step 3: Write implementation**

```python
# scripts/case_study_writer.py
import json
from pathlib import Path
from typing import List
from moment_extractor import MomentExtractor, Moment
from narrative_builder import NarrativeBuilder

class CaseStudyWriter:
    def __init__(self, timeline_dir: str):
        self.timeline_dir = Path(timeline_dir)
        self.moment_extractor = MomentExtractor()
        self.narrative_builder = NarrativeBuilder()

    def write_all_skeletons(self) -> List:
        """Extract and write skeletons for all projects"""
        skeletons = []

        # Find all timeline JSON files
        timeline_files = list(self.timeline_dir.glob("*-timeline.json"))

        for timeline_file in sorted(timeline_files):
            project_id = timeline_file.stem.replace("-timeline", "")

            with open(timeline_file) as f:
                timeline = json.load(f)

            # Extract moments
            moments = self.moment_extractor.extract_moments(timeline)

            # Build skeleton
            skeleton = self.narrative_builder.build_skeleton(project_id, moments)
            skeletons.append(skeleton)

            # Save skeleton JSON
            skeleton_file = self.timeline_dir.parent / "case-study-skeletons" / f"{project_id}-skeleton.json"
            skeleton_file.parent.mkdir(exist_ok=True)

            with open(skeleton_file, 'w') as f:
                json.dump({
                    "project": skeleton.project,
                    "constraint": skeleton.constraint,
                    "arc": skeleton.arc,
                    "platforms": skeleton.platforms,
                    "timeline_span": skeleton.timeline_span,
                    "texture_score": skeleton.texture_score,
                    "source_snippets": skeleton.source_snippets
                }, f, indent=2)

        return skeletons
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_case_study_writer.py -v
```

**Step 5: Commit**

```bash
git add scripts/case_study_writer.py tests/test_case_study_writer.py
git commit -m "feat: add case study skeleton writer for all 17 projects"
```

---

### Task 4: Apply guardrails to skeletons

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/skeleton_guardrails.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_skeleton_guardrails.py`

**Step 1: Write failing test**

```python
# tests/test_skeleton_guardrails.py
from scripts.skeleton_guardrails import SkeletonGuardrails

def test_reject_flat_constraint():
    guardrails = SkeletonGuardrails()

    skeleton = {
        "project": "test",
        "constraint": "Personal system for work",
        "arc": [],
        "texture_score": 0.1
    }

    result = guardrails.validate(skeleton)

    assert not result["passes"]
    assert "generic" in result["issues"][0].lower()

def test_reject_low_texture():
    guardrails = SkeletonGuardrails()

    skeleton = {
        "project": "test",
        "constraint": "Specific, detailed constraint",
        "arc": [{"type": "genesis"}],  # Only one type
        "texture_score": 0.05
    }

    result = guardrails.validate(skeleton)

    assert not result["passes"]
    assert "texture" in result["issues"][0].lower()

def test_accept_good_skeleton():
    guardrails = SkeletonGuardrails()

    skeleton = {
        "project": "savepoint-protocol",
        "constraint": "Capture semantic turning points where thinking shifts and meaning clicks",
        "arc": [
            {"type": "genesis"},
            {"type": "problem"},
            {"type": "pivot"},
            {"type": "validation"}
        ],
        "texture_score": 0.75
    }

    result = guardrails.validate(skeleton)

    assert result["passes"]
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_skeleton_guardrails.py -v
```

**Step 3: Write implementation**

```python
# scripts/skeleton_guardrails.py
import re
from typing import Dict, List

class SkeletonGuardrails:
    GENERIC_PATTERNS = [
        r"(?i)personal system",
        r"(?i)organize.*work",
        r"(?i)productivity tool",
        r"(?i)management system"
    ]

    MIN_TEXTURE_SCORE = 0.3
    MIN_ARC_DIVERSITY = 3  # At least 3 different moment types

    def validate(self, skeleton: Dict) -> Dict:
        """Validate skeleton against flattening guardrails"""
        issues = []

        # Check constraint specificity
        constraint = skeleton.get("constraint", "")
        for pattern in self.GENERIC_PATTERNS:
            if re.search(pattern, constraint):
                issues.append(f"Constraint is too generic: '{constraint}'")
                break

        if len(constraint) < 50:
            issues.append(f"Constraint too brief ({len(constraint)} chars)")

        # Check texture
        texture = skeleton.get("texture_score", 0)
        if texture < self.MIN_TEXTURE_SCORE:
            issues.append(f"Texture too low ({texture:.2f}). Arc shows only success, no complexity/pivots.")

        # Check arc diversity
        arc_types = set(m.get("type") for m in skeleton.get("arc", []))
        if len(arc_types) < self.MIN_ARC_DIVERSITY:
            issues.append(f"Arc lacks diversity ({len(arc_types)} types). Need genesis→problem→solution at minimum.")

        return {
            "passes": len(issues) == 0,
            "issues": issues,
            "texture_score": texture,
            "constraint_length": len(constraint),
            "arc_diversity": len(arc_types)
        }
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_skeleton_guardrails.py -v
```

**Step 5: Commit**

```bash
git add scripts/skeleton_guardrails.py tests/test_skeleton_guardrails.py
git commit -m "feat: add guardrails validation for case study skeletons"
```

---

### Task 5: Create narrative assembly report

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/assemble_report.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_assemble_report.py`

**Step 1: Write failing test**

```python
# tests/test_assemble_report.py
from scripts.assemble_report import AssemblyReporter

def test_generate_assembly_report():
    reporter = AssemblyReporter()

    report = reporter.generate_report(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output",
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons"
    )

    assert report["total_projects"] == 17
    assert report["total_entries"] == 2448
    assert all(p["passes"] for p in report["validations"])
    assert "summary_md" in report
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_assemble_report.py -v
```

**Step 3: Write implementation**

```python
# scripts/assemble_report.py
import json
from pathlib import Path
from typing import Dict, List
from skeleton_guardrails import SkeletonGuardrails

class AssemblyReporter:
    def __init__(self):
        self.guardrails = SkeletonGuardrails()

    def generate_report(self, timeline_dir: str, skeleton_dir: str) -> Dict:
        """Generate comprehensive assembly report"""
        timeline_path = Path(timeline_dir)
        skeleton_path = Path(skeleton_dir)

        # Load all skeletons
        skeletons = {}
        total_entries = 0
        validations = []

        for skeleton_file in sorted(skeleton_path.glob("*-skeleton.json")):
            with open(skeleton_file) as f:
                skeleton = json.load(f)

            project = skeleton["project"]
            skeletons[project] = skeleton

            # Validate
            validation = self.guardrails.validate(skeleton)
            validation["project"] = project
            validations.append(validation)

            # Count entries
            total_entries += len(skeleton.get("arc", []))

        # Generate markdown summary
        summary_md = self._generate_markdown(skeletons, validations)

        return {
            "total_projects": len(skeletons),
            "total_entries": total_entries,
            "skeletons": skeletons,
            "validations": validations,
            "summary_md": summary_md
        }

    def _generate_markdown(self, skeletons: Dict, validations: List) -> str:
        """Generate markdown report"""
        md = "# Case Study Skeletons - Assembly Report\n\n"
        md += f"**Total Projects:** {len(skeletons)}\n"
        md += f"**Total Timeline Entries:** {sum(len(s.get('arc', [])) for s in skeletons.values())}\n\n"

        # Table of projects
        md += "| Project | Entries | Texture | Platforms | Status |\n"
        md += "|---------|---------|---------|-----------|--------|\n"

        for v in validations:
            project = v["project"]
            skeleton = skeletons[project]
            entries = len(skeleton.get("arc", []))
            texture = f"{skeleton.get('texture_score', 0):.2f}"
            platforms = ", ".join(skeleton.get("platforms", {}).keys())
            status = "✅ PASS" if v["passes"] else "❌ REVIEW"
            md += f"| {project} | {entries} | {texture} | {platforms} | {status} |\n"

        return md
```

**Step 4: Run tests**

```bash
python -m pytest tests/test_assemble_report.py -v
```

**Step 5: Commit**

```bash
git add scripts/assemble_report.py tests/test_assemble_report.py
git commit -m "feat: add assembly report generator for all case study skeletons"
```

---

### Task 6: Generate skeletons for all 17 projects

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/run_skeleton_generation.py`

**Step 1: Write script**

```python
# scripts/run_skeleton_generation.py
from case_study_writer import CaseStudyWriter
from assemble_report import AssemblyReporter
from pathlib import Path

def main():
    print("Generating case study skeletons for all 17 projects...")

    # Generate skeletons
    writer = CaseStudyWriter(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )
    skeletons = writer.write_all_skeletons()
    print(f"✓ Generated {len(skeletons)} skeletons")

    # Generate report
    reporter = AssemblyReporter()
    report = reporter.generate_report(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output",
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons"
    )

    # Save report
    output_file = Path("/home/peter/homelab/projects/active/petersalvato.com/docs/SKELETON-ASSEMBLY-REPORT.md")
    with open(output_file, 'w') as f:
        f.write(report["summary_md"])

    print(f"✓ Report saved to {output_file}")

    # Show validation results
    passed = sum(1 for v in report["validations"] if v["passes"])
    failed = len(report["validations"]) - passed

    print(f"\n✓ Validations: {passed} passed, {failed} failed")

    if failed > 0:
        print("\nFailed validations:")
        for v in report["validations"]:
            if not v["passes"]:
                print(f"  - {v['project']}: {v['issues']}")

if __name__ == "__main__":
    main()
```

**Step 2: Run script**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python scripts/run_skeleton_generation.py
```

**Step 3: Verify output**

Check that:
- 17 JSON skeleton files created in `docs/case-study-skeletons/`
- Each has: project, constraint, arc, platforms, texture_score, source_snippets
- All validations pass (or review failed ones)
- Report generated at `docs/SKELETON-ASSEMBLY-REPORT.md`

**Step 4: Commit**

```bash
git add scripts/run_skeleton_generation.py
git commit -m "feat: add skeleton generation runner for all 17 projects"
```

---

## Output Structure

After all tasks complete, you'll have:

**For each project:** `/docs/case-study-skeletons/{project}-skeleton.json`
```json
{
  "project": "savepoint-protocol",
  "constraint": "Capture semantic turning points where thinking shifts",
  "arc": [
    {"type": "genesis", "timestamp": "2024-09-30...", "snippet": "...", "platform": "claude"},
    {"type": "problem", "timestamp": "2024-10-05...", "snippet": "...", "platform": "claude"},
    {"type": "pivot", "timestamp": "2024-10-15...", "snippet": "...", "platform": "claude"},
    ...
  ],
  "platforms": {"claude": 320, "gemini": 222, "chatgpt": 6},
  "timeline_span": "2024-09-30 to 2026-01-26",
  "texture_score": 0.85,
  "source_snippets": ["snippet 1", "snippet 2", ...]
}
```

**Master report:** `/docs/SKELETON-ASSEMBLY-REPORT.md`
- Table of all 17 projects with metrics
- Validation status for each
- Texture scores, platform distribution
- Ready for final narrative assembly by you

---

## Next Phase After Execution

Once skeletons are generated:
1. **You review** each skeleton
2. **You refine** constraint statements if needed
3. **You write** case study narratives using skeletons as scaffolding
4. **Guardrails validate** your drafts for flattening/texture/specificity

This approach:
- ✅ Preserves actual thinking (extracted moments)
- ✅ Prevents genericization (grounded in sources)
- ✅ Puts you in control (you do final narrative)
- ✅ Maintains texture (moment diversity visible)
- ✅ Keeps voice authentic (your thinking, not AI summary)

---

## Execution Approach

**Plan complete and saved to `docs/plans/2026-02-06-case-study-writing-system.md`**

**Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**