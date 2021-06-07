nome = str(input('Digite no nome Completo: '))
print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.count(" "))
primeiroNome = nome.split()
nome1 = primeiroNome[0]
print(len(nome1))

