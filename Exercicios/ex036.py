print('-='*30)
print(f'                 TENTATIVA DE EMPRESTIMO')
print('-='*30)

casa = float(input('Digite o Valor da Casa: '))
salario = float(input('Qual o seu Salário: '))
anos = int(input('Quantos anos Você Pretende Pagar: '))
meses = 12 * anos

prestacao = casa / meses

if prestacao > salario * (0.30):
    print('O valor da sua Mensalidade é maior que 30% do Seu Salário')
    print('Emprestimo \033[32mNEGADO\033[m')
else:
    print('O seu Salario é compativel com a Prestação\033[m')
    print('\033[43mEMPRESTIMO ACEITO\033[m')


