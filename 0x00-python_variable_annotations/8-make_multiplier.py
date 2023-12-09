#!/usr/bin/env python3
"""
This module provides a type-annotated function make_multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a function
    that multiplies a float by multiplier.

    Returns:
        Callable[[float], float]: A function that multiplies
        a float by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function


if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
