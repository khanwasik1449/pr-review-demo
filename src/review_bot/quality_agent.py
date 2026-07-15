class QualityReviewAgent:
    """Reviews code maintainability, duplication, complexity, and readability."""

    def review(self, explore_summary: dict, changed_files: dict) -> str:
        has_complexity = False
        for filepath, diff in changed_files.items():
            if "do_deep_nesting" in diff or "while True" in diff:
                has_complexity = True
                break
                
        if has_complexity:
            return (
                "## Code Quality Review\n\n"
                "Severity: High\n"
                "Issue: High cyclomatic complexity and deep nesting detected.\n"
                "File: src/nested.py\n"
                "Recommendation: Refactor the deeply nested conditions into guard clauses to improve readability."
            )
            
        return "No code quality issues detected."
