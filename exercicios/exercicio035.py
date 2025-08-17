import math
r1 = float(input('digite o tamanho de uma reta: '))
r2 = float(input('digite o tamanho de outra reta: '))
r3 = float(input('digite o tamanho de mais uma reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'é possivel formar um triangulo com {r1}, {r2} e {r3}')
    print('grato!')
else:
    print(f'não é possivel formar um triangulo com {r1}, {r2} e {r3}')
    print('grato!')