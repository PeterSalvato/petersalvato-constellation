# Case Study Extraction System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Ingest 3 chat export JSONs, semantically index them by project, reconstruct chronological project lineages across all platforms, extract verbatim thinking, and write guardrail-protected case studies grounded in actual history.

**Architecture:**
1. **Ingest Phase**: Load and parse 3 JSON exports (Gemini, ChatGPT, Claude)
2. **Index Phase**: Semantically map each chat to projects (Aetherwright, Savepoint, etc.)
3. **Lineage Phase**: Sort all mentions chronologically, reconstruct project evolution across platforms
4. **Extraction Phase**: Pull verbatim source material for each project
5. **Writing Phase**: Case study writing with guardrails checking against actual history
6. **Synthesis Phase**: Build cross-project colophon

**Tech Stack:** Python, JSON parsing, semantic matching (regex + LLM calls), chronological sorting, guardrail verification

---

## Core Philosophy

The system works backwards from actual history:

1. **Chat exports are the source of truth** - all case studies grounded in what actually happened
2. **Semantic indexing finds project mentions** across all 3 platforms (Gemini, ChatGPT, Claude)
3. **Chronological reconstruction** sorts mentions by timestamp across platforms to rebuild complete project evolution
4. **Guardrails prevent flattening** by:
   - Rejecting generic constraint statements
   - Requiring texture (complexity, pivots, failures) from timeline
   - Checking distinctiveness (could this be any project? NO = rejected)
   - Verifying voice/authenticity (sounds like actual thinking, not template)

---

## Input Data

**Three chat export files:**
- Gemini: `/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json`
- ChatGPT: `/home/peter/homelab/knowledge/exports/data-2026-01-26-15-50-54-batch-0000/conversations.json` (20.5MB)
- Claude: `/home/peter/homelab/knowledge/exports/7bb7d7448a4fe8b37c10d84958a3011b01d3dc5d3b4a88cb8a89ceea3ebda027-2026-01-22-18-47-51-f068f48a77d44e359188dc77169ae29d/conversations.json`

**Manifest (source of project definitions):**
- `/home/peter/homelab/projects/active/petersalvato.com/docs/mainfest.json`

---

## Task Breakdown

### Task 1: Design chat export schema

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/docs/plans/chat-extraction-schema.md`

**Step 1: Document the structure of each JSON export**

Understand what fields each platform uses:
- Gemini: `title`, `time`, `safeHtmlItem[].html` (HTML formatted)
- ChatGPT: (need to read sample to see structure)
- Claude: (need to read sample to see structure)

**Step 2: Create normalized schema**

```markdown
# Chat Export Schema

## Common Fields
- **id** (platform-specific)
- **timestamp** (ISO 8601)
- **title** (user prompt or subject)
- **content** (the actual conversation text)
- **platform** (gemini|chatgpt|claude)

## Platform-Specific Handling
- Gemini: Extract HTML from `safeHtmlItem[0].html`, convert to plain text
- ChatGPT: Map native JSON structure
- Claude: Map native JSON structure

## Semantic Indexing Fields
- **projects** (array of project IDs mentioned)
- **keywords** (key concepts: "Aetherwright", "ritual", "sovereignty", etc.)
- **chat_id** (unique identifier for this conversation)
```

**Step 3: Document semantic matching strategy**

```markdown
# Semantic Matching Rules

## High Confidence
- Exact project name mentions ("Aetherwright", "Savepoint", "Encore")
- Project IDs from manifest ("order-of-the-aetherwright", "savepoint-protocol")

## Medium Confidence
- Keywords ("ritual", "symbolic", "turning point", "cognitive")
- Related system names ("AI DevOps", "Portable Agency")

## Extraction
- Each chat tagged with projects it mentions
- Confidence score (high/medium) recorded
- Ambiguous chats flagged for manual review
```

**Step 4: Commit**

```bash
git add docs/plans/chat-extraction-schema.md
git commit -m "docs: define chat export schema and semantic indexing strategy"
```

---

### Task 2: Create chat ingest and parsing module

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/chat_ingest.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_chat_ingest.py`

