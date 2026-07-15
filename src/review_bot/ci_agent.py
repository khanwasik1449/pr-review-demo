class CIReviewAgent:
    """Reviews GitHub Actions workflows and CI/CD setup files."""

    def review(self, explore_summary: dict, changed_files: dict) -> str:
        has_ci_issue = False
        for filepath, diff in changed_files.items():
            if "actions: write" in diff:
                has_ci_issue = True
                break
                
        if has_ci_issue:
            return (
                "## CI/CD Review\n\n"
                "Severity: High\n"
                "Issue: Excessive GitHub Action permission 'actions: write' detected.\n"
                "Recommendation: Limit workflow permissions to the minimum necessary scopes (e.g. contents: read)."
            )
            
        return "No CI/CD issues detected."
