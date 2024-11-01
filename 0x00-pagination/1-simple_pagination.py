import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Retrieves the index range from a given page and page size."""
        return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a page of dataset."""
        assert isinstance(page, int) and page > 0, " must  positive ."
        assert isinstance(page_size, int) and page_size > 0, " must positive ."

        start, end = self.index_range(page, page_size)
        data = self.dataset()

        # Return the appropriate slice of the dataset or an empty
        # list if out of range
        if start >= len(data):
            return []
        return data[start:end]
