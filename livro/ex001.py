#A soma dos sete primeiros inteiros positivos
import random
listaNumeros = [1,2,3,4,5,6,7]

print(sum(listaNumeros))

lista = []
while len(lista) < 7:
    num = random.randint(1, 100)
    if num not in lista:
        lista.append(num)
    lista.sort()

print(lista)
print(f'A soma de todos os Numeros da lista Gerada é {sum(lista)}')


