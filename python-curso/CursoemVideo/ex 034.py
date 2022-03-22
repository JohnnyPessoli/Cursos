salario = float(input('Qual é o salário do funcionário? R$'))
if salario >1250:
    salario = salario *1.10
else:
    salario = salario * 1.15

print(f'Seu novo salário será de R${salario:.2f}')