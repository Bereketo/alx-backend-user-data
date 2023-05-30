# 0x01. Basic authentication

# General
 * What authentication means
 * What Base64 is
 * How to encode a string in Base64
 * What Basic authentication means
 * How to send the Authorization header

# Tasks 
 * <font size=3> **0. Simple-basic-API** </font>
  * Setup and start server
 * <font sizse=3> **1. Error handler: Unauthorized** </font>
  * Edit api/v1/app.py:
  * Add a new error handler for this status code, the response must be:
   * a JSON: {"error": "Unauthorized"}
   * status code 401
   * you must use jsonify from Flask
  * For testing this new error handler, add a new endpoint in api/v1/views/index.py:
   * Route: GET /api/v1/unauthorized
   * This endpoint must raise a 401 error by using abort - Custom Error Pages
  * By calling abort(401), the error handler for 401 will be executed.
 * <font size=3> **2. Error handler: Forbidden** </font>
  * Edit api/v1/app.py:
  * Add a new error handler for this status code, the response must be:
   * a JSON: {"error": "Forbidden"}
   * status code 403
   * you must use jsonify from Flask
  * For testing this new error handler, add a new endpoint in api/v1/views/index.py:
   * Route: GET /api/v1/forbidden
   * This endpoint must raise a 403 error by using abort - Custom Error Pages
   * By calling abort(403), the error handler for 403 will be executed.
 * <font size=3> **3. Auth class** </font>
  * Create a folder api/v1/auth
  * Create an empty file api/v1/auth/__init__.py
  * Create the class Auth:
   * in the file api/v1/auth/auth.py
   * import request from flask
   * class name Auth
   * public method def require_auth(self, path: str, excluded_paths: List[str]) -> bool: that returns False - path and 
     excluded_paths will be used later, now, you don’t need to take care of them
   * public method def authorization_header(self, request=None) -> str: that returns None - request will be the Flask request object
   * public method def current_user(self, request=None) -> TypeVar('User'): that returns None - request will be the Flask request object

 * <font size=3> **4. Define which routes don't need authentication** </font>
  * Update the method def require_auth(self, path: str, excluded_paths: List[str]) -> bool: 
   in Auth that returns True if the path is not in the list of strings excluded_paths:
   * Returns True if path is None
   * Returns True if excluded_paths is None or empty
   * Returns False if path is in excluded_paths
   * You can assume excluded_paths contains string path always ending by a /
   * This method must be slash tolerant: path=/api/v1/status and path=/api/v1/status/ must be returned False if excluded_paths contains /api/v1/status/
 * <font size=3> **5. Request validation!** </font>
 Update the method def authorization_header(self, request=None) -> str: in api/v1/auth/auth.py:
  * If request is None, returns None
  * If request doesn’t contain the header key Authorization, returns None
  * Otherwise, return the value of the header request Authorization
 Update the file api/v1/app.py:
  * Create a variable auth initialized to None after the CORS definition
  * Based on the environment variable AUTH_TYPE, load and assign the right instance of authentication to auth
   * if auth:
    * import Auth from api.v1.auth.auth
    * create an instance of Auth and assign it to the variable auth
 Now the biggest piece is the filtering of each request. For that you will use the Flask method before_request
  * Add a method in api/v1/app.py to handler before_request
   * if auth is None, do nothing
   * if request.path is not part of this list ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'], 
     do nothing - you must use the method require_auth from the auth instance
   * if auth.authorization_header(request) returns None, raise the error 401 - you must use abort
   * if auth.current_user(request) returns None, raise the error 403 - you must use abort 

