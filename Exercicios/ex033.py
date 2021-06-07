n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite Outro: '))
n3 = int(input('Digite o Último: '))
maior = 0
menor = 0

if n1 > maior:
    maior = n1
    menor = n1
if n2 > maior:
    maior = n2
if menor > n2:
    menor = n2
if n3 > maior:
    maior = n3
if menor > n3:
    menor = n3


print(f'O Maior Numero é {maior}')
print(f'O Menor Numero é {menor}')