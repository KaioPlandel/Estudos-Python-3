#olhe se o nome pertence a familia Silva
nome = str(input('Digite seu Nome: ')).strip().upper()

if 'SILVA' in nome:
    print('Você é da Família Silva')
else:
    print('Você não Pertence a Familia Silva')