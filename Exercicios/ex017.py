from math import sqrt
a = float(input('Digite o Cateto Oposto do Triangulo: '))
b = float(input('Digite o Cateto Adjacente do Triangulo: '))
hipotenusa = a**2 + b**2
c = sqrt(hipotenusa)

print(f'O cumprimento da Hipotenusa é {c}')