**Step 1: Write failing test for Gemini parsing**

```python
# tests/test_chat_ingest.py
import json
from scripts.chat_ingest import GeminiParser

def test_gemini_parser_extracts_title():
    sample_gemini = {
        "title": "Prompted test subject",
        "time": "2026-01-26T13:04:42.022Z",
        "safeHtmlItem": [{"html": "<p>Test content</p>"}]
    }

    parser = GeminiParser()
    result = parser.parse_chat(sample_gemini)

    assert result["title"] == "Prompted test subject"
    assert result["timestamp"] == "2026-01-26T13:04:42.022Z"
    assert "<p>" not in result["content"]  # HTML stripped
    assert "Test content" in result["content"]

def test_gemini_parser_handles_missing_html():
    sample_gemini = {
        "title": "Test",
        "time": "2026-01-26T13:04:42.022Z",
        "safeHtmlItem": []
    }

    parser = GeminiParser()
    result = parser.parse_chat(sample_gemini)

    assert result["content"] == ""
```

**Step 2: Run test to verify it fails**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python -m pytest tests/test_chat_ingest.py::test_gemini_parser_extracts_title -v
```

Expected: `FAILED - ModuleNotFoundError: No module named 'scripts'`

**Step 3: Write minimal implementation**

```python
# scripts/chat_ingest.py
import re
from html.parser import HTMLParser

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = []

    def handle_data(self, d):
        self.text.append(d)

    def get_data(self):
        return ''.join(self.text)

