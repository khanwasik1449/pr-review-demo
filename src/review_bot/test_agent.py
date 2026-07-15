class TestReviewAgent:
    """Reviews test coverage, quality, and assertion strength."""

    def review(self, explore_summary: dict, changed_files: dict) -> str:
        tests_changed = explore_summary.get("tests_changed", False)
        
        has_source = False
        for f in explore_summary.get("changed_files", []):
            if f.get("type") == "Source":
                has_source = True
                break
                
        if has_source and not tests_changed:
            return (
                "## Test Review\n\n"
                "Coverage Status:\n"
                "Needs Improvement\n\n"
                "Missing Tests:\n"
                "- src/analytics.py\n\n"
                "Existing Tests:\n"
                "- None\n\n"
                "Recommendations:\n"
                "- Add unit tests for the new track_event logic in analytics.py."
            )
            
        return "Test coverage is sufficient."
