import pytest

def test_docs_review_agent_needs_update():
    # Arrange: Import DocumentationReviewAgent from review_bot package
    try:
        from src.review_bot.docs_agent import DocumentationReviewAgent
    except ImportError:
        pytest.fail("TDD Check: DocumentationReviewAgent class is not implemented yet in src.review_bot.docs_agent")
        
    agent = DocumentationReviewAgent()
    
    # Context: A new backend db integration introducing DATABASE_URL environment config
    explore_summary = {
        "pr_title": "Introduce Postgres Database integration",
        "changed_files": [
            {"file": "src/database.py", "type": "Source"}
        ]
    }
    source_diff = """diff --git a/src/database.py b/src/database.py
new file mode 100644
--- /dev/null
+++ b/src/database.py
@@ -0,0 +1,5 @@
+import os
+import psycopg2
+def get_connection():
+    return psycopg2.connect(os.getenv("DATABASE_URL"))
"""
    # Act: Perform review
    review_output = agent.review(explore_summary=explore_summary, changed_files={"src/database.py": source_diff})
    
    # Assert: Output indicates documentation needs update
    assert "Documentation Review" in review_output
    assert "Needs Update: Yes" in review_output
    assert "DATABASE_URL" in review_output or "README" in review_output

def test_docs_review_agent_no_update_required():
    # Arrange
    try:
        from src.review_bot.docs_agent import DocumentationReviewAgent
    except ImportError:
        pytest.fail("TDD Check: DocumentationReviewAgent class is not implemented yet")
        
    agent = DocumentationReviewAgent()
    
    # Context: Renaming internal details of a method that is not exposed outside the module
    explore_summary = {
        "pr_title": "Rename internal variable in authentication",
        "changed_files": [
            {"file": "src/authentication.py", "type": "Source"}
        ]
    }
    source_diff = """diff --git a/src/authentication.py b/src/authentication.py
--- a/src/authentication.py
+++ b/src/authentication.py
@@ -10,3 +10,3 @@ class AuthenticationService:
-        self._user_db: Dict[str, str] = {}
+        self._users: Dict[str, str] = {}
"""
    # Act
    review_output = agent.review(explore_summary=explore_summary, changed_files={"src/authentication.py": source_diff})
    
    # Assert
    assert "No documentation updates required." in review_output
