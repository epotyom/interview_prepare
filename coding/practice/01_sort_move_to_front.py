#!/usr/bin/env python

def sort(data):
  if len(data) > 1:
    for point in range(0,len(data)): 
      max = data[point]
      for i in range(point+1, len(data)):
        if max < data[i]:
          max = data[i]
      moveToBeginning(data, max)

def moveToBeginning(data, elem):
  for i,v in enumerate(data):
    if v == elem:
      break
  print "data={}".format(data)
  data.pop(i)
  data.insert(0, v)
  print "data2={}".format(data)

def main():
  a=[1,5,3,6,87,2,9]
  print a
  sort(a)
  print(a)

if __name__ == '__main__':
  main()

