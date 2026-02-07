import json
from pathlib import Path
from typing import List
from scripts.moment_extractor import MomentExtractor
from scripts.narrative_builder import NarrativeBuilder


class CaseStudyWriter:
    """Orchestrates extraction and skeleton generation across all projects."""

    def __init__(self, timeline_dir: str):
        """
        Initialize the case study writer.

        Args:
            timeline_dir: Path to directory containing *-timeline.json files
        """
        self.timeline_dir = Path(timeline_dir)
        self.output_dir = self.timeline_dir.parent / "case-study-skeletons"
        self.moment_extractor = MomentExtractor()
        self.narrative_builder = NarrativeBuilder()

    def write_all_skeletons(self) -> List:
        """
        Extract moments and build skeletons for all projects.

        Process:
        1. Find all *-timeline.json files
        2. For each file:
           - Load timeline JSON
           - Extract moments using MomentExtractor
           - Build skeleton using NarrativeBuilder
           - Save skeleton to output directory
        3. Return list of all skeletons

        Returns:
            List of NarrativeSkeleton objects
        """
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

        skeletons = []

        # Find all timeline files
        timeline_files = sorted(self.timeline_dir.glob("*-timeline.json"))

        for timeline_file in timeline_files:
            try:
                # Extract project name from filename (remove -timeline.json suffix)
                project_name = timeline_file.stem.replace("-timeline", "")

                # Load timeline JSON
                with open(timeline_file, "r", encoding="utf-8") as f:
                    timeline_data = json.load(f)

                # Extract moments from timeline
                moments = self.moment_extractor.extract_moments(timeline_data)

                # Convert Moment objects to dictionaries for NarrativeBuilder
                moment_dicts = [
                    {
                        "type": moment.type.value,
                        "timestamp": moment.timestamp,
                        "content": moment.content,
                        "platform": moment.platform,
                        "snippet": moment.snippet,
                        "title": moment.title
                    }
                    for moment in moments
                ]

                # Build skeleton from moments
                skeleton = self.narrative_builder.build_skeleton(
                    project_name, moment_dicts
                )

                # Save skeleton to JSON file
                skeleton_file = self.output_dir / f"{project_name}-skeleton.json"
                self._save_skeleton(skeleton, skeleton_file)

                skeletons.append(skeleton)

            except Exception as e:
                print(f"Error processing {timeline_file.name}: {e}")
                continue

        return skeletons

    def _save_skeleton(self, skeleton, output_file: Path) -> None:
        """
        Save skeleton to JSON file.

        Args:
            skeleton: NarrativeSkeleton object to save
            output_file: Path where skeleton JSON will be saved
        """
        skeleton_data = {
            "project": skeleton.project,
            "constraint": skeleton.constraint,
            "arc": skeleton.arc,
            "platforms": skeleton.platforms,
            "timeline_span": skeleton.timeline_span,
            "texture_score": skeleton.texture_score,
            "source_snippets": skeleton.source_snippets
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(skeleton_data, f, indent=2, ensure_ascii=False)
