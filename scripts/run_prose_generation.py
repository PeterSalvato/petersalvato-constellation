from case_study_prose_writer import CaseStudyProseWriter
from pathlib import Path

def main():
    print("=" * 70)
    print("CASE STUDY PROSE GENERATION")
    print("=" * 70)
    print()

    print("Step 1: Extracting personal voice from conversations...")
    print()

    writer = CaseStudyProseWriter(
        skeleton_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/case-study-skeletons",
        conversation_dir="/home/peter/homelab/projects/active/petersalvato.com/docs/extraction-output"
    )

    prose_docs = writer.write_all_prose()

    print(f"✓ Generated prose for {len(prose_docs)} projects")
    print()

    # Step 2: Validation summary
    print("Step 2: Validation Results")
    print()

    passed = sum(1 for doc in prose_docs if doc["validation"]["passes"])
    failed = len(prose_docs) - passed

    print(f"✓ {passed} passed validation")
    if failed > 0:
        print(f"⚠️  {failed} need review/revision")
    print()

    # Step 3: Report
    print("SUMMARY")
    print("-" * 70)
    print(f"Projects: {len(prose_docs)}")
    print(f"Prose documents generated: docs/case-study-prose/")
    print()
    print("✅ PROSE GENERATION COMPLETE")
    print()
    print("Next: Review prose files and refine as needed")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
