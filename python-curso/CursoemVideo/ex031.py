"""entrada = float(input('Quala a distância da sua viagem? '))
passagem1 = 0.50
passagem2 = 0.45
print(f'Você esta prestes a iniciar uma viagem de {entrada:.2f}Km.')
if entrada > 200:
    print(f'Sua passagem custará R${entrada*passagem2:.2f}')
else:
    print(f'Sua passagem vai custar R${entrada*passagem1:.2f}')
print('Faça uma boa viagem!')"""

entrada = float(input('Quala a distância da sua viagem? '))
if entrada >= 200:
    preco = entrada*0.50
else:
    preco = entrada *0.45
print(f'O valor da passagem será de R${preco:.2f}')