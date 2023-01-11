#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção Inteira.

import math

num = float(input('Digite um número float: '))
porcaoInt = math.trunc(num)
print('A porção inteira de {} é {}'.format(num, porcaoInt))

