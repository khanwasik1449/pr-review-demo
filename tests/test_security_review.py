import pytest
import json
import os

def test_security_review_agent_detection():
    # Arrange: Import SecurityReviewAgent from review_bot package
    try:
        from src.review_bot.security_agent import SecurityReviewAgent
    except ImportError:
        pytest.fail("TDD Check: SecurityReviewAgent class is not implemented yet in src.review_bot.security_agent")
        
    agent = SecurityReviewAgent()
    
    # Resolve fixture paths
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
    metadata_path = os.path.join(fixtures_dir, "sample_security_pr", "metadata.json")
    diff_path = os.path.join(fixtures_dir, "sample_security_pr", "diff.patch")
    
    with open(metadata_path, "r") as f:
        metadata = json.load(f)
        
    with open(diff_path, "r") as f:
        diff_content = f.read()
        
    # Act: Perform review on the security-vulnerable PR diff
    review_output = agent.review(explore_summary=metadata, changed_files={"src/database.py": diff_content})
    
    # Assert: Verify security findings and structure
    assert "Security Review" in review_output
    assert "database.py" in review_output
    assert "credentials" in review_output.lower() or "secret_pass" in review_output
    assert "Severity:" in review_output

def test_security_review_agent_clean():
    # Arrange
    try:
        from src.review_bot.security_agent import SecurityReviewAgent
    except ImportError:
        pytest.fail("TDD Check: SecurityReviewAgent class is not implemented yet")
        
    agent = SecurityReviewAgent()
    
    # Safe PostgreSQL configuration leveraging environment variable
    clean_diff = """diff --git a/src/database.py b/src/database.py
new file mode 100644
--- /dev/null
+++ b/src/database.py
@@ -0,0 +1,5 @@
+import os
+import psycopg2
+
+def get_connection():
+    return psycopg2.connect(os.getenv("DATABASE_URL"))
"""
    # Act
    review_output = agent.review(
        explore_summary={"pr_title": "Load DB url from environment", "changed_files": [{"file": "src/database.py", "type": "Source"}]},
        changed_files={"src/database.py": clean_diff}
    )
    
    # Assert
    assert "No security issues detected." in review_output
