#!/usr/bin/env python2.7

def sort(data):
  """
  selection sort
  
  find min element from the rest unsorted
  and put it as last sorted

  Arguments:
    data(list): List of numbers
  """
  for first_unsorted in range(0, len(data)):
    min_i = first_unsorted
    for i in range (first_unsorted, len(data)):
      if data[min_i] > data[i]:
        min_i = i
    tmp = data[min_i]
    data[min_i] = data[first_unsorted]
    data[first_unsorted] = tmp
    
    
    
