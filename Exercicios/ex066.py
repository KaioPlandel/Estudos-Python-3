#programa que soma os numeros digitados
s = 0
cont = 0
while True:
    n = int(input('Digite um numero para Finazalizar digite 999: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} Numeros')
print(f'A Soma entre eles é {s}')