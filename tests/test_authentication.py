import pytest
from src.authentication import AuthenticationService


def test_register_and_login():
    auth = AuthenticationService()
    assert auth.register_user("testuser", "password123") is True
    # Can't register same user twice
    assert auth.register_user("testuser", "password456") is False

    token = auth.login("testuser", "password123")
    assert token is not None
    assert auth.get_user_by_token(token) == "testuser"


def test_invalid_login():
    auth = AuthenticationService()
    auth.register_user("testuser", "password123")
    
    with pytest.raises(ValueError) as excinfo:
        auth.login("testuser", "wrongpassword")
    assert "Invalid username or password" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        auth.login("nonexistent", "password")
    assert "Invalid username or password" in str(excinfo.value)


def test_logout():
    auth = AuthenticationService()
    auth.register_user("testuser", "password123")
    token = auth.login("testuser", "password123")
    
    assert auth.logout(token) is True
    # Token should no longer be active
    with pytest.raises(ValueError):
        auth.get_user_by_token(token)
    
    # Repeated logout should return False
    assert auth.logout(token) is False
