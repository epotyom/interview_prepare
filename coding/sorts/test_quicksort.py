#!/usr/bin/python

import unittest
import random
import copy

import quicksort

class TestQuicksort(unittest.TestCase):
  def test_random_data(self):
    data = [random.randint(0,100) for _ in range(10)]
    sorted_data = copy.copy(data)
    sorted_data.sort()
    quicksort.sort(data)
    self.assertEqual(data, sorted_data)


if __name__ == '__main__':
  unittest.main()
  
