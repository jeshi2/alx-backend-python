#!/usr/bin/env python3
"""
This module provides a type-annotated function add.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns the result.

    Returns:
        float: The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
