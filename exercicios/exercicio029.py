import math
v = float(input('Digite sua velocidade em Km/h: '))
print('voce estava a {}Km/h'.format(v))
if v > 80:
    print('você foi multado em R${} por excesso de velocidade'.format(7 * (v - 80)))
else:
    print('você esta dentro da velocidade permitida')