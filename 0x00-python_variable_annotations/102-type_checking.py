#!/usr/bin/env python3
"""
This module provides a corrected type-annotated function zoom_array.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any], factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if __name__ == "__main__":
    array = [12, 72, 91]

    zoom_2x = zoom_array(tuple(array))
    zoom_3x = zoom_array(tuple(array), 3)
