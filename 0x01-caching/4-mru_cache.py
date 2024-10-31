#!/usr/bin/env python3
""" MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently used algorithm
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """ Adds key value pair to the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item

                self.access_order.remove(key)
                self.access_order.append(key)
            else:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    mru_key = self.access_order.pop()
                    print(f"DISCARD: {mru_key}")
                    del self.cache_data[mru_key]
                self.cache_data[key] = item
                self.access_order.append(key)

    def get(self, key):
        """ Gets Value by key
        """
        if key not in self.cache_data:
            return None
        else:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
