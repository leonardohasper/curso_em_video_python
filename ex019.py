#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
import time

lista = input('Primeiro aluno: '.capitalize()), \
        input('Segundo aluno: '), \
        input('Terceiro aluno: '), \
        input('Quarto aluno: ')


print('Alunos a serem sorteados: ', lista)

print('SORTEANDO...')
time.sleep(2)

print('O aluno sorteado para apagar o quadro foi: {}'.format(random.choice(lista)))
