s = float(input('digite seu salario; '))
if s <= 1250:
    print('seu salario foi reajustado para {:.2f}'.format(s * 1.15))
else:
    print('seu salario foi reajustado para {:.2f}'.format(s * 1.10))
