import numpy as np 

L = [2, 5, 7, 1]
a = np.array(L)

def lab_1(j):
  s = 1
  for i in range (len(j)):
    s = s * j[i]
  print()