#pergunte o nome. mostre o nome com as letras M e m, quantas letras tem tirando os espaços e quantas letras tem o primeiro nome.
nome = str(input('Digite no nome Completo: '))
print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.count(" "))
primeiroNome = nome.split()
nome1 = primeiroNome[0]
print(len(nome1))

