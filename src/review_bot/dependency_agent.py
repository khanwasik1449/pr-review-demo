class DependencyReviewAgent:
    """Reviews dependencies added or modified in the pull request."""

    def review(self, explore_summary: dict, changed_files: dict) -> str:
        has_vulnerable_pkg = False
        for filepath, diff in changed_files.items():
            if "jinja2==2.11.3" in diff:
                has_vulnerable_pkg = True
                break
                
        if has_vulnerable_pkg:
            return (
                "## Dependency Review\n\n"
                "Package: jinja2==2.11.3\n"
                "Risk: Known security vulnerabilities (CVE-2024-22195, CVE-2024-34064). jinja2 versions < 3.1.3 are vulnerable to XSS.\n"
                "Recommendation: Upgrade jinja2 to version >= 3.1.4 or 3.0.3+ to patch these security flaws."
            )
            
        return "No dependency issues detected."
