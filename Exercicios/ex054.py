from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for c in range(0,7):
    n = int(input('Digite a data de Nacimento: '))
    idade = hoje - n
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} são Maiores de IDADE')
print(f'{menor} são Menores de IDADE')