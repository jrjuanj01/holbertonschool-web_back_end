#!/usr/bin/env python3
"""File that contains the function index range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """function that returns the the index and size of a page"""

    return (((page * page_size) - page_size), (page * page_size))
