v = float(input('digite a distancia da sua viagem em Km: '))
if v <= 200:
    print(f'o valor da sua viagem vai ser R${v * 0.5}')
elif v > 200:
    print(f'o valor da sua viagem vai ser R${v * 0.45}')
