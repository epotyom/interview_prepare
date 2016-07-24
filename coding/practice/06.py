#!/usr/bin/env python
# 3 min
def reverse(words):
  wrds = words.split()
  wrds = [wrds[i] for i in range(len(wrds)-1,-1,-1)]
  print " ".join(wrds)

reverse("test ya ura")
