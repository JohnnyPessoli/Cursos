km = float(input('Informe a quantidade de Km rodados com seu carro: '))
dias = float(input('Informe quantos dias você alugou o carro: '))
c = 60
ckm = 0.15
t = (c*dias)+(ckm*km)
print(f'O valor do aluguel será de R$ {(c*dias):.2f} referente aos {dias:.2f} dias, e mais R$ {ckm*km} referente aos {km:.2f} km rodados, totalizando R$ {t} a pagar')
