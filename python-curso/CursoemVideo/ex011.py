a = float(input('Digite a altura de sua parede: '))
lr = float(input('Digite a largura de sua parede: '))
area = a * lr
qt = area / 2
print(f'Sua parede tem {a}x{lr}')
print(f'A quantidade de litros necessário para pintar {area:.2f}m² é de {qt:.2f} litros')