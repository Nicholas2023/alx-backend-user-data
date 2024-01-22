# User Authentication Service :smile:

This project implements a user authentication service using Flask and SQLAlchemy. The service includes functionalities such as user registration, login, logout, password reset, and user profile retrieval.

## Table of Contents

- [Task Overview](#task-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Integration Tests](#integration-tests)

## Task Overview

The project is divided into several tasks, each addressing specific functionalities and components of the user authentication service. The tasks cover the creation of a user model, database interactions, password hashing, session management, and API endpoints for user registration, login, profile retrieval, and more.

## Getting Started

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/alx-backend-user-data.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-backend-user-data/0x03-user_authentication_service
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

The application should now be running at [http://localhost:5000](http://localhost:5000).

## Usage

### Database Initialization

The application uses SQLite as the database. The database is initialized when creating an instance of the `DB` class in the `db.py` file.

### API Endpoints

The API provides the following endpoints:

- **POST /users**: Register a new user.
- **POST /sessions**: Log in and create a new session.
- **DELETE /sessions**: Log out and destroy the session.
- **POST /reset_password**: Request a reset password token.
- **PUT /reset_password**: Update the password using the reset token.
- **GET /profile**: Retrieve user profile information.

### Integration Tests

To run end-to-end integration tests, use the provided `main.py` script:

```bash
python main.py
```
