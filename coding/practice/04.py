#!/usr/bin/env python
from pprint import pprint


def handle(data):
  for i in range (0,len(data)):
    for j in range (0,len(data)):
      print "data={}".format(data)
      print "cur={},{}".format(i,j)
      if data[i][j] in ['O','D']:
        go(data,i,j)
def go(data,x,y):
  data[x][y] = 'T'
  print '---'
  print (x,y)
  print data
  neighbors = []
  for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if 0 <= i < len(data) and 0<=j<len(data[i]):
      if data[i][j] == 'G':
        neighbors.append(-1)
      elif isinstance(data[i][j], int):
        neighbors.append(data[i][j])
      elif data[i][j] == 'O':
        d = go(data,i,j)
        if d is not None:
          neighbors.append(d)
            
  print neighbors
  if len(neighbors):
    data[x][y] = min(neighbors) + 1
    return data[x][y]
  else:
    data[x][y] = 'D'
    return None

a = [
  ['O', 'G', 'W' , 'O'],
  ['O', 'O', 'O', 'O'],
  ['O', 'W', 'W', 'O'],
  ['O', 'G', 'W', 'O'],
]
handle(a)
for v in a:
  print "\n"
  print ' '.join([str(i) for i in v])
