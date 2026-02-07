#!/usr/bin/env python3
"""
Task 6: Skeleton Generation Runner
Orchestrates full system to generate case study skeletons for all 17 projects.
"""

from case_study_writer import CaseStudyWriter
from assemble_report import AssemblyReporter
from pathlib import Path


def main():
    print("=" * 70)
    print("CASE STUDY SKELETON GENERATION - FINAL ASSEMBLY")
    print("=" * 70)
    print()

    # Step 1: Generate skeletons for all projects
    print("Step 1: Generating case study skeletons for all 17 projects...")
    print()

    writer = CaseStudyWriter(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )
    skeletons = writer.write_all_skeletons()

    print(f"✓ Generated {len(skeletons)} narrative skeletons")
    print()

    # Step 2: Generate comprehensive report
    print("Step 2: Generating assembly report...")
    print()

    reporter = AssemblyReporter()
    report = reporter.generate_report(
        timeline_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output",
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons"
    )

    # Step 3: Save report
    print("Step 3: Saving report...")
    print()

    output_file = Path("/home/peter/homelab/projects/active/petersalvato.com/docs/SKELETON-ASSEMBLY-REPORT.md")
    with open(output_file, 'w') as f:
        f.write(report["summary_md"])

    print(f"✓ Report saved to {output_file}")
    print()

    # Step 4: Show validation results
    print("Step 4: Validation Results")
    print()

    passed = sum(1 for v in report["validations"] if v["passes"])
    failed = len(report["validations"]) - passed

    print(f"✓ Validations: {passed} passed, {failed} flagged for review")
    print()

    if failed > 0:
        print("Projects flagged for review:")
        for v in report["validations"]:
            if not v["passes"]:
                print(f"  ⚠️  {v['project']}")
                for issue in v['issues']:
                    print(f"      - {issue}")
        print()

    # Step 5: Summary
    print("SUMMARY")
    print("-" * 70)
    print(f"Total Projects: {report['total_projects']}")
    print(f"Total Timeline Entries: {report['total_entries']}")
    print(f"Skeletons Generated: {len(skeletons)}")
    print(f"Output Directory: docs/case-study-skeletons/")
    print(f"Report File: {output_file.name}")
    print()
    print("✅ SKELETON GENERATION COMPLETE")
    print()
    print("Next Steps:")
    print("  1. Review SKELETON-ASSEMBLY-REPORT.md")
    print("  2. Refine any flagged skeletons if needed")
    print("  3. Use skeletons as scaffolding for case study writing")
    print("  4. Apply Master Builder voice during narrative assembly")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
