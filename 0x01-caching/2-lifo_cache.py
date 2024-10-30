#!/usr/bin/env python3
"""Lifo Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last in first out algorithm
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """Adds key-value pair to the cache
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    last_key = self.cache_data.popitem()[0]
                    print(f"DISCARD: {last_key}")
                self.cache_data[key] = item

    def get(self, key):
        """ Gets value by key
        """
        return self.cache_data.get(key)
