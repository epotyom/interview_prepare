#!/usr/bin/env python

import unittest
import random
import copy

import bubblesort

class TestBubblesort(unittest.TestCase):
  def test_normal(self):
    data = [ random.randint(0,100) for _ in range(0,100) ] 
    sorted_data = copy.copy(data)
    sorted_data.sort()
    bubblesort.sort(data)
    self.assertEqual(data, sorted_data)

if __name__ == '__main__':
   unittest.main()
