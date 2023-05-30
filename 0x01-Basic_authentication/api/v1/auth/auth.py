#!/usr/bin/env python3
"""auth.py
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ template class for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user
        """
        return None
