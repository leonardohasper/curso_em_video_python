import random
import time

print('PAR OU ÍMPAR')
#soma = 0
cont = 0

while True:
    userInput = int(input('Digite um número: '))
    parImpar = input('Par ou Ímpar? [P/I]').upper()
    pcInput = random.randint(1, 10)
    soma = userInput + pcInput
    par = soma % 2 == 0
    impar = soma % 2 == 1
    cont += 1

    if parImpar == 'P' and soma % 2 == 0:
        print(f'Você venceu! {soma} é PAR! ')
    elif parImpar == 'I' and soma % 2 == 0:
        print(f'Você perdeu! {soma} é PAR!')
        cont -= 1
        break
    if parImpar == 'I' and soma % 2 == 1:
        print(f'Você venceu! {soma} é ÍMPAR!')
    elif parImpar == 'P' and soma % 2 == 1:
        print(f'Você perdeu! {soma} é ÍMPAR!')
        cont -= 1
        break


    print(f'Você jogou {userInput} e o Computador {pcInput}. Total de {soma}')


print(f'Você jogou {userInput} e o Computador {pcInput}. Total de {soma}')
print(f'GAME OVER! Você ganhou {cont} vezes')
