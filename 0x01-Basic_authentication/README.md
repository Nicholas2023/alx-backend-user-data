# Basic authentication :smile:

This repository contains the implementation of a simple API with basic authentication for user data storage. The project involves creating error handlers for unauthorized and forbidden requests, implementing an authentication class, and securing the API with basic authentication.

## Table of Contents

- [Error Handler: Unauthorized](#error-handler-unauthorized)
- [Error Handler: Forbidden](#error-handler-forbidden)
- [Auth Class](#auth-class)
- [Define Routes Excluded from Authentication](#define-routes-excluded-from-authentication)
- [Request Validation](#request-validation)
- [Basic Authentication](#basic-authentication)
- [Basic - Base64 Part](#basic-base64-part)
- [Basic - Base64 Decode](#basic-base64-decode)
- [Basic - User Credentials](#basic-user-credentials)
- [Basic - User Object](#basic-user-object)
- [Basic - Overload current_user](#basic-overload-current_user)
- [Allow Password with ":"](#allow-password-with-)
- [Require Auth with Stars](#require-auth-with-stars)

## Error Handler: Unauthorized

In this section, we implement an error handler for unauthorized requests with HTTP status code 401. The response includes a JSON message: `{"error": "Unauthorized"}`.

### Usage

```bash
curl "http://0.0.0.0:5000/api/v1/unauthorized"
```

## Error Handler: Forbidden

Similar to the unauthorized error handler, this section adds an error handler for forbidden requests with HTTP status code 403. The response includes a JSON message: `{"error": "Forbidden"}`.

### Usage

```bash
curl "http://0.0.0.0:5000/api/v1/forbidden"
```

## Auth Class

The Auth class is introduced to manage API authentication. It includes methods for checking if authentication is required (`require_auth`), extracting the authorization header (`authorization_header`), and retrieving the current user (`current_user`).

## Define Routes Excluded from Authentication

The `require_auth` method is updated to define routes that don't need authentication. It checks if the path is included in the list of excluded paths and returns `False` in such cases.

## Request Validation

All requests are now validated to secure the API. The `before_request` method is utilized to filter requests and ensure proper authentication. Unauthorized requests result in a 401 error, and forbidden requests lead to a 403 error.

## Basic Authentication

The BasicAuth class is introduced, inheriting from Auth, to handle basic authentication. It includes methods to extract the Base64 part of the Authorization header, decode the Base64 value, extract user credentials, and retrieve the User instance.

### Usage

```bash
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <base64_value>"
```

## Basic - Base64 Part

This section adds a method to the BasicAuth class to extract the Base64 part from the Authorization header.

## Basic - Base64 Decode

The BasicAuth class is enhanced with a method to decode the Base64 Authorization header.

## Basic - User Credentials

A method is added to the BasicAuth class to extract user credentials from the decoded Base64 Authorization header.

## Basic - User Object

A method is implemented in the BasicAuth class to retrieve the User instance based on email and password.

## Basic - Overload current_user

The `current_user` method is overloaded in the BasicAuth class to provide the User instance for a given request.

### Usage

```bash
curl "http://0.0.0.0:5000/api/v1/status" -H "Authorization: Basic <base64_value>"
```

## Allow Password with ":"

The `extract_user_credentials` method is improved in the BasicAuth class to allow passwords containing ":".

## Require Auth with Stars

The `require_auth` method is enhanced to support "*" at the end of excluded paths, providing flexibility in specifying excluded routes.

### Example

```python
excluded_paths = ["/api/v1/stat*"]
```
