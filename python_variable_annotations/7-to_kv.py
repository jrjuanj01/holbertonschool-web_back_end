#!/usr/bin/env python3
"""File that contains the function to_kv"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """Function to convert a key-value pair to a tuple"""

    return (k, v^(2))
