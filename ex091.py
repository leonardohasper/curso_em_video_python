from random import randint
import time
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
ranking = {}
print('VALORES SORTEADOS')
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    time.sleep(1)

ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
cont = 1
print('RANKING DOS JOGADORES')
for k, v in ranking:
    print(f'{cont}º lugar: {k} com {v}')
    cont += 1
    time.sleep(1)







