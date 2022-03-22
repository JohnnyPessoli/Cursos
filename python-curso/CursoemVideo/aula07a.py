# nome = input('Qual é seu nome? ')
# print(f'Prazer em lhe conhecer {nome:20}!')
# print(f'Prazer me lhe conhecer {nome:>20}!')
# print(f'Prazer em lhe conhecer {nome:<20}!')
# print(f'Prazer em lhe conhecer {nome:^20}!')
# print(f'Prazer em lhe conhecer {nome:=^20}!')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
m = n1 * n2
div = n1 / n2
divi = n1 // n2
divr = n1 % n2
raiz = s ** (1/2)
raiz3 = s ** (1/3)
total = s+m+div+divi+divr+raiz+raiz3
print(f'A soma de {n1} mais {n2} é {s:.2f},\n'
      f'a multiplicação entre {n1} e {n2} é {m:.2f},\n'
      f'a divisão entre {n1} e {n2} é {div:.2f},\n'
      f'a divisão inteira de  {n1} e {n2} é {divi:.2f},\n'
      f'o resto da divisão entre {n1} e {n2} é {divr:.2f},\n'
      f'a raiz quadrada da soma de {n1} e {n2} é {raiz:.2f},\n'
      f'e a raiz cubica da soma de {n1} e {n2} é {raiz3:.2f},\n'
      f'e a soma de todos os resultados é {total:.2f} ')
