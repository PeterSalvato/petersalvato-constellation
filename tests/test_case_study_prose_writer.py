from scripts.case_study_prose_writer import CaseStudyProseWriter

def test_write_all_case_study_prose():
    writer = CaseStudyProseWriter(
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons",
        conversation_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    prose_docs = writer.write_all_prose()

    assert len(prose_docs) >= 17
    assert all(doc.get("project") for doc in prose_docs)
    assert all(doc.get("prose") for doc in prose_docs)
    assert all(doc.get("validation") for doc in prose_docs)
