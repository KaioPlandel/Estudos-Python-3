#crie uma função que mostre o sobreNome da pessea "," a primeira letra do Nome dela ex Kaio Plandel = mostre Plandel, K
def inverterNome(st):
    nome = st.capitalize()
    sobre = nome.split()
    forma = sobre[1]
    print(f'{forma},{sobre[0][0]}')

inverterNome('larissa gomes')