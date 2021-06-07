#calcula o valor da passagem da viagem considerando o Km
distancia = int(input('Qual a Distancia da Viagem em KM: '))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da passagem é R${valor}')
else:
    valor = distancia * 0.45
    print(f'O Valor a pagar pela passagem é R${valor}')