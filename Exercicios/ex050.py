soma = 0
for c in range(0,6):
    n = int(input('Digite um numero par para fazer a Soma: '))
    if n % 2 == 0:
        soma += n
print(soma)