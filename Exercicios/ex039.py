#programa de alistamento Militar
from datetime import date
atual = date.today().year
ano = int(input('Digite o Ano de Nascimento: '))
idade = atual - ano
print(f'Você tem {idade} anos')
if idade < 18:
    falta = 18 - idade
    print('Voce ainda não tem idade de se Alistar')
    print(f'Falta {falta} anos')
elif idade == 18:
    print('Esta na hora de se Alistar')
else:
    passou = idade - 18
    print('Ja passou da Hora de se Alistar')
    print(f'Ja se passaram {passou} anos')
