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
