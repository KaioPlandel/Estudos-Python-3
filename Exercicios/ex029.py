#radar de transito
radar = int(input('Velocidade Atual: '))
if radar > 80:
    print(f'Você está a {radar}Km/hr Foi MULTADO')
    multa = (radar -80) * 7
    print(f'O valor a pagar da Multa é R${multa:.2f}')
else:
    print(f'Você esta a {radar} Dirija com segurança')