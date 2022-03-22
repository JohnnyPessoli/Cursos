emprestimo = float(input('Qual o valor da casa? ').strip())
salario = float(input('Qual seu salário? ').strip())
tempo = int(input('Em quantos meses você deseja pagar? ').strip())
teto = salario *0.30
if emprestimo/tempo <= teto:
    print(f'Você irá pagar uma mensalidade de {emprestimo/tempo}')
else:
    print('O valor do seu salário não é o suficiente para o emprestimo')