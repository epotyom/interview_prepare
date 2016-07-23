#!/usr/bin/env python2.7

import random

def main():
  data = [ random.randint(0,100) for i in range(0,100)]
  print "Unsorted: {0}".format(data)
  insertionSort(data)
  #bubbleSort(data)
  print "Sorted: {0}".format(data)

def sort(data):
  if len(data) > 1:
    no_swaps = False
    while not no_swaps:
      no_swaps = True
      for i in range(0,len(data)-1):
        if data[i] > data [i+1]:
          tmp = data[i]
          data[i] = data[i+1]
          data[i+1] = tmp
          no_swaps = False    

if __name__ == '__main__':
  main()
