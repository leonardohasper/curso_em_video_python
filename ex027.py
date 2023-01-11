#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = input('Digite seu nome completo: ').title().strip().split()
first = name[0]
last = name[-1]

print('O primeiro nome é {} e o último nome é {}'.format(first, last))






