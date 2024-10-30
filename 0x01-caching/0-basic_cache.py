#!/usr/bin/env python3
""" BasicCache assigns and retreives from the storage
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Assigns and retrieves from storage
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets value by key
        """
        return self.cache_data.get(key)
