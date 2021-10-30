a = float(input('введите число: '))

b = float(input('а теперь второе: '))

c = a / b
d = a % b

if b != 0 and a / b > 0 :
  print(c)
  print(d)
else:
  print( 'не получается')