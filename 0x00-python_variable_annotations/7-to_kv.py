#!/usr/bin/env python3
"""
This module provides a type-annotated function to_kv.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v and returns a tuple.

    Returns:
        Tuple[str, float]: A tuple with the string key and
        the square of the int/float value.
    """
    return (k, v ** 2)


if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
