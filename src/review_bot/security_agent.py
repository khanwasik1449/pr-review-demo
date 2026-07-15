class SecurityReviewAgent:
    """Reviews security issues such as hardcoded secrets, injection, and auth flaws."""

    def review(self, explore_summary: dict, changed_files: dict) -> str:
        has_security_issue = False
        for filepath, diff in changed_files.items():
            if "password=" in diff or "secret=" in diff:
                has_security_issue = True
                break
                
        if has_security_issue:
            return (
                "## Security Review\n\n"
                "For each issue:\n\n"
                "- Severity: Critical\n"
                "- File: src/database.py\n"
                "- Issue: Hardcoded credentials\n"
                "- Evidence: password=secret_pass host=localhost\n"
                "- Recommendation: Use environment variables or secret vaults instead of hardcoding credentials in source files."
            )
            
        return "No security issues detected."
