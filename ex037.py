#Escreva um programa em Python que leia um número inteiro qualquer e peça
#para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

import math
number = int(input('Digite um número inteiro: '))
conversao = int(input('[1] para binário\n[2] para octal\n[3] para hexadecimal'))

if conversao == 1:
    print(bin(number)[2:])
elif conversao == 2:
    print(oct(number)[2:])
elif conversao == 3:
    print(hex(number)[2:])
else:
    print('OPÇÃO INVÁLIDA!')
