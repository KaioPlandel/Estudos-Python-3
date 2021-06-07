#Sistema Desenvolvido para a Faculdade

print('~='*30)
print('                   SISTEMA DE NOTAS DA UVV')
print('~='*30)
totalAlunos = 4                                # numeros de alunos para Cadastrar Optei por colocar em uma Variavel
aluno = 0                                        # para trabalhar melhor com %
aprovado = 0
reprovado = 0

while aluno < totalAlunos:  #Programa vai cadastra de acordo com o numero de Total de alunos que coloquei na variavel
    print('~=' * 30)
    aluno +=1
    print(f'               Pontuação Referente ao aluno {aluno} ')
    aop1 = float(input('Digite a Nota da OAP1 [0, 1] : '))

    while aop1 > 1 or aop1 < 0:   # Aqui decidir fazer um tratamento de erro de acordo com meu conhecimento,
        print('NOTA INVÁLIDA')     #Caso digite um valor acima da Nota Recebe um ERRO
        aop1 = float(input('Digite a Nota OAP1 Válida [0, 1]: '))

    aop2 = float(input('Digite a Nota da OAP2  [0, 2]: '))
    while aop2 > 2 or aop2 < 0:
        print('NOTA INVÁLIDA')
        aop2 = float(input('Digite a Nota OAP2 Válida  [0, 2]: ')) #Mesmo tratamento de ERRO

    aop3 = float(input('Digite a Nota da OAP3 [0, 1]:'))
    while aop3 > 1 or aop3 < 0:
        print('NOTA INVÁLIDA')
        aop3 = float(input('Digite a Nota OAP3 Válida  [0, 1]: '))

    provaRegular = float(input('Digite a Nota da Prova Regular [0, 6]: '))
    while provaRegular > 6 or provaRegular < 0:
        print('NOTA INVÁLIDA')
        provaRegular = float(input('Digite a Nota Válida  [0, 6]: '))

    mediaM = aop1 + aop2 + aop3 + provaRegular
    print(f'A Media do Aluno {aluno} é {mediaM}')

    if mediaM < 7:                                          #Media sendo Menor que 7 Vai pedir a nota de Recuperação
        print('~=' * 30)
        print('          Você Deve fazer a Prova de Recuperação')
        print('~=' * 30)
        pRecuperacao = float(input('Digite a nota da Prova de Recuperação [0, 10]: '))
        while pRecuperacao > 10 or pRecuperacao < 0:
            print('NOTA INVÁLIDA')
            pRecuperacao = float(input('Digite a Nota Válida  [0, 10]: '))
        if pRecuperacao >= 5:                                                           # Se a nota da Recuperação for maior ou ingual a 5 == Aprovado
            aprovado += 1
            print(f'O Aluno {aluno} foi Aprovado')
        else:
            print(f'O Aluno {aluno} foi Reprovado')
            reprovado += 1
    else:
        aprovado += 1
        print(f'O Aluno {aluno} foi APROVADO')

totaslAp = (aprovado / totalAlunos) * 100  # aqui o sistme calcula a porcentagem de acordo com o total de alunos
totalRp = (reprovado / totalAlunos) * 100
print('~='*30)
print( '                     RESULTADO ')
print('~='*30)
print(f'Total de Alunos Cadastrados foram {totalAlunos}')
print(f'Foram Aprovados {totaslAp:.0f}%')
print(f'Foram Reprovados {totalRp:.0f}% ')
