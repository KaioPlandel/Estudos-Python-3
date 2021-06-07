#verifique se a cidade começa com o nome Santos
city = str(input('Digite o nome da Cidade: ')).strip().upper().split()[0]
if city == 'SANTOS':
    print('A sua Cidade Começa com o Nome Santos')
else:
    print('A sua Cidade não Começa com o Nome Santos')