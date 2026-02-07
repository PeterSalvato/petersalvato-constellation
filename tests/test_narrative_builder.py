from scripts.narrative_builder import NarrativeBuilder, NarrativeSkeleton


def test_build_narrative_skeleton():
    builder = NarrativeBuilder()

    moments = [
        {
            "type": "genesis",
            "timestamp": "2024-09-30T10:00:00Z",
            "snippet": "I need to mark where my thinking changed"
        },
        {
            "type": "problem",
            "timestamp": "2024-10-05T14:30:00Z",
            "snippet": "Tagging systems don't capture the shift"
        },
        {
            "type": "pivot",
            "timestamp": "2024-10-15T09:00:00Z",
            "snippet": "Markup language preserves the moment"
        },
        {
            "type": "validation",
            "timestamp": "2024-11-01T16:00:00Z",
            "snippet": "This approach captures inflection points"
        }
    ]

    skeleton = builder.build_skeleton("savepoint-protocol", moments)

    assert skeleton.project == "savepoint-protocol"
    assert skeleton.constraint is not None
    assert skeleton.arc is not None
    assert len(skeleton.arc) >= 3


def test_skeleton_has_quotations():
    builder = NarrativeBuilder()

    moments = [{"type": "genesis", "timestamp": "2024-09-30T10:00:00Z",
                "snippet": "First idea"}]

    skeleton = builder.build_skeleton("test-project", moments)

    assert any(m.get("snippet") for m in skeleton.arc)
