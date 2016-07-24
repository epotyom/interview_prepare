#!/usr/bin/python

class Node(object):
  def __init__(self, value, right=None, down=None):
    self.right = right
    self.down =down
    self.value = value
    
def flatten(head):
  return head.value + ('->{}'.format(flatten(head.down)) if head.down is not None else '') + ('->{0}'.format(flatten(head.right)) if head.right is not None else '')


def main():
  e = Node('E')
  l = Node('L')
  d = Node('D', right=e, down=l)
  y = Node('Y')
  t = Node('T', right=d, down=y)
  z = Node('Z')
  x = Node('X', down=z)
  n = Node('N', right=t, down=x)
  a = Node('A')
  c = Node('C', down=a)
  m = Node('M', right=n, down=c)
  print flatten(m)
  
if __name__ == '__main__':
  main()
