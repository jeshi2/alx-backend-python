#!/usr/bin/env python3
"""
This module provides a corrected type-annotated function zoom_array.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    zoomed_in: Tuple[int] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


if __name__ == "__main__":
    """Change to tuple"""
    array = (12, 72, 91)
    zoom_2x = zoom_array(array)
    """Change to int"""
    zoom_3x = zoom_array(array, 3)
    print(zoom_array.__annotations__)
