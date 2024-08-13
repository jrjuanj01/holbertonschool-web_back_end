#!/usr/bin/env python3
"""file tha tcontains the function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a function that multiplies its input"""

    def multiplier_func(number: float) -> float:
        """Inner function that multiplies the input by multiplier"""

        return number * multiplier

    return multiplier_func
