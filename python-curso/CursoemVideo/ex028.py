import random
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número estou pensando?'))
print('Processando...')
sleep(2)
computador = random.randint(0, 5)
if jogador == computador:
    print('Muito bem você acertou, eu estava pensando neste número!')
else:
    print(f'Sinto muito, eu estava pensando no número {computador}, tente novamente')
