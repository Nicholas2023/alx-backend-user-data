#!/usr/bin/env python3
"""
A module that implements password encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Obfuscates a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if an obfusced password was formed from given pwd
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
