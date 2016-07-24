#!/usr/bin/env python
def main():
  print test_arr([1,2,4,5,3], 8)

def test_arr(data, target):
  for first in range (0,len(data)):
    for last in range(first,len(data)+1):
      summ = sum(data[first:last])
      if summ == target:
        return True
      elif summ > target:
        break
  return False


if __name__ == '__main__':
  main()
