f = 1
f1 = 1

a = int(input('введите натуральное число: '))

print(f, f1, end = ' ')
while f1 < a:
  print(f1, end = ' ')
  f, f1 = f1, f + f1