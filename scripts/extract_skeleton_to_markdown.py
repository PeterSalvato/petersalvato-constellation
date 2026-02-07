#!/usr/bin/env python3
"""
Extract skeleton moments from raw chat timelines into markdown document.

Given a skeleton file and its corresponding timeline, this tool:
1. Loads skeleton (index of moments to extract)
2. Loads timeline (raw chat data)
3. For each skeleton moment, finds it in timeline
4. Extracts the passage with line numbers
5. Outputs markdown file with all moments in sequence

Usage:
  python extract_skeleton_to_markdown.py <project_name>

Output:
  docs/extraction-output/{project_name}-extraction.md
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def load_skeleton(project_name: str) -> Dict:
    """Load skeleton JSON for project."""
    skeleton_file = Path(
        "/home/peter/homelab/projects/active/petersalvato.com"
        f"/docs/case-study-skeletons/{project_name}-skeleton.json"
    )
    with open(skeleton_file) as f:
        return json.load(f)


def load_timeline(project_name: str) -> List[Dict]:
    """Load timeline JSON (raw chats) for project."""
    timeline_file = Path(
        "/home/peter/homelab/projects/active/petersalvato.com"
        f"/docs/extraction-output/{project_name}-timeline.json"
    )
    with open(timeline_file) as f:
        data = json.load(f)

    # Timeline might be wrapped or be direct list
    if isinstance(data, dict) and "arc" in data:
        return data["arc"]
    elif isinstance(data, list):
        return data
    else:
        raise ValueError(f"Unexpected timeline structure: {type(data)}")


def find_moment_in_timeline(
    moment: Dict, timeline: List[Dict]
) -> Optional[Tuple[int, Dict]]:
    """
    Find a skeleton moment in the timeline.

    Returns: (line_number, timeline_entry) or None
    """
    snippet = moment.get("snippet", "").lower().strip()
    timestamp = moment.get("timestamp", "")

    # Search by snippet first (most reliable)
    for i, entry in enumerate(timeline):
        content = entry.get("content", "").lower().strip()
        if snippet and snippet in content:
            return (i, entry)

    # Fallback: search by timestamp
    for i, entry in enumerate(timeline):
        entry_timestamp = entry.get("timestamp", "")
        if timestamp and entry_timestamp == timestamp:
            return (i, entry)

    return None


def extract_passage(
    moment: Dict, timeline_entry: Dict
) -> str:
    """Extract relevant passage from timeline entry, focusing on the skeleton snippet."""
    content = timeline_entry.get("content", "")
    snippet = moment.get("snippet", "")
    timestamp = timeline_entry.get("timestamp", "")

    # If content is very large (> 2000 chars), try to extract just the relevant section
    if len(content) > 2000 and snippet:
        # Find the snippet in content and extract surrounding context
        snippet_lower = snippet.lower()
        content_lower = content.lower()
        idx = content_lower.find(snippet_lower)

        if idx >= 0:
            # Extract snippet + surrounding context (500 chars before/after)
            start = max(0, idx - 500)
            end = min(len(content), idx + len(snippet) + 500)
            passage = content[start:end]

            # Add ellipsis if truncated
            if start > 0:
                passage = "..." + passage
            if end < len(content):
                passage = passage + "..."
        else:
            # Fallback: take first 1000 chars
            passage = content[:1000] + "..." if len(content) > 1000 else content
    else:
        passage = content

    return f"**[{timestamp}]**\n\n{passage}"


def extract_all_moments(project_name: str) -> str:
    """Extract all skeleton moments to markdown."""
    skeleton = load_skeleton(project_name)
    timeline = load_timeline(project_name)

    project_display = project_name.replace("-", " ").title()
    manifest = skeleton.get("constraint", "")
    arc = skeleton.get("arc", [])

    # Build markdown
    md = f"# {project_display} - Prose Extraction Source\n\n"
    md += f"**Manifest:** {manifest[:200]}...\n\n"
    md += f"**Total moments:** {len(arc)}\n\n"
    md += "---\n\n"
    md += "## Extracted Moments\n\n"

    found_count = 0
    not_found = []

    for i, moment in enumerate(arc, 1):
        moment_type = moment.get("type", "unknown")
        timestamp = moment.get("timestamp", "unknown")
        snippet = moment.get("snippet", "")[:100]

        # Find in timeline
        result = find_moment_in_timeline(moment, timeline)

        if result:
            line_num, timeline_entry = result
            passage = extract_passage(moment, timeline_entry)
            found_count += 1

            md += f"### Moment {i}: [{moment_type.upper()}] - {timestamp}\n\n"
            md += f"**Skeleton snippet:** \"{snippet}...\"\n\n"
            md += f"**Source:** line {line_num}\n\n"
            md += f"**Passage:**\n\n```\n{passage}\n```\n\n"
            md += "---\n\n"
        else:
            not_found.append((i, moment_type, snippet))

    # Add summary
    md += f"\n## Summary\n\n"
    md += f"- **Total moments:** {len(arc)}\n"
    md += f"- **Found:** {found_count}\n"
    md += f"- **Not found:** {len(not_found)}\n\n"

    if not_found:
        md += "### Not Found Moments\n\n"
        for idx, mtype, snippet in not_found:
            md += f"- Moment {idx} [{mtype}]: {snippet}\n"

    return md


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_skeleton_to_markdown.py <project_name>")
        print("Example: python extract_skeleton_to_markdown.py order-of-the-aetherwright")
        sys.exit(1)

    project_name = sys.argv[1]

    print(f"Extracting {project_name}...")
    print(f"  Loading skeleton...")
    print(f"  Loading timeline...")

    markdown = extract_all_moments(project_name)

    output_file = Path(
        "/home/peter/homelab/projects/active/petersalvato.com"
        f"/docs/extraction-output/{project_name}-extraction.md"
    )

    with open(output_file, "w") as f:
        f.write(markdown)

    print(f"✓ Extraction complete: {output_file}")
    print(f"  Size: {len(markdown)} bytes")


if __name__ == "__main__":
    main()
