# scripts/prose_generator.py
from typing import Dict, List
import json

class ProseGenerator:
    def generate_prose(self, skeleton: Dict, voice_prompt: str, max_length: int = 2000) -> str:
        """Generate prose from skeleton using blended voice"""

        project = skeleton.get("project", "Unknown")
        constraint = skeleton.get("constraint", "")
        arc = skeleton.get("arc", [])

        # Build prompt for LLM
        prompt = self._build_prose_prompt(skeleton, voice_prompt)

        # Call LLM (placeholder - would be actual API call)
        prose = self._call_llm(prompt, max_length)

        # Validate skeleton fidelity
        validation = self.validate_fidelity(prose, skeleton)

        if validation.get("fidelity_score", 0) < 0.6:
            # If fidelity is low, regenerate with tighter constraints
            return self._regenerate_with_constraints(skeleton, voice_prompt, validation)

        return prose

    def _build_prose_prompt(self, skeleton: Dict, voice_prompt: str) -> str:
        """Build comprehensive prompt for prose generation"""

        arc_summary = self._summarize_arc(skeleton.get("arc", []))

        prompt = f"""{voice_prompt}

PROJECT: {skeleton.get('project', 'Unknown')}
CONSTRAINT: {skeleton.get('constraint', 'Not specified')}

NARRATIVE ARC (in chronological order):
{arc_summary}

INSTRUCTIONS:
1. Start with: "I [built/created/designed] [system] to [solve constraint]"
2. Walk through the arc moments in order, expanding each into prose
3. Use actual quotes from the snippets where they fit naturally
4. Show the thinking evolution: what problem emerged, how approach changed, what validates it works
5. Keep language direct, concrete, grounded in structural choices
6. Total length: 800-1200 words

Remember: Every claim must be grounded in the arc moments. Don't fabricate details.
"""

        return prompt

    def _summarize_arc(self, arc: List[Dict]) -> str:
        """Summarize arc moments for context"""
        summary = []
        for moment in arc[:10]:  # Use first 10 moments for context
            summary.append(f"- [{moment.get('type')}] {moment.get('snippet')}")

        return "\n".join(summary)

    def _call_llm(self, prompt: str, max_length: int) -> str:
        """Call LLM to generate prose (placeholder)"""
        # This would be actual API call to Claude API
        # For now, return structured response with more content
        return f"""I built a system to mark where my thinking changed. The problem emerged when I realized that tagging systems don't capture the shift in how I approach problems. The key insight was that a markup language preserves the moment of transformation. This allows me to capture semantic turning points where thinking shifts, creating a record of intellectual evolution. The savepoint protocol represents this thinking in a structured way that honors both the what and the why of my decision-making process. This approach proves effective because it grounds my work in the actual moments of cognitive change."""

    def validate_fidelity(self, prose: str, skeleton: Dict) -> Dict:
        """Validate that prose stays grounded in skeleton"""

        validation = {
            "fidelity_score": 0.0,
            "grounded": True,
            "issues": []
        }

        # Check if prose references key moments
        arc = skeleton.get("arc", [])
        constraint = skeleton.get("constraint", "")

        snippet_matches = 0
        for moment in arc[:5]:  # Check first 5 moments
            snippet = moment.get("snippet", "")
            if snippet.lower() in prose.lower():
                snippet_matches += 1
            else:
                # Check for partial matches with key words from snippet
                snippet_words = snippet.lower().split()
                if len(snippet_words) > 0:
                    key_word = snippet_words[0]
                    if key_word in prose.lower():
                        snippet_matches += 0.5

        # Calculate fidelity score
        fidelity_score = (snippet_matches / max(1, len(arc[:5]))) * 0.5  # Snippet match is 50%

        # Add points if constraint is mentioned
        if constraint.lower() in prose.lower():
            fidelity_score += 0.3
        else:
            # Check for partial constraint match
            constraint_words = constraint.lower().split()
            matched_constraint_words = sum(1 for word in constraint_words if word in prose.lower())
            if matched_constraint_words > 0:
                fidelity_score += 0.15

        # Add points if prose shows thinking evolution
        if any(word in prose.lower() for word in ["pivot", "realized", "problem", "failed", "shift", "mark", "thinking"]):
            fidelity_score += 0.2

        validation["fidelity_score"] = min(1.0, fidelity_score)

        return validation

    def _regenerate_with_constraints(self, skeleton: Dict, voice_prompt: str, validation: Dict) -> str:
        """Regenerate with tighter fidelity constraints"""

        # Build tighter prompt with specific issues
        tighter_prompt = f"""Previous attempt had fidelity issues: {validation.get('issues', [])}

Regenerate with these constraints:
1. Must reference specific moments from the arc (use exact snippets)
2. Must explain the constraint clearly
3. Must show thinking evolution through the moments
4. Keep it grounded - no speculation

{voice_prompt}
"""

        return self._call_llm(tighter_prompt, 2000)
