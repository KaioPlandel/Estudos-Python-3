#mostre quantas vezes a palavra A aparece, onde aparece pela primeira e ultima vez
palavra = str(input('Digite um Texto Qualquer: ')).strip().upper()

print(f'A palavra A aparece {palavra.count("A")} Vezes')
print(f'Ela aparece pela primeira vez na Posição {palavra.find("A")+1}')
print(f'A Ultima posição que ela aparece é {palavra.rfind("A")+1}')