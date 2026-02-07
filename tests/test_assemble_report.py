from scripts.assemble_report import AssemblyReporter

def test_generate_assembly_report():
    reporter = AssemblyReporter()

    report = reporter.generate_report(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output",
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons"
    )

    assert report["total_projects"] == 17
    assert report["total_entries"] >= 2300
    assert "summary_md" in report
    assert "validations" in report
