from typing import Dict, Any, Optional


class UserProfile:
    def __init__(self, username: str, email: str, display_name: str) -> None:
        self.username = username
        self.email = email
        self.display_name = display_name


class UserManager:
    """Manages user profiles and metadata."""

    def __init__(self) -> None:
        self._profiles: Dict[str, UserProfile] = {}

    def create_profile(self, username: str, email: str, display_name: str) -> UserProfile:
        """Create and store a user profile.
        
        Raises:
            ValueError: If profile already exists or invalid input.
        """
        if not username or not email or not display_name:
            raise ValueError("All profile fields are required.")
        if username in self._profiles:
            raise ValueError(f"Profile for user '{username}' already exists.")
        
        profile = UserProfile(username, email, display_name)
        self._profiles[username] = profile
        return profile

    def get_profile(self, username: str) -> Optional[UserProfile]:
        """Retrieve a user profile. Returns None if not found."""
        return self._profiles.get(username)

    def update_profile(self, username: str, email: Optional[str] = None, display_name: Optional[str] = None) -> UserProfile:
        """Update fields of an existing user profile.
        
        Raises:
            ValueError: If profile does not exist.
        """
        if username not in self._profiles:
            raise ValueError(f"Profile for user '{username}' does not exist.")
        
        profile = self._profiles[username]
        if email is not None:
            if not email:
                raise ValueError("Email cannot be empty.")
            profile.email = email
        if display_name is not None:
            if not display_name:
                raise ValueError("Display name cannot be empty.")
            profile.display_name = display_name
        return profile

    def delete_profile(self, username: str) -> bool:
        """Delete a user profile. Returns True if deleted."""
        if username in self._profiles:
            del self._profiles[username]
            return True
        return False
