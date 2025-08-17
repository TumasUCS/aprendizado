import math
co = float(input('digite o cateto oposto '))
ca = float(input('digite o cateto adjacente '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('o valor da hipotenusa é {:.2f}'.format(h))