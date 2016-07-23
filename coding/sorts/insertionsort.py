#!/usr/bin/env python2.7

def sort(data):
  if len(data) > 1:
    for last_sorted in range (0, len(data) - 1):
      if data[last_sorted+1] < data[last_sorted]:
        first_unsort = data[last_sorted+1]
        for i in range(0,last_sorted+1):
          if first_unsort < data[i]:
            for j in range(last_sorted, i-1, -1):
              data[j+1]= data[j]
            data[i] = first_unsort   
            break
