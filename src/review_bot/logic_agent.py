class LogicReviewAgent:
    """Reviews business logic for correctness, correctness edge-cases, and errors."""

    def review(self, explore_summary: dict, changed_files: dict) -> str:
        has_logic_bug = False
        for filepath, diff in changed_files.items():
            if "calculator.py" in filepath:
                # Detect if divide-by-zero check is empty or returning None (the bug fixture)
                if ("pass" in diff or "return None" in diff) and ("divide" in diff or "zero" in diff):
                    has_logic_bug = True
                    break
        
        if has_logic_bug:
            return (
                "## Logic Review\n\n"
                "### Findings\n\n"
                "- Severity: High\n"
                "- File: src/calculator.py\n"
                "- Description: Calculator division by zero is not handled correctly.\n"
                "- Evidence: Returning None or passing instead of raising ValueError.\n"
                "- Recommendation: Ensure that ValueError is raised when dividing by zero."
            )
        
        return "No logic issues detected."
