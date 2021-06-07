#classificação do atleta de acordo com a idade
from datetime import date
nascimento = int(input('Digite o Ano de Nascimento: '))
idade = date.today().year - nascimento
print(f'A IDADE DO ATLETA É {idade}')
if idade <= 9:
    print('ATLETA MIRIM')
elif idade <= 14:
    print('ATLETA INFANTIL')
elif idade <= 19:
    print('ATLETA JUNIOR')
elif idade <= 20:
    print('ATLETA SENIOR')
else:
    print('ATLETA MASTER')