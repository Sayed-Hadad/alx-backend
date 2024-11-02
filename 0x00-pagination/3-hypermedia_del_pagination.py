#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no dataset loaded."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file."""
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]  # Skip header
            except FileNotFoundError:
                raise Exception("Dataset file not found.")
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Retrieves a page of data with additional pagination information."""
        assert 0 <= index < len(self.__indexed_dataset), "."

        data = []
        current_index = index

        # Collect the requested number of items
        for _ in range(page_size):
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
            current_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": (
                current_index
                if current_index < len(self.__indexed_dataset)
                else None
            ),
        }
