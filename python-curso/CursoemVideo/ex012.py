p = float(input('Digite o valor do produto para saber seu desconto: '))
d = (p * 1.05)- p
print(f'Considerando que o valor do produto é de R${p:.2f}, seu desconto será de R${d:.2f}, e o total a pagar será de R$ {(p-d):.2f}')
