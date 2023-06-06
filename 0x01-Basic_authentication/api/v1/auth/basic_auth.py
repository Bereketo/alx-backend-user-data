#!/usr/bin/env python3
"""Basic auth
"""

from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
        except Exception as e:
            decoded_string = None
        return decoded_string

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password
            from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str) or \
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        email, password = decoded_base64_authorization_header.split(':')
        return (email, password)
