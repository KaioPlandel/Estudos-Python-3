salario = float(input('Digite O Salário: '))

if salario > 1250:
    aumento = (salario * 0.10) + salario
    print(f'O Seu Salário com 10% de aumento fica R${aumento:.2f}')
else:
    aumento = (salario * 0.15) + salario
    print(f'O Seu Salário com o aumento de 15% fica R${aumento:.2f}')
