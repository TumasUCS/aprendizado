d = int(input('quantos dias o carro foi alugado? '))
k = float(input('quantos km foi rodado com o carro? '))
vd = d * 60
vk = k * 0.15
print('o valor total ficou de {:.2f}'.format(vd + vk))