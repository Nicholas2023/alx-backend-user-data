#!/usr/bin/env python3
"""
A module that filters personal information data
"""
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str) -> str:
    """
    Obfuscate specified fields in the log message
    Args:
        fields (list[str]) : List of str to obfuscate
        redaction (str) : The value to use in obfuscation
        message (str): String representing the log line
        separator (str) : Str representing character seperating fields
    Returns:
        str : Obfuscated log message
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, seperator), replace(redaction), message)
