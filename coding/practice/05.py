#!/usr/bin/env python
# 30 min

def build_tree(rest_code):
  result = {}
  if len(rest_code) > 1:
    if 0<int(rest_code[:2])< 27:
      result[rest_code[:2]] = build_tree(rest_code[2:])
  if len(rest_code) > 0:
    if 0<int(rest_code[0]):
      result[rest_code[0]] = build_tree(rest_code[1:])
  else:
    result = None
  return result
    
def print_tree(tree, strbase=''):
  for k,v in tree.items(): 
    if v is None:
      print "{}{}\n".format(strbase,map_char(k))
    else:
      print_tree(v,strbase+map_char(k))

def map_char(char_num):
  base = ord('a')
  mapc = {i:chr(i) for i in range(ord('a'),ord('z'))}
  return mapc[int(char_num) + base - 1]


a = '123'
print a
t = build_tree(a)
print_tree(t)
