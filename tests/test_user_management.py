import pytest
from src.user_management import UserManager, UserProfile


def test_create_and_get_profile():
    manager = UserManager()
    profile = manager.create_profile("alice", "alice@example.com", "Alice Smith")
    
    assert profile.username == "alice"
    assert profile.email == "alice@example.com"
    assert profile.display_name == "Alice Smith"
    
    retrieved = manager.get_profile("alice")
    assert retrieved is not None
    assert retrieved.email == "alice@example.com"
    
    # Try to create duplicate
    with pytest.raises(ValueError) as excinfo:
        manager.create_profile("alice", "alice2@example.com", "Alice 2")
    assert "already exists" in str(excinfo.value)


def test_update_profile():
    manager = UserManager()
    manager.create_profile("bob", "bob@example.com", "Bob Jones")
    
    # Update email and display name
    updated = manager.update_profile("bob", email="bob.new@example.com", display_name="Robert Jones")
    assert updated.email == "bob.new@example.com"
    assert updated.display_name == "Robert Jones"
    
    # Update only one field
    updated = manager.update_profile("bob", display_name="Bob J.")
    assert updated.email == "bob.new@example.com"
    assert updated.display_name == "Bob J."


def test_delete_profile():
    manager = UserManager()
    manager.create_profile("charlie", "charlie@example.com", "Charlie Brown")
    
    assert manager.delete_profile("charlie") is True
    assert manager.get_profile("charlie") is None
    assert manager.delete_profile("charlie") is False
