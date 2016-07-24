#!/usr/bin/env python

def sort(data):
  """
  sort list using divide and conquer algorythm
  
  Arguments:
    data (list) - list of numbers
  """
  if len(data) < 2:
    return data
  
  a = sort(data[:len(data)//2])
  b = sort(data[len(data)//2:len(data)])
  result = []
  while len(a) and len(b):
    if a[0] < b[0]:
      result.append(a.pop(0))
    else:
      result.append(b.pop(0))

  result.extend(a + b)
  return result
  
