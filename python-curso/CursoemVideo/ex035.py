a = float(input('Digite a variável 1: '))
b = float(input('Digite a variável 2: '))
c = float(input('Digite a variável 3: '))
if a < b+c and b < a+c and c < a+b:
    print('Podem formar Triangulo')
else:
    print(f'Não Pode ser um TRIANGULO')