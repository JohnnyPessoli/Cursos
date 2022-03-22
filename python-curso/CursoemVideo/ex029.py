velocidade = int(input('Qual a velocidade atual do carro? '))
multa = float(velocidade * 7)-80
if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade e foi multado em R${float(velocidade-80)*7:.2f}!')
print('Tenha um bom dia, dirija com cuidado!')

