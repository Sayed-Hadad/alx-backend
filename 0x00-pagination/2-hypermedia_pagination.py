#!/usr/bin/env python3
"""Task 1: Simple pagination."""

import csv
from typing import List, Tuple, Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size."""
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no dataset loaded."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data."""
        assert isinstance(page, int) and page > 0, "Positive ."
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer."
        )

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves a page of data with additional pagination information."""
        assert isinstance(page, int) and page > 0, "integer."
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer."
        )

        data = self.get_page(page, page_size)  # Reuse get_page
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
