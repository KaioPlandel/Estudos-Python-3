#Crie uma lista que gere 7 numeros e mostre a lista e a soma de todos os numeros
import random

lista = []
while len(lista) < 7:
    num = random.randint(1, 100)
    if num not in lista:
        lista.append(num)
    lista.sort()

print(lista)
print(f'A soma de todos os Numeros da lista Gerada é {sum(lista)}')


