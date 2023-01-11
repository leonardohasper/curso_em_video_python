#Faça um programa que mostre a tabuada de vários números,
#um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

print('===========TABUADA===========')
cont = 0
soma = 0
num = 0
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for cont in range(0, 10):
        #num = int(input('Digite um número para ver sua tabuada: '))
        cont += 1
        tab = num * cont
        print(f'{num} x {cont} = {tab}')

print('FIM')
