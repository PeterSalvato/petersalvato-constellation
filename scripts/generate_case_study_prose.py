#!/usr/bin/env python3
"""
Generate case study prose for all 17 projects using Craftsman Voice Protocol.
Uses skeleton files as input and writes prose to docs/case-study-prose/
"""

import json
import sys
from pathlib import Path


def extract_skeleton_context(skeleton_file):
    """Extract key information from skeleton for prose generation."""
    with open(skeleton_file) as f:
        data = json.load(f)

    project = data.get("project", "unknown")
    constraint = data.get("constraint", "")
    arc = data.get("arc", [])

    # Extract key moments by type
    moments_by_type = {}
    for moment in arc:
        mtype = moment.get("type")
        if mtype not in moments_by_type:
            moments_by_type[mtype] = []
        moments_by_type[mtype].append(moment)

    # Get timeline span
    timestamps = [m.get("timestamp", "") for m in arc if m.get("timestamp")]
    timeline_span = f"{timestamps[0]} to {timestamps[-1]}" if timestamps else "unknown"

    # Get key snippets (first 3 of each type)
    key_snippets = []
    for mtype in ["genesis", "problem", "pivot", "validation"]:
        if mtype in moments_by_type:
            for moment in moments_by_type[mtype][:1]:  # Just first of each type
                snippet = moment.get("snippet", "")
                if snippet:
                    key_snippets.append(f"[{mtype.upper()}] {snippet}")

    return {
        "project": project,
        "constraint": constraint,
        "arc_length": len(arc),
        "moment_types": {k: len(v) for k, v in moments_by_type.items()},
        "timeline_span": timeline_span,
        "key_snippets": key_snippets[:5],  # Top 5 snippets
        "full_arc": arc
    }


def generate_prose_prompt(context):
    """Generate a prompt for prose generation from skeleton context."""
    project = context["project"]
    constraint = context["constraint"]
    key_snippets = context["key_snippets"]

    snippet_text = "\n".join(key_snippets)

    prompt = f"""Generate a case study for "{project}" using ONLY the Craftsman Voice Protocol.

CONSTRAINT (the driving problem):
{constraint[:200]}...

KEY NARRATIVE MOMENTS:
{snippet_text}

TOTAL MOMENTS: {context['arc_length']}
MOMENT DISTRIBUTION: {context['moment_types']}
TIMELINE: {context['timeline_span']}

REQUIREMENTS:
1. Write 800-1200 words in Craftsman Voice (show don't tell)
2. Lead with "I built..." - demonstrate what was created
3. Ground every claim in actual moments from the narrative arc
4. Use concrete verbs: hold, break, craft, land, drifts, scaffold
5. Show thinking evolution through moments (genesis → problem → pivot → validation)
6. No hype, theater, or explanation - only consequence
7. Mentor-to-apprentice tone: use "you" for demonstration, "I" for authority
8. Show what didn't work and why the solution survives the constraint

Generate the prose now."""

    return prompt


def main():
    skeleton_dir = Path("/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons")
    prose_dir = Path("/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-prose")
    prose_dir.mkdir(exist_ok=True)

    print("=" * 70)
    print("CASE STUDY PROSE GENERATION")
    print("=" * 70)
    print()

    projects = sorted([f for f in skeleton_dir.glob("*-skeleton.json")])
    print(f"Found {len(projects)} skeleton files")
    print()

    # Extract all contexts first
    contexts = {}
    for skeleton_file in projects:
        project_name = skeleton_file.stem.replace("-skeleton", "")
        try:
            context = extract_skeleton_context(skeleton_file)
            contexts[project_name] = context
            print(f"✓ {project_name}: {context['arc_length']} moments")
        except Exception as e:
            print(f"✗ {project_name}: {e}")

    print()
    print("=" * 70)
    print("PROSE GENERATION READY")
    print("=" * 70)
    print()
    print("Generated prompts for all projects. Now invoke prose generation skill")
    print("for each project to create actual case study prose.")
    print()

    # Output project list and key stats
    print("Projects to generate:")
    for project_name in sorted(contexts.keys()):
        ctx = contexts[project_name]
        print(f"  - {project_name}: {ctx['arc_length']} moments, {dict(ctx['moment_types'])}")

    return contexts


if __name__ == "__main__":
    contexts = main()
