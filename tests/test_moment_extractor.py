from scripts.moment_extractor import MomentExtractor, MomentType


def test_extract_genesis_moment():
    extractor = MomentExtractor()
    timeline = [
        {
            "title": "First idea about Savepoint",
            "timestamp": "2024-09-30T10:00:00Z",
            "content": "I need a way to mark where my thinking changed, not just what I thought",
            "platform": "claude"
        }
    ]

    moments = extractor.extract_moments(timeline)

    assert len(moments) > 0
    assert moments[0].type == MomentType.GENESIS
    assert "mark where" in moments[0].snippet.lower()


def test_detect_pivot_keyword():
    extractor = MomentExtractor()
    content = "I tried tagging first, but that didn't work. Then I realized it should be markup language."

    moment_type = extractor.detect_moment_type(content)

    assert moment_type == MomentType.PIVOT


def test_moment_has_all_fields():
    extractor = MomentExtractor()
    timeline = [
        {
            "title": "Test moment",
            "timestamp": "2024-01-01T00:00:00Z",
            "content": "I realized something important",
            "platform": "claude"
        }
    ]

    moments = extractor.extract_moments(timeline)

    assert len(moments) == 1
    moment = moments[0]
    assert moment.type == MomentType.REALIZATION
    assert moment.timestamp == "2024-01-01T00:00:00Z"
    assert moment.platform == "claude"
    assert moment.title == "Test moment"
    assert len(moment.snippet) > 0


def test_extract_snippet_truncation():
    extractor = MomentExtractor()
    long_content = "I discovered " + "a" * 200 + " pattern in the data"

    snippet = extractor._extract_snippet(long_content)

    assert len(snippet) <= 160  # Should be truncated
    assert "..." in snippet or len(snippet) < len(long_content)


def test_multiple_moments_in_timeline():
    extractor = MomentExtractor()
    timeline = [
        {
            "title": "Genesis",
            "timestamp": "2024-01-01T00:00:00Z",
            "content": "Initial idea about building something",
            "platform": "claude"
        },
        {
            "title": "Problem",
            "timestamp": "2024-01-02T00:00:00Z",
            "content": "The approach broke when I tried it",
            "platform": "claude"
        },
        {
            "title": "Pivot",
            "timestamp": "2024-01-03T00:00:00Z",
            "content": "I tried the first approach but switched to something else instead",
            "platform": "claude"
        },
        {
            "title": "Validation",
            "timestamp": "2024-01-04T00:00:00Z",
            "content": "The new approach works great",
            "platform": "claude"
        }
    ]

    moments = extractor.extract_moments(timeline)

    assert len(moments) == 4
    types = [m.type for m in moments]
    assert MomentType.GENESIS in types
    assert MomentType.PROBLEM in types
    assert MomentType.PIVOT in types
    assert MomentType.VALIDATION in types


def test_empty_timeline():
    extractor = MomentExtractor()
    moments = extractor.extract_moments([])
    assert len(moments) == 0


def test_moment_with_no_content():
    extractor = MomentExtractor()
    timeline = [
        {
            "title": "Empty entry",
            "timestamp": "2024-01-01T00:00:00Z",
            "content": "",
            "platform": "claude"
        }
    ]

    moments = extractor.extract_moments(timeline)

    assert len(moments) == 0


def test_all_moment_types_detected():
    extractor = MomentExtractor()
    test_cases = [
        ("I started with this idea", MomentType.GENESIS),
        ("I realized something important", MomentType.REALIZATION),
        ("This didn't work", MomentType.PROBLEM),
        ("I tried that but switched instead", MomentType.PIVOT),
        ("I refined the approach", MomentType.REFINEMENT),
        ("I integrated the components", MomentType.INTEGRATION),
        ("I tested and validated it works", MomentType.VALIDATION),
        ("I built a new tool", MomentType.ARTIFACT),
    ]

    for content, expected_type in test_cases:
        detected_type = extractor.detect_moment_type(content)
        assert detected_type == expected_type, f"Failed for '{content}': got {detected_type}, expected {expected_type}"
