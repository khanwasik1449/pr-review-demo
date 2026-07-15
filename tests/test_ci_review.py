import pytest

def test_ci_review_agent_insecure_permissions():
    # Arrange: Import CIReviewAgent from review_bot package
    try:
        from src.review_bot.ci_agent import CIReviewAgent
    except ImportError:
        pytest.fail("TDD Check: CIReviewAgent class is not implemented yet in src.review_bot.ci_agent")
        
    agent = CIReviewAgent()
    
    explore_summary = {
        "pr_title": "Modify workflow permissions",
        "changed_files": [
            {"file": ".github/workflows/ci.yml", "type": "Workflow"}
        ]
    }
    # Insecure permission setup (e.g., adding actions write permission when unnecessary)
    insecure_diff = """diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
--- a/.github/workflows/ci.yml
+++ b/.github/workflows/ci.yml
@@ -9,2 +9,3 @@ permissions:
   contents: read
+  actions: write
"""
    # Act: Perform review
    review_output = agent.review(explore_summary=explore_summary, changed_files={".github/workflows/ci.yml": insecure_diff})
    
    # Assert: Output indicates CI/CD review concerns with permissions
    assert "CI/CD Review" in review_output
    assert "Severity:" in review_output
    assert "permission" in review_output.lower() or "actions: write" in review_output

def test_ci_review_agent_clean():
    # Arrange
    try:
        from src.review_bot.ci_agent import CIReviewAgent
    except ImportError:
        pytest.fail("TDD Check: CIReviewAgent class is not implemented yet")
        
    agent = CIReviewAgent()
    
    # Optimization modification adding pip caching (secure and correct)
    clean_diff = """diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
--- a/.github/workflows/ci.yml
+++ b/.github/workflows/ci.yml
@@ -21,2 +21,3 @@ jobs:
       uses: actions/setup-python@v5
+      with:
+        cache: 'pip'
"""
    # Act
    review_output = agent.review(
        explore_summary={"pr_title": "Cache pip in workflow", "changed_files": [{"file": ".github/workflows/ci.yml", "type": "Workflow"}]},
        changed_files={".github/workflows/ci.yml": clean_diff}
    )
    
    # Assert
    assert "No CI/CD issues detected." in review_output
