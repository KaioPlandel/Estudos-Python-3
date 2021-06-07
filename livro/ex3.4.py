# Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string).
# O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos.
# Dependendo do resultado, uma mensagem apropriada deverá ser impressa.
# Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar. Aqui está um exemplo de um login bem-sucedido:

lista = ['kaio','paola','felipe','gustavo']
nome = input('Digite o Nome: ')

if nome in lista:
    print('Você Entrou')
else:
    print('Nome Desconhecido')
print('FIM')