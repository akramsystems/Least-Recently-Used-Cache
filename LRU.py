from math import inf


class CacheLRU(object):
    """
    Title:
    Creates Least Recently Used Cache Item

    Example:
        # Create cache with 10 item capacity
        cache = CacheLRU(2) 
        cache.put(1,"first")
        cache.put(2,"second")
        cache.put(3,"third")
        cache.get(3) # third

    Variables:
        capactiy<int>: Maximum num of objects
        storage<object:usageCount>: Mapping of objects to usage count

    Methods:
        put: insert a value for an associated key
        get: retrieve a value for an associated key
        reset:  clear all items in cache
        _removeLRU: remove least used cache item
        _getCache: retrieve cache items
        _getCacheCount: retrieve cache counts
        __repr__: string representation of CacheLRU
    """

    def __init__(self, capacity):

        assert type(capacity) is int
        assert capacity > 0
        self.capacity = capacity
        self.cache = {}
        self.cacheCount = {}

    # Insert new value for the key
    def put(self, key, value):
        if self.cacheCount.get(key):
            self.cacheCount[key] += 1
            self.cache[key] = value
            return

        if self.capacity == len(self.cacheCount.values()):
            # Remove Least Recently Used Item
            self._removeLRU()

        self.cache[key] = value
        self.cacheCount[key] = 1
        return

    # Get the value for an associated key
    def get(self, key):
        if self.cache.get(key) == None:
            return False
        else:
            self.cacheCount[key] += 1
            return self.cache.get(key)

    # reset our LRU cache
    def reset(self):
        self.cache = {}
        self.cacheCount = {}
        return

    # delete a specific key
    def delete(self, key):
        if self.get(key):
            self.cache.pop(key)
            self.cacheCount.pop(key)
            return True
        else:
            pass

    def _removeLRU(self):
        min_cnt = inf
        min_key = None
        for key, cnt in self.cacheCount.items():
            if cnt < min_cnt:
                min_cnt = cnt
                min_key = key

        self.cache.pop(min_key)
        self.cacheCount.pop(min_key)

        return

    def _getCacheCount(self):
        return self.cacheCount.items()

    def _getCache(self):
        return self.cache.items()

    def __repr__(self):
        return str(self._getCache())
