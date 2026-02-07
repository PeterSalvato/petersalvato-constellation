import json
import os
from pathlib import Path
from typing import Dict, List, Any
from scripts.skeleton_guardrails import SkeletonGuardrails


class AssemblyReporter:
    """Generates a comprehensive report of all project skeletons and their validation status."""

    def __init__(self):
        """Initialize the reporter with guardrails validator."""
        self.guardrails = SkeletonGuardrails()

    def generate_report(self, timeline_dir: str, skeleton_dir: str) -> Dict[str, Any]:
        """
        Generate a comprehensive assembly report.

        Args:
            timeline_dir: Directory containing timeline JSON files
            skeleton_dir: Directory containing skeleton JSON files

        Returns:
            Dictionary containing:
                - total_projects: Count of projects
                - total_entries: Total arc entries across all projects
                - skeletons: Dict of all loaded skeletons
                - validations: List of validation results
                - summary_md: Markdown report with table
        """
        # Load all skeleton files
        skeletons = self._load_skeletons(skeleton_dir)

        # Validate each skeleton and collect metrics
        validations = []
        total_entries = 0

        for project_name, skeleton in skeletons.items():
            # Validate using guardrails
            validation = self.guardrails.validate(skeleton)

            # Count entries in arc
            arc = skeleton.get("arc", [])
            entry_count = len(arc)
            total_entries += entry_count

            # Extract platforms if available
            platforms = skeleton.get("platforms", [])
            if isinstance(platforms, list):
                platform_count = len(platforms)
            else:
                platform_count = 0

            # Build validation record
            validation_record = {
                "project": project_name,
                "entries": entry_count,
                "texture_score": validation.get("texture_score", 0.0),
                "platforms": platform_count,
                "passes": validation.get("passes", False),
                "issues": validation.get("issues", []),
                "constraint_length": validation.get("constraint_length", 0),
                "arc_diversity": validation.get("arc_diversity", 0)
            }

            validations.append(validation_record)

        # Generate markdown summary
        summary_md = self._generate_markdown(skeletons, validations)

        return {
            "total_projects": len(skeletons),
            "total_entries": total_entries,
            "skeletons": skeletons,
            "validations": validations,
            "summary_md": summary_md
        }

    def _load_skeletons(self, skeleton_dir: str) -> Dict[str, Dict[str, Any]]:
        """
        Load all skeleton JSON files from a directory.

        Args:
            skeleton_dir: Path to directory containing skeleton JSON files

        Returns:
            Dictionary mapping project names to skeleton data
        """
        skeletons = {}
        skeleton_path = Path(skeleton_dir)

        # Find all *-skeleton.json files
        for json_file in sorted(skeleton_path.glob("*-skeleton.json")):
            project_name = json_file.stem.replace("-skeleton", "")

            try:
                with open(json_file, 'r') as f:
                    skeleton = json.load(f)
                    skeletons[project_name] = skeleton
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to load {json_file.name}: {e}")
                continue

        return skeletons

    def _generate_markdown(self, skeletons: Dict[str, Any], validations: List[Dict[str, Any]]) -> str:
        """
        Generate a markdown report with project metrics and validation status.

        Args:
            skeletons: Dictionary of loaded skeletons
            validations: List of validation results

        Returns:
            Formatted markdown string
        """
        # Header with summary counts
        total_projects = len(skeletons)
        total_entries = sum(v["entries"] for v in validations)
        passing = sum(1 for v in validations if v["passes"])
        needs_review = total_projects - passing

        markdown = f"""# Narrative Assembly Report

## Summary

- **Total Projects:** {total_projects}
- **Total Arc Entries:** {total_entries}
- **Validation Status:** {passing} passing ✅ | {needs_review} need review ⚠️

---

## Project Details

| Project | Entries | Texture | Platforms | Arc Diversity | Status |
|---------|---------|---------|-----------|---------------|--------|
"""

        # Add rows for each project
        for validation in sorted(validations, key=lambda v: v["project"]):
            project = validation["project"]
            entries = validation["entries"]
            texture = f"{validation['texture_score']:.2f}"
            platforms = validation["platforms"]
            arc_div = validation["arc_diversity"]
            status = "✅ PASS" if validation["passes"] else "❌ REVIEW"

            markdown += f"| {project} | {entries} | {texture} | {platforms} | {arc_div} | {status} |\n"

        # Add validation issues section if any
        issues_to_report = [v for v in validations if not v["passes"]]
        if issues_to_report:
            markdown += "\n---\n\n## Validation Issues Requiring Review\n\n"

            for validation in issues_to_report:
                markdown += f"### {validation['project']}\n\n"
                for issue in validation["issues"]:
                    markdown += f"- {issue}\n"
                markdown += "\n"

        return markdown
