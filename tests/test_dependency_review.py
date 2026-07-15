import pytest

def test_dependency_review_agent_vulnerability():
    # Arrange: Import DependencyReviewAgent from review_bot package
    try:
        from src.review_bot.dependency_agent import DependencyReviewAgent
    except ImportError:
        pytest.fail("TDD Check: DependencyReviewAgent class is not implemented yet in src.review_bot.dependency_agent")
        
    agent = DependencyReviewAgent()
    
    explore_summary = {
        "pr_title": "Add vulnerable dependency",
        "changed_files": [
            {"file": "requirements.txt", "type": "Dependency"}
        ]
    }
    # Add an old package version with known vulnerabilities (e.g. jinja2 2.11.3)
    vuln_diff = """diff --git a/requirements.txt b/requirements.txt
--- a/requirements.txt
+++ b/requirements.txt
@@ -1,2 +1,3 @@
 pytest>=8.0.0
+jinja2==2.11.3
"""
    # Act: Perform review
    review_output = agent.review(explore_summary=explore_summary, changed_files={"requirements.txt": vuln_diff})
    
    # Assert: Output flags the version risk / vulnerability
    assert "Dependency Review" in review_output
    assert "jinja2" in review_output.lower()
    assert "Risk" in review_output

def test_dependency_review_agent_clean():
    # Arrange
    try:
        from src.review_bot.dependency_agent import DependencyReviewAgent
    except ImportError:
        pytest.fail("TDD Check: DependencyReviewAgent class is not implemented yet")
        
    agent = DependencyReviewAgent()
    
    # Safe modern version update
    clean_diff = """diff --git a/requirements.txt b/requirements.txt
--- a/requirements.txt
+++ b/requirements.txt
@@ -1,2 +1,3 @@
 pytest>=8.0.0
+jinja2>=3.1.4
"""
    # Act
    review_output = agent.review(
        explore_summary={"pr_title": "Add jinja2 dependency", "changed_files": [{"file": "requirements.txt", "type": "Dependency"}]},
        changed_files={"requirements.txt": clean_diff}
    )
    
    # Assert
    assert "No dependency issues detected." in review_output
