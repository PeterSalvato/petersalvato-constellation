from scripts.case_study_writer import CaseStudyWriter
import json


def test_write_all_case_study_skeletons():
    writer = CaseStudyWriter(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    skeletons = writer.write_all_skeletons()

    assert len(skeletons) >= 17
    assert all(s.project for s in skeletons)
    assert all(s.constraint for s in skeletons)
    assert all(s.arc for s in skeletons)


def test_skeleton_has_texture():
    writer = CaseStudyWriter(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    skeletons = writer.write_all_skeletons()

    # All skeletons should have texture score > 0
    assert all(s.texture_score > 0 for s in skeletons)
