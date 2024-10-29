#!/usr/bin/env python3
"""Pagination with HATEOAS
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Helper Function:
        Gets the index range
        Returns:
            A Tuple of start and end index
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the requested page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []
        return dataset[start_index:min(end_index, len(dataset))]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the requested pages with hypermedia
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        next_page = page + 1 if start_index < len(dataset) else None
        prev_page = page - 1 if page > 1 else None

        retval = {'page_size': page_size,
                  'page': page,
                  'data': self.get_page(page, page_size),
                  'next_page': next_page,
                  'prev_page': prev_page,
                  'total_pages': math.ceil(len(dataset) / page_size)
                  }
        return retval
