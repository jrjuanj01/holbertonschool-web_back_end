#!/usr/bin/env python3
"""File that contains the function sum_mixed_list """
from typing import List, Union

def sum_mixed_list(lst: List[Union[int, float]]) -> float:
    """Function that returns the sum of all elements in a list"""

    return sum(lst)
