""" import math
x = float(input('Digite o angulo: '))
print(f'O valor de seno do angulo {x} é {math.acos(math.radians(x)):.2f}\n'
      f'O valor de cosseno do angulo {x} é {math.asin(math.radians(x)):.2f}\n'
      f'O valor da tangente do angulo {x} é {math.atan(math.radians(x)):.2f}')"""


"""import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = (n1, n2, n3, n4)
print(f'O aluno sorteado foi {random.choice(lista) }')"""

"""import random

n1 = str('Ana')
n2 = str('joao')
n3 = str('andre')
n4 = str('jose')
lista = (n1, n2, n3, n4)
escolhido = random.choice(lista)
ordem = random.sample(lista, 4)
print(f'Os alunos devem apresentar na seguinte ordem{ordem}')"""

import playsound
playsound.playsound('musica.mp3')

import pygame
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
