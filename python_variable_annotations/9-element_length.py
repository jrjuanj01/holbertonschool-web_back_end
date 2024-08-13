#!/usr/bin/env python3
"""File that contains the function element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns some stuff"""
    return [(i, len(i)) for i in lst]
