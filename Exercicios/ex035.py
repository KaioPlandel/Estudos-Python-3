#verifica se forma um triangulo
a = float(input('Digite a primeira Reta: '))
b = float(input('A Segunda: '))
c = float(input('A Terceira: '))

if (a < b + c and a > b - c) and (b < a + c and b > a- c ) and (c < a + b and c > a - b):
    print('As medidas passadas PODE FORMAR UM TRIANGULO')
else:
    print('Não FORMA UM TRIANGULO')