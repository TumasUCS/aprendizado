import math
n = float(input('digite um numero: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('o seno de {} equivale a {:.2f}'.format(n, s))
print('o coseno de {} equivale a {:.2f}'.format(n, c))
print('a tangente de {} equivale a {:.2f}'.format(n, t))
