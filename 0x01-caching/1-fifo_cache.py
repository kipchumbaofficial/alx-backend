#!/usr/bin/env python3
""" FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Implements fifo caching
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Adds key value Pair to  the cache
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    # Remove the first added key
                    first_key = list(self.cache_data.keys())[0]

                    print(f"DISCARD: {first_key}")

                    self.cache_data.pop(first_key)

                self.cache_data[key] = item

    def get(self, key):
        """ Gets Value by key
        """
        return self.cache_data.get(key)
