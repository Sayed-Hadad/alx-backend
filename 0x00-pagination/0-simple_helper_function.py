#!/usr/bin/env python3
"""
This module provides a utility function to calculate the range of indexes
for paginated results.
"""

def index_range(page, page_size):
    """
    Calculate the start and end index for paginated results.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)
