frase = str(input('Digite Algo: ')).strip().upper()
separa = frase.split()
junto = ''.join(separa)

novo = junto[::-1]
if novo == junto:
    print('É um Polimetro')
else:
    print('Não é um Polimetro')

