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
