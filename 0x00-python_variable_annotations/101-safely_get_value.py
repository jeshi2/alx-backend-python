#!/usr/bin/env python3
"""
This module provides a type-annotated function safely_get_value.
"""

from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Takes a dictionary, a key, and an optional default value.
    Returns the value associated with the key if it exists in the dictionary,
    otherwise returns the default value.

    Returns:
        Union[Any, T]: The value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    annotations = safely_get_value.__annotations__
    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print("{}: {}".format(k, v))
