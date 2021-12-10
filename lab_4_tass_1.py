
def lab_1(j):
  s = 0
  for i in range (len(j)):
    s = s + j[i]
  r = s / len(j)
  print(r)

L = [4, 7, 9, 9] 
lab_1(L)