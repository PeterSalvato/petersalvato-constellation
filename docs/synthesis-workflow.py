#!/usr/bin/env python3
"""
NotebookLM Synthesis Workflow for Case Study Extraction

Extract narrative arcs from manifest + extraction timeline using NotebookLM.
This script is the Timeline Narrator Specialist's primary tool.

Usage:
    python3 synthesis-workflow.py savepoint-protocol
    python3 synthesis-workflow.py aiden-jae
    python3 synthesis-workflow.py encore

Output:
    - docs/working/outline-[project].md (structured narrative arc)
    - docs/working/synthesis-[project].txt (raw NotebookLM response)
"""

import sys
import json
import os
from pathlib import Path
from datetime import datetime

# Add NotebookLM MCP to path
sys.path.insert(0, str(Path.home() / '.claude' / 'notebooklm-mcp' / 'src'))

def load_manifest():
    """Load manifest.json and return as dict."""
    manifest_path = Path('docs/mainfest.json')
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    with open(manifest_path) as f:
        return json.load(f)

def find_project_in_manifest(manifest, project_slug):
    """Find project by slug in manifest structure."""
    site_manifest = manifest.get('site_manifest', {})

    # Search through all tiers
    for tier_key in ['tier_01_protocols', 'tier_02_applied_systems', 'tier_03_practice']:
        tier = site_manifest.get(tier_key, {})
        for project in tier.get('projects', []):
            if project.get('id') == project_slug:
                return project, tier_key

    raise ValueError(f"Project not found: {project_slug}")

def load_extraction_timeline(project_slug):
    """Load extraction timeline for project."""
    timeline_path = Path(f'docs/extraction_timelines/{project_slug}-timeline.md')
    if not timeline_path.exists():
        raise FileNotFoundError(f"Timeline not found: {timeline_path}")

    with open(timeline_path) as f:
        return f.read()

def run_synthesis(project_slug, project_info, timeline_text):
    """
    Run NotebookLM synthesis.

    Returns tuple: (notebook_id, synthesis_response)
    """
    from notebooklm_mcp.api_client import NotebookLMClient
    from notebooklm_mcp.auth import load_cached_tokens

    # Load cached auth
    try:
        cached_tokens = load_cached_tokens()
        if not cached_tokens or not cached_tokens.cookies:
            raise ValueError("No cached auth tokens")
    except Exception as e:
        print(f"\n✗ Authentication Error: {e}")
        print(f"\nTo authenticate, run:")
        print(f"  cd ~/.claude/notebooklm-mcp && source venv/bin/activate")
        print(f"  notebooklm-mcp-auth --file")
        print(f"  (Follow the Chrome DevTools extraction steps)")
        raise

    # Initialize client
    client = NotebookLMClient(cookies=cached_tokens.cookies)

    # Build manifest text
    manifest_text = f"""# {project_info['name']} - Manifest Entry

**Mission Statement:**
{project_info['mission_statement']}

**Plain Spoken Lesson:**
{project_info['plain_spoken_lesson']}

**Defense Against Drift:**
{project_info['defense_against_drift']}

**Description:**
{project_info.get('description', 'N/A')}
"""

    # Create notebook
    print(f"\n[1/4] Creating NotebookLM notebook...")
    notebook = client.create_notebook(
        name=f"{project_info['name']} - Synthesis",
        description="Extract narrative from manifest + timeline"
    )
    notebook_id = notebook.get('id')
    print(f"✓ Notebook: {notebook_id}")

    # Add manifest
    print(f"[2/4] Adding manifest source...")
    client.add_text_source(
        notebook_id=notebook_id,
        text=manifest_text,
        title="Manifest Entry"
    )
    print(f"✓ Manifest added")

    # Add timeline
    print(f"[3/4] Adding extraction timeline...")
    client.add_text_source(
        notebook_id=notebook_id,
        text=timeline_text,
        title="Extraction Timeline"
    )
    print(f"✓ Timeline added")

    # Run synthesis query
    print(f"[4/4] Running synthesis query...")
    response = client.query(
        notebook_id=notebook_id,
        query="""Reading both the manifest and the extraction timeline together:

1. What is the actual story of this system?
2. What was the arc from initial conception to what it became?
3. What key moments or decisions changed the thinking?
4. What from the manifest mission survived to reality?
5. What problems did it solve?

Please structure your answer chronologically with specific moments from the timeline.
Mark where the narrative connects to the manifest mission."""
    )

    print(f"✓ Synthesis complete")

    return notebook_id, response

def write_outline(project_slug, response):
    """
    Extract structured outline from synthesis response.
    Write to docs/working/outline-[project].md
    """
    outline_path = Path(f'docs/working/outline-{project_slug}.md')
    outline_path.parent.mkdir(parents=True, exist_ok=True)

    answer = response.get('answer', '')

    outline_content = f"""# {project_slug} - Narrative Outline

**Generated:** {datetime.now().isoformat()}
**Synthesis Method:** NotebookLM (manifest + extraction timeline)

---

## Raw Synthesis Response

{answer}

---

## Timeline for Master Builder Copywriter

Use the events and arc identified above to write the case study in three parts:

1. **The System** (100-150 words)
   - What it IS, stated directly
   - Mission reframed conversationally

2. **Why I Needed to Make It** (300-500 words)
   - The actual problem/constraint
   - Why this mattered
   - Source: manifest context + timeline context

3. **How I Did It** (800-1200 words)
   - Chronological story from timeline
   - Follow the actual arc identified above
   - Show decisions, survival, evolution
   - Source: sanitized timeline

---

## Next Step

Pass this outline to Master Builder Copywriter with the source timeline.
Master Builder will write docs/working/draft-{project_slug}.md
"""

    with open(outline_path, 'w') as f:
        f.write(outline_content)

    print(f"\n✓ Outline written: {outline_path}")
    return outline_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 synthesis-workflow.py [project-slug]")
        print("\nExamples:")
        print("  python3 synthesis-workflow.py savepoint-protocol")
        print("  python3 synthesis-workflow.py aiden-jae")
        print("  python3 synthesis-workflow.py encore")
        sys.exit(1)

    project_slug = sys.argv[1]

    print("="*70)
    print(f"NotebookLM Synthesis: {project_slug}")
    print("="*70)

    try:
        # Load data
        print(f"\nLoading manifest and timeline...")
        manifest = load_manifest()
        project_info, tier = find_project_in_manifest(manifest, project_slug)
        timeline = load_extraction_timeline(project_slug)

        print(f"✓ Manifest loaded: {project_info['name']}")
        print(f"✓ Timeline loaded: {len(timeline)} characters")

        # Run synthesis
        notebook_id, response = run_synthesis(project_slug, project_info, timeline)

        # Write output
        outline_path = write_outline(project_slug, response)

        print("\n" + "="*70)
        print(f"✓ SUCCESS: {project_slug}")
        print("="*70)
        print(f"\nNext: Pass outline to Master Builder Copywriter")
        print(f"Outline file: {outline_path}")

    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
