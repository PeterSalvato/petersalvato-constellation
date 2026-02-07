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
