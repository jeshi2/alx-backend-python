#!/usr/bin/env python3
"""
This module provides a type-annotated function concat.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2


if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"
    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
