#!/usr/bin/env python3
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
        output_dir.mkdir(exist_ok=True, parents=True)

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
