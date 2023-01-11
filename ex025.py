#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.


name = input('Digite seu nome completo: ').title()

if 'Silva' in name.split():
    print('O nome possui Silva')

else:
    print('O nome não possui Silva')






