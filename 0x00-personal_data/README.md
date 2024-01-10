# Personal Data Filter and Encryption :smile:

This project provides a set of functionalities to handle personal data, including filtering sensitive information in log messages, creating secure loggers, connecting to a secure database, and encrypting passwords using bcrypt.

## Task 0: Regex-ing

The `filter_datum` function in `filtered_logger.py` uses regex to obfuscate sensitive information in log messages.

## Task 1: Log Formatter

The `RedactingFormatter` class in `filtered_logger.py` is an extension of the logging formatter that redacts specific fields from log records using the `filter_datum` function.

## Task 2: Create Logger

The `get_logger` function in `filtered_logger.py` creates a logging.Logger object named "user_data," configured to log up to the INFO level with a StreamHandler using the `RedactingFormatter` as the formatter.

## Task 3: Connect to Secure Database

The `get_db` function in `filtered_logger.py` connects to a MySQL database using credentials obtained from environment variables, following secure practices. It uses the `mysql-connector-python` library for the connection.

## Task 4: Read and Filter Data

The `main` function in `filtered_logger.py` retrieves all rows from the "users" table in the connected database and logs each row's filtered format using the configured logger.

## Task 5: Encrypting Passwords

The `hash_password` function in `encrypt_password.py` uses bcrypt to hash and salt passwords securely.

## Task 6: Check Valid Password

The `is_valid` function in `encrypt_password.py` checks if a provided password matches the hashed password using bcrypt.

## Usage

- Ensure you have the required dependencies installed: `pip install bcrypt mysql-connector-python`
- Execute `./filtered_logger.py` to run the main function, reading and logging data from the connected database.

## Contributors

- Nicholas Otieno Odhiambo
