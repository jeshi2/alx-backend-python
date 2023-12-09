#!/usr/bin/env python3
"""
This module provides a duck-typed function safe_first_element.
"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence and returns its first element if it exists,
    otherwise returns None.

    Returns:
        Union[Any, None]: The first element of the input sequence
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element.__annotations__)
