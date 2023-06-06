#!/usr/bin/env python3
"""Basic auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class for Basic Authentication
    """
    def extract_base64_authorization_header(
              self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None
        header = authorization_header.split(' ')

        if header[0] != 'Basic':
            return None
        return header[1]
