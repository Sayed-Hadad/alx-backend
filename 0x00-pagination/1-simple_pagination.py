#!/usr/bin/env python3

import csv
from typing import List, Tuple


class Server:
    """Class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server with no dataset loaded."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]  # Skip header
        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return the start and end index for a page."""
        return ((page - 1) * page_size, (page - 1) * page_size + page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the rows for a specific page."""
        assert isinstance(page, int) and page > 0, "positive integer."
        assert isinstance(page_size, int) and page_size > 0, "+ integer."

        start, end = self.index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []  # Out of range
        return data[start:end]