def strip_html(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return stripper.get_data()

class GeminiParser:
    def parse_chat(self, chat_dict):
        """Parse a single Gemini activity entry"""
        title = chat_dict.get("title", "")
        timestamp = chat_dict.get("time", "")

        # Extract HTML content
        html_content = ""
        if "safeHtmlItem" in chat_dict and chat_dict["safeHtmlItem"]:
            html_content = chat_dict["safeHtmlItem"][0].get("html", "")

        # Strip HTML tags
        content = strip_html(html_content) if html_content else ""

        return {
            "title": title,
            "timestamp": timestamp,
            "content": content,
            "platform": "gemini"
        }
```

**Step 4: Run test to verify it passes**

```bash
python -m pytest tests/test_chat_ingest.py::test_gemini_parser_extracts_title -v
python -m pytest tests/test_chat_ingest.py -v
```

Expected: `PASSED`

**Step 5: Commit**

```bash
git add scripts/chat_ingest.py tests/test_chat_ingest.py
git commit -m "feat: add Gemini chat parser with HTML stripping"
```

---

### Task 3: Create file loading and multi-platform ingest

**Files:**
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/scripts/chat_ingest.py`
- Modify: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_chat_ingest.py`

**Step 1: Write failing test for loading Gemini JSON**

```python
def test_load_gemini_export():
    loader = ChatExportLoader()
    chats = loader.load_gemini(
        "/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json"
    )

    assert isinstance(chats, list)
    assert len(chats) > 0
    assert all("timestamp" in c for c in chats)
    assert all(c["platform"] == "gemini" for c in chats)
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_chat_ingest.py::test_load_gemini_export -v
```

**Step 3: Write implementation**

```python
# Add to scripts/chat_ingest.py
import json
from pathlib import Path
from typing import List, Dict

class ChatExportLoader:
    def __init__(self):
        self.gemini_parser = GeminiParser()

    def load_gemini(self, filepath: str) -> List[Dict]:
        """Load and parse Gemini activity export"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Gemini exports as array of activity items
        chats = []
        for item in data:
            parsed = self.gemini_parser.parse_chat(item)
            chats.append(parsed)

        return chats

    def load_all_exports(self, gemini_path: str, chatgpt_path: str, claude_path: str):
        """Load all three exports and combine"""
        all_chats = []

        # Load Gemini
        gemini_chats = self.load_gemini(gemini_path)
        all_chats.extend(gemini_chats)

        # TODO: Add ChatGPT loader
        # TODO: Add Claude loader

        return all_chats
```

**Step 4: Run test**

```bash
python -m pytest tests/test_chat_ingest.py::test_load_gemini_export -v
```

Expected: `PASSED`

**Step 5: Commit**

```bash
git add scripts/chat_ingest.py tests/test_chat_ingest.py
git commit -m "feat: add ChatExportLoader for Gemini JSON files"
```

---

### Task 4: Create semantic indexing module

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/semantic_index.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_semantic_index.py`

**Step 1: Write failing test for project mention detection**

```python
# tests/test_semantic_index.py
from scripts.semantic_index import SemanticIndexer

def test_detect_aetherwright_mention():
    indexer = SemanticIndexer()
    chat = {
        "title": "Order of the Aetherwright structure",
        "content": "The ritual framework for sovereign cognition...",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "order-of-the-aetherwright" in projects
    assert projects["order-of-the-aetherwright"]["confidence"] == "high"

def test_detect_savepoint_keyword():
    indexer = SemanticIndexer()
    chat = {
        "title": "Thinking about turning points",
        "content": "I need to mark where my understanding shifted, like a savepoint in thinking...",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "savepoint-protocol" in projects
    assert projects["savepoint-protocol"]["confidence"] == "medium"
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_semantic_index.py -v
```

**Step 3: Write implementation**

```python
# scripts/semantic_index.py
import re
from typing import Dict, List

class SemanticIndexer:
    # High-confidence exact matches
    PROJECT_NAMES = {
        "order-of-the-aetherwright": [
            r"(?i)aetherwright",
            r"(?i)order of the æ",
            r"(?i)sovereign cognition",
            r"(?i)ritual framework"
        ],
        "savepoint-protocol": [
            r"(?i)savepoint",
            r"(?i)semantic turning point",
            r"(?i)mark where.*changed",
            r"(?i)realization clicked"
        ],
        "ai-devops-workbench": [
            r"(?i)ai devops",
            r"(?i)vibecoding",
            r"(?i)architectural decisions"
        ],
        "encore": [
            r"(?i)enterprise platform",
            r"(?i)windows forms.*web",
            r"(?i)40,000.*users"
        ],
        "aiden-jae": [
            r"(?i)aiden.?jae",
            r"(?i)luxury.*jewelry",
            r"(?i)tropical.*organic"
        ],
        "modernist-homestead": [
            r"(?i)modernist homestead",
            r"(?i)neurodivergent.*scaffolding",
            r"(?i)home system"
        ]
    }

    def detect_projects(self, chat: Dict) -> Dict:
        """Detect which projects are mentioned in a chat"""
        title = chat.get("title", "")
        content = chat.get("content", "")
        full_text = f"{title} {content}"

        detected = {}

        for project_id, patterns in self.PROJECT_NAMES.items():
            for pattern in patterns:
                if re.search(pattern, full_text):
                    if project_id not in detected:
                        detected[project_id] = {
                            "confidence": "high",
                            "matched_pattern": pattern
                        }
                    break

        return detected

    def index_chat(self, chat: Dict) -> Dict:
        """Add project detection to a chat"""
        chat["detected_projects"] = self.detect_projects(chat)
        return chat
```

**Step 4: Run test**

```bash
python -m pytest tests/test_semantic_index.py -v
```

Expected: `PASSED`

**Step 5: Commit**

```bash
git add scripts/semantic_index.py tests/test_semantic_index.py
git commit -m "feat: add semantic project detection for chat indexing"
```

---

### Task 5: Create chronological lineage rebuilder

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/lineage_builder.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_lineage_builder.py`

**Step 1: Write failing test for sorting chats by project and time**

```python
# tests/test_lineage_builder.py
from scripts.lineage_builder import LineageBuilder
from datetime import datetime

def test_build_project_timeline():
    builder = LineageBuilder()

    chats = [
        {
            "timestamp": "2025-06-01T10:00:00Z",
            "title": "First Aetherwright idea",
            "detected_projects": {"order-of-the-aetherwright": {"confidence": "high"}}
        },
        {
            "timestamp": "2025-08-15T14:30:00Z",
            "title": "Aetherwright refinement",
            "detected_projects": {"order-of-the-aetherwright": {"confidence": "high"}}
        },
        {
            "timestamp": "2025-07-10T09:00:00Z",
            "title": "Savepoint research",
            "detected_projects": {"savepoint-protocol": {"confidence": "high"}}
        }
    ]

    timeline = builder.build_project_timeline(chats, "order-of-the-aetherwright")

    assert len(timeline) == 2
    assert timeline[0]["title"] == "First Aetherwright idea"
    assert timeline[1]["title"] == "Aetherwright refinement"
    assert timeline[0]["timestamp"] < timeline[1]["timestamp"]

def test_all_projects_timeline():
    builder = LineageBuilder()

    chats = [
        {
            "timestamp": "2025-06-01T10:00:00Z",
            "title": "Aetherwright",
            "detected_projects": {"order-of-the-aetherwright": {"confidence": "high"}}
        },
        {
            "timestamp": "2025-07-10T09:00:00Z",
            "title": "Savepoint",
            "detected_projects": {"savepoint-protocol": {"confidence": "high"}}
        }
    ]

    all_timelines = builder.build_all_project_timelines(chats)

    assert "order-of-the-aetherwright" in all_timelines
    assert "savepoint-protocol" in all_timelines
    assert len(all_timelines["order-of-the-aetherwright"]) == 1
    assert len(all_timelines["savepoint-protocol"]) == 1
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_lineage_builder.py -v
```

**Step 3: Write implementation**

```python
# scripts/lineage_builder.py
from typing import Dict, List
from datetime import datetime

class LineageBuilder:
    def build_project_timeline(self, chats: List[Dict], project_id: str) -> List[Dict]:
        """Build chronological timeline for a single project"""
        # Filter chats mentioning this project
        project_chats = [
            c for c in chats
            if project_id in c.get("detected_projects", {})
        ]

        # Sort by timestamp
        project_chats.sort(
            key=lambda c: datetime.fromisoformat(c["timestamp"].replace('Z', '+00:00'))
        )

        return project_chats

    def build_all_project_timelines(self, chats: List[Dict]) -> Dict[str, List[Dict]]:
        """Build timelines for all projects"""
        # Collect all project IDs
        all_projects = set()
        for chat in chats:
            projects = chat.get("detected_projects", {})
            all_projects.update(projects.keys())

        # Build timeline for each
        timelines = {}
        for project_id in sorted(all_projects):
            timelines[project_id] = self.build_project_timeline(chats, project_id)

        return timelines
```

**Step 4: Run test**

```bash
python -m pytest tests/test_lineage_builder.py -v
```

Expected: `PASSED`

**Step 5: Commit**

```bash
git add scripts/lineage_builder.py tests/test_lineage_builder.py
git commit -m "feat: add chronological lineage rebuilding for projects"
```

---

### Task 6: Create end-to-end pipeline

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/extract_case_studies.py`
- Modify: `tests/test_chat_ingest.py` (add integration test)

**Step 1: Write integration test**

```python
def test_end_to_end_extraction():
    """Load all chats, index them, build timelines, extract for Aetherwright"""
    from scripts.chat_ingest import ChatExportLoader
    from scripts.semantic_index import SemanticIndexer
    from scripts.lineage_builder import LineageBuilder

    # Load
    loader = ChatExportLoader()
    chats = loader.load_gemini(
        "/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json"
    )

    # Index
    indexer = SemanticIndexer()
    indexed_chats = [indexer.index_chat(c) for c in chats]

    # Build timelines
    builder = LineageBuilder()
    timelines = builder.build_all_project_timelines(indexed_chats)

    # Should have detected Aetherwright mentions
    assert "order-of-the-aetherwright" in timelines
    assert len(timelines["order-of-the-aetherwright"]) > 0
```

**Step 2: Run test**

```bash
python -m pytest tests/test_chat_ingest.py::test_end_to_end_extraction -v
```

Expected: `PASSED` (if Gemini file has Aetherwright mentions) or output shows detected projects

**Step 3: Create main extraction script**

```python
# scripts/extract_case_studies.py
import json
from pathlib import Path
from chat_ingest import ChatExportLoader
from semantic_index import SemanticIndexer
from lineage_builder import LineageBuilder

class CaseStudyExtractor:
    def __init__(self, gemini_path: str, chatgpt_path: str, claude_path: str):
        self.gemini_path = gemini_path
        self.chatgpt_path = chatgpt_path
        self.claude_path = claude_path
        self.loader = ChatExportLoader()
        self.indexer = SemanticIndexer()
        self.builder = LineageBuilder()

    def extract_all(self):
        """Run full extraction pipeline"""
        # Load all chats
        print("Loading chat exports...")
        all_chats = self.loader.load_all_exports(
            self.gemini_path,
            self.chatgpt_path,
            self.claude_path
        )
        print(f"Loaded {len(all_chats)} chats")

        # Index by project
        print("Indexing by project...")
        indexed_chats = [self.indexer.index_chat(c) for c in all_chats]

        # Build timelines
        print("Building project timelines...")
        timelines = self.builder.build_all_project_timelines(indexed_chats)

        # Save results
        output_dir = Path("docs/extraction-output")
        output_dir.mkdir(exist_ok=True)

        for project_id, timeline in timelines.items():
            output_file = output_dir / f"{project_id}-timeline.json"
            with open(output_file, 'w') as f:
                json.dump(timeline, f, indent=2)
            print(f"Wrote {len(timeline)} entries for {project_id}")

        return timelines

if __name__ == "__main__":
    extractor = CaseStudyExtractor(
        "/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json",
        "/home/peter/homelab/knowledge/exports/data-2026-01-26-15-50-54-batch-0000/conversations.json",
        "/home/peter/homelab/knowledge/exports/7bb7d7448a4fe8b37c10d84958a3011b01d3dc5d3b4a88cb8a89ceea3ebda027-2026-01-22-18-47-51-f068f48a77d44e359188dc77169ae29d/conversations.json"
    )
    timelines = extractor.extract_all()
```

**Step 4: Run to verify it works**

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python scripts/extract_case_studies.py
```

Expected: Outputs JSON files for each detected project with chronological chats

**Step 5: Commit**

```bash
git add scripts/extract_case_studies.py tests/test_chat_ingest.py
git commit -m "feat: add end-to-end case study extraction pipeline"
```

---

### Task 7: Add guardrail verification module

**Files:**
- Create: `/home/peter/homelab/projects/active/petersalvato.com/scripts/guardrails.py`
- Create: `/home/peter/homelab/projects/active/petersalvato.com/tests/test_guardrails.py`

**Step 1: Write failing test for guardrail checks**

```python
# tests/test_guardrails.py
from scripts.guardrails import CaseStudyGuardrails

def test_reject_generic_constraint():
    guardrails = CaseStudyGuardrails()

    draft = {
        "project": "aetherwright",
        "constraint": "Personal system for organizing work",  # Too generic
        "narrative": "I built a system to organize my thoughts"
    }

    result = guardrails.check_constraint_specificity(draft)

    assert not result["passes"]
    assert "too generic" in result["reason"].lower()

def test_accept_specific_constraint():
    guardrails = CaseStudyGuardrails()

    draft = {
        "project": "aetherwright",
        "constraint": "Resists tool fragmentation by using ritual to unify symbolic thinking, documentation, and practice across digital and physical domains",
        "narrative": "..."
    }

    result = guardrails.check_constraint_specificity(draft)

    assert result["passes"]

def test_check_texture_preservation():
    guardrails = CaseStudyGuardrails()

    timeline = [
        {"timestamp": "2025-06-01T10:00:00Z", "content": "Initial realization about ritual"},
        {"timestamp": "2025-07-15T14:00:00Z", "content": "First failure: generic tag system"},
        {"timestamp": "2025-08-20T09:00:00Z", "content": "Pivot to markup language"}
    ]

    result = guardrails.check_timeline_texture(timeline)

    assert result["passes"]
    assert "pivot" in result["findings"].lower()
    assert len(result["key_moments"]) == 3
```

**Step 2: Run test to verify it fails**

```bash
python -m pytest tests/test_guardrails.py -v
```

**Step 3: Write implementation**

```python
# scripts/guardrails.py
from typing import Dict, List

class CaseStudyGuardrails:
    GENERIC_PHRASES = [
        r"(?i)personal system",
        r"(?i)organize.*work",
        r"(?i)productivity tool",
        r"(?i)management system",
        r"(?i)platform for.*work"
    ]

    def check_constraint_specificity(self, draft: Dict) -> Dict:
        """Reject if constraint is generic"""
        import re
        constraint = draft.get("constraint", "")

        for pattern in self.GENERIC_PHRASES:
            if re.search(pattern, constraint):
                return {
                    "passes": False,
                    "reason": f"Constraint is too generic: matches '{pattern}'",
                    "suggestion": "Explain specifically what problem this solves that others don't"
                }

        # Check length (too short = likely generic)
        if len(constraint) < 50:
            return {
                "passes": False,
                "reason": "Constraint is too brief to be specific",
                "suggestion": "Expand to show what makes this problem unique"
            }

        return {"passes": True, "reason": "Constraint is specific"}

    def check_timeline_texture(self, timeline: List[Dict]) -> Dict:
        """Verify timeline shows complexity, not just success"""
        findings = {
            "passes": True,
            "findings": [],
            "key_moments": []
        }

        # Check for pivot/failure moments
        failure_keywords = ["failed", "pivot", "realized", "broke", "didn't work"]
        complexity_count = 0

        for entry in timeline:
            content = entry.get("content", "").lower()

            for keyword in failure_keywords:
                if keyword in content:
                    complexity_count += 1
                    findings["key_moments"].append({
                        "timestamp": entry.get("timestamp"),
                        "type": keyword,
                        "snippet": entry.get("content")[:100]
                    })
                    break

        if complexity_count == 0:
            findings["passes"] = False
            findings["findings"].append("Timeline shows only success, no complexity/pivots/failures")

        if complexity_count >= 1:
            findings["findings"].append(f"Found {complexity_count} complexity moment(s)")

        return findings

    def check_distinctiveness(self, timeline: List[Dict]) -> Dict:
        """Verify project is not interchangeable with others"""
        content_combined = " ".join([e.get("content", "") for e in timeline])

        # Check if specific project concepts appear
        # (This is simplified; in reality would check against other project timelines)

        return {
            "passes": True,
            "comment": "Manual review recommended for distinctiveness"
        }
```

**Step 4: Run test**

```bash
python -m pytest tests/test_guardrails.py -v
```

Expected: `PASSED`

**Step 5: Commit**

```bash
git add scripts/guardrails.py tests/test_guardrails.py
git commit -m "feat: add guardrail verification for case study specificity and texture"
```

---

## Next Phase: Writing with Guardrails

Once extraction is complete:

1. **Agent 4: Writing** - Takes timeline + guardrails, writes case study draft
2. **Agent 5: Voice + Privacy Check** - Verifies voice, checks for sensitive data, validates specificity
3. **Agent 6: Colophon Synthesis** - Builds cross-project narrative from all case studies

---

## Key Decisions (Locked In)

- **Source of truth**: Chat exports (verbatim conversations)
- **Semantic indexing**: Regex-based pattern matching + future LLM enhancement
- **Chronological reconstruction**: Timestamps across all 3 platforms
- **Guardrails**: Prevent flattening through specificity/texture/distinctiveness checks
- **Output**: JSON timelines → Case study drafts → Final published narratives

---

## How to Execute

Save this plan and invoke: `superpowers:executing-plans` in a new session with separate worktree, OR use `superpowers:subagent-driven-development` to dispatch tasks in parallel.
