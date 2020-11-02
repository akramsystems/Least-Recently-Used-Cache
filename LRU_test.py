import unittest
from LRU import CacheLRU

# Run Test Command: $ python -m unittest LRU_test.py


class TestLRUCache(unittest.TestCase):

    def test_init(self):
        testCache = CacheLRU(10)
        self.assertIsInstance(testCache, CacheLRU)
        return

    def test_capcity(self):
        SIZE = 10
        testCache = CacheLRU(10)
        for i in range(SIZE+1):
            testCache.put(i, f"test{i}")
        self.assertEqual(SIZE, len(testCache.cache))
        return

    def test_put(self):
        testCache = CacheLRU(1)
        testCache.put(1, "test")
        self.assertEqual(testCache.cache.get(1), "test")
        return

    def test_get(self):
        testCache = CacheLRU(1)
        testCache.put(1, "test")
        self.assertEqual(testCache.get(1), "test")
        return

    def test_remove(self):
        testCache = CacheLRU(10)
        for i in range(10):
            testCache.put(i, f"test{i}")
        testCache.reset()
        cacheSize = len(testCache.cache)
        cacheCountSize = len(testCache.cacheCount)
        self.assertEqual(cacheCountSize, cacheSize)
        self.assertEqual(cacheSize, 0)

        return
