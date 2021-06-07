soma = 0
n1 = 0
for c in range(0,4):
    n = float(input(f'Digite o {c+1} Numero: '))
    if c <= 2:
        soma += n
    else:
        n1 = n

media = soma / 3

if media == n1:
    print('São Inguais')
