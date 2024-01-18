# Session Authentication :smile:

This project extends the previous work on Basic Authentication by introducing Session Authentication. Session Authentication allows users to log in using a session ID stored in a cookie, providing a more user-friendly authentication mechanism often used in web applications.

## Project Structure

The project is organized into the following components:

- `api/v1/app.py`: Main application file where Flask app is created and configured.
- `api/v1/auth/`: Directory containing authentication-related files.
  - `basic_auth.py`: Basic authentication implementation.
  - `session_auth.py`: Session authentication implementation.
  - `auth.py`: Base authentication class with common methods.
- `api/v1/models/`: Directory containing the User model.
- `api/v1/views/`: Directory containing view files.
  - `users.py`: Handles User endpoints.
  - `session_auth.py`: Implements routes for Session Authentication.

## Setup

Before running the application, make sure to set the required environment variables:

- `API_HOST`: Host address for the API (default: 0.0.0.0).
- `API_PORT`: Port number for the API (default: 5000).
- `AUTH_TYPE`: Authentication type (either `basic_auth` or `session_auth`).
- `SESSION_NAME`: Name of the cookie used for Session ID.

## Usage

1. **Basic Authentication Endpoints:**
   - `GET /api/v1/users`: Retrieve all users (requires authentication).
   - `POST /api/v1/users`: Create a new user (requires authentication).
   - `GET /api/v1/users/<user_id>`: Retrieve user details by ID (requires authentication).
   - `PUT /api/v1/users/<user_id>`: Update user details by ID (requires authentication).
   - `DELETE /api/v1/users/<user_id>`: Delete user by ID (requires authentication).

2. **Session Authentication Endpoints:**
   - `POST /api/v1/auth_session/login`: Log in and create a session (requires email and password).
   - `DELETE /api/v1/auth_session/logout`: Log out and destroy the session.

3. **Additional Endpoint:**
   - `GET /users/me`: Retrieve details of the authenticated user (requires session authentication).

## Examples

### Basic Authentication:

```bash
# Create a user and obtain basic authentication token
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py

# Access protected endpoints using basic authentication
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <base64_token>"
```

### Session Authentication:

```bash
# Run the application with session authentication
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app

# Log in and create a session
curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=user@example.com" -d "password=password"

# Access protected endpoint using the obtained session ID
curl "http://0.0.0.0:5000/users/me" --cookie "_my_session_id=<session_id>"
```

### Logout:

```bash
# Log out and destroy the session
curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=<session_id>"
```

## Notes

- Make sure to install the required dependencies specified in the `requirements.txt` file before running the application.
- For security reasons, it's recommended to run the application over HTTPS in a production environment.

Feel free to explore the provided scripts and customize the authentication mechanism based on your application's needs.
