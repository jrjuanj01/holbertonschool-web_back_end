#!/usr/bin/env python3
"""file tha tcontains the function make_multiplier"""
from typing import Callable

def make_multiplier(multiplier:float) -> Callable[[float], float]:
    """Function that returns a new function that multiplies its input by a given multiplier"""

    def multiplier_func(number: float) -> float:
        """Inner function that multiplies the input number by the given multiplier"""

        return number * multiplier

    return multiplier_func
