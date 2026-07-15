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

    def _validate_non_empty(self, value: Optional[str], error_message: str) -> str:
        """Validate that a string value is not empty or None."""
        if not value:
            raise ValueError(error_message)
        return value

    def create_profile(self, username: str, email: str, display_name: str) -> UserProfile:
        """Create and store a user profile.
        
        Raises:
            ValueError: If profile already exists or invalid input.
        """
        self._validate_non_empty(username, "All profile fields are required.")
        self._validate_non_empty(email, "All profile fields are required.")
        self._validate_non_empty(display_name, "All profile fields are required.")
        
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
            profile.email = self._validate_non_empty(email, "Email cannot be empty.")
        if display_name is not None:
            profile.display_name = self._validate_non_empty(display_name, "Display name cannot be empty.")
        return profile

    def delete_profile(self, username: str) -> bool:
        """Delete a user profile. Returns True if deleted."""
        if username in self._profiles:
            del self._profiles[username]
            return True
        return False
