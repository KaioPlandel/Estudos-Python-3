# adicione 4 nomes e mostre a ordem sorteado deles
import math
import random

a1 = input('NOme 1: ')
a2 = input('Nome 2: ')
a3 = input('Nome 3: ')
a4 = input('Nome 4: ')

lista = [a1,a2,a3,a4]
random.shuffle(lista)
print(lista)
