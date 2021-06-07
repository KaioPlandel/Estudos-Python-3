n = 0
soma = n
cont = 0
while n != 999:
    if n != 999:
        soma += n
        n = int(input('Digite um numeo: '))
        cont += 1
    else:
        print('SAINDO DO PROGRAMA')

print(f'Foram Digitados {cont-1} Numeros\n A soma entre eles é {soma}')