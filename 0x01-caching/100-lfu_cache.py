#!/usr/bin/env python3
""" LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Algorithm
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.key_freq = {}
        self.freq = {}
        self.min_freq = 0

    def _update_frequency(self, key):
        freq = self.key_freq[key]

        # Remove the key from the old frequency list
        self.freq[freq].remove(key)
        if not self.freq[freq]:
            del self.freq[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        new_freq = freq + 1
        self.key_freq[key] = new_freq
        if new_freq not in self.freq:
            self.freq[new_freq] = []
        self.freq[new_freq].append(key)

    def put(self, key, item):
        """ Adds key-value pair to the cache
        """
        if key and item:
            if key in self.cache_data:
                # Update the value of exixting key
                self.cache_data[key] = item
                self._update_frequency(key)
            else:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    # Evict the least frequently used key
                    lfu_key = self.freq[self.min_freq].pop(0)
                    if not self.freq[self.min_freq]:
                        del self.freq[self.min_freq]
                    print(f"DISCARD: {lfu_key}")
                    del self.cache_data[lfu_key]
                    del self.key_freq[lfu_key]

                self.cache_data[key] = item
                self.key_freq[key] = 1
                if 1 not in self.freq:
                    self.freq[1] = []
                self.freq[1].append(key)
                self.min_freq = 1

    def get(self, key):
        """ Gets the value by key
        """
        if key not in self.cache_data:
            return None
        self._update_frequency(key)
        return self.cache_data[key]
