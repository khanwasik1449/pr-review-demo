import pytest

def test_test_review_agent_missing_tests():
    # Arrange: Import TestReviewAgent from review_bot package
    try:
        from src.review_bot.test_agent import TestReviewAgent
    except ImportError:
        pytest.fail("TDD Check: TestReviewAgent class is not implemented yet in src.review_bot.test_agent")
        
    agent = TestReviewAgent()
    
    # Context: A new source file is introduced, but tests_changed is false
    explore_summary = {
        "pr_title": "Add analytics engine",
        "changed_files": [
            {"file": "src/analytics.py", "type": "Source"}
        ],
        "tests_changed": False
    }
    source_diff = """diff --git a/src/analytics.py b/src/analytics.py
new file mode 100644
--- /dev/null
+++ b/src/analytics.py
@@ -0,0 +1,5 @@
+def track_event(name):
+    print(f"Tracking event: {name}")
"""
    # Act: Perform review
    review_output = agent.review(explore_summary=explore_summary, changed_files={"src/analytics.py": source_diff})
    
    # Assert: Output indicates coverage needs improvement and specifies missing tests
    assert "Test Review" in review_output
    assert "Needs Improvement" in review_output
    assert "analytics.py" in review_output or "Missing Tests" in review_output

def test_test_review_agent_sufficient_tests():
    # Arrange
    try:
        from src.review_bot.test_agent import TestReviewAgent
    except ImportError:
        pytest.fail("TDD Check: TestReviewAgent class is not implemented yet")
        
    agent = TestReviewAgent()
    
    # Context: Source changes are paired with test additions
    explore_summary = {
        "pr_title": "Add analytics engine",
        "changed_files": [
            {"file": "src/analytics.py", "type": "Source"},
            {"file": "tests/test_analytics.py", "type": "Test"}
        ],
        "tests_changed": True
    }
    changed_files = {
        "src/analytics.py": "def track_event(name):\n    pass",
        "tests/test_analytics.py": "def test_track_event():\n    assert True"
    }
    # Act
    review_output = agent.review(explore_summary=explore_summary, changed_files=changed_files)
    
    # Assert
    assert "Test coverage is sufficient." in review_output
