a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'o menor é {menor}')
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior é {maior}')