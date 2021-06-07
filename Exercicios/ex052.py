n = int(input('Digite um Numero: '))
cont = 0
for c in range(1,999):
    if n % c == 0:
        cont += 1
if cont == 2:
    print('é primo')


