print('='*10)
print('Digite um número abaixo e eu lhe direi se é impar ou par')
print('='*10)
numero = float(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print('Este número é par')
else:
    print('Este número é impar')


