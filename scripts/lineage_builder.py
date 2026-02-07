# scripts/lineage_builder.py
from typing import Dict, List
from datetime import datetime, timezone

class LineageBuilder:
    def build_project_timeline(self, chats: List[Dict], project_id: str) -> List[Dict]:
        """Build chronological timeline for a single project"""
        # Filter chats mentioning this project
        project_chats = [
            c for c in chats
            if project_id in c.get("detected_projects", {})
        ]

        # Sort by timestamp (normalize all to naive UTC)
        def parse_timestamp(ts_str):
            try:
                if not ts_str:
                    return datetime.min
                # Parse and convert to naive UTC datetime
                if ts_str.endswith('Z'):
                    dt = datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
                else:
                    dt = datetime.fromisoformat(ts_str)

                # Convert to naive UTC if aware
                if dt.tzinfo is not None:
                    dt = dt.replace(tzinfo=None)

                return dt
            except:
                # Return epoch as fallback for invalid timestamps
                return datetime.min

        project_chats.sort(
            key=lambda c: parse_timestamp(c.get("timestamp", ""))
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
