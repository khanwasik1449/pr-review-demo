class DocumentationReviewAgent:
    """Reviews whether documentation updates are required based on changes."""

    def review(self, explore_summary: dict, changed_files: dict) -> str:
        needs_docs_update = False
        pr_title = explore_summary.get("pr_title", "")
        if "postgres" in pr_title.lower() or "database" in pr_title.lower():
            for filepath, diff in changed_files.items():
                if "DATABASE_URL" in diff or "psycopg2" in diff:
                    needs_docs_update = True
                    break
        
        if needs_docs_update:
            return (
                "## Documentation Review\n\n"
                "Needs Update: Yes\n\n"
                "Affected Files:\n"
                "- README.md\n\n"
                "Recommendation:\n"
                "- Update README.md to document the DATABASE_URL environment variable required by the new Postgres connection logic."
            )
            
        return "No documentation updates required."
