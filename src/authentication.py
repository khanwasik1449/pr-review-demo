import hashlib
import uuid
from typing import Dict


class AuthenticationService:
    """A mock authentication service for demonstration purposes."""

    def __init__(self) -> None:
        # Maps username -> hashed_password
        self._user_db: Dict[str, str] = {}
        # Maps token -> username
        self._active_sessions: Dict[str, str] = {}

    def _hash_password(self, password: str) -> str:
        """Hash a password using SHA-256."""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def register_user(self, username: str, password: str) -> bool:
        """Register a new user. Returns False if user already exists."""
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")
        if username in self._user_db:
            return False
        self._user_db[username] = self._hash_password(password)
        return True

    def login(self, username: str, password: str) -> str:
        """Authenticate user and return a session token.
        
        Raises:
            ValueError: If credentials are invalid.
        """
        hashed = self._hash_password(password)
        if username not in self._user_db or self._user_db[username] != hashed:
            raise ValueError("Invalid username or password.")
        
        # Create a session token
        token = str(uuid.uuid4())
        self._active_sessions[token] = username
        return token

    def logout(self, token: str) -> bool:
        """Invalidate a session token. Returns True if successful."""
        if token in self._active_sessions:
            del self._active_sessions[token]
            return True
        return False

    def get_user_by_token(self, token: str) -> str:
        """Retrieve username for a session token.
        
        Raises:
            ValueError: If token is invalid.
        """
        if token not in self._active_sessions:
            raise ValueError("Invalid or expired session token.")
        return self._active_sessions[token]
