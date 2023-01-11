import time
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
choice = 0
sair = 5
while choice != sair:
    print('========Menu de Opções========')
    choice = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]NOVOS NÚMEROS\n[4]MAIOR\n[5]SAIR'))
    time.sleep(1)
    if choice == 1:
        soma = n1 + n2
        print('A soma entre os valores é {}'.format(soma))
    if choice == 2:
        mult = n1 * n2
        print('A multiplicação entre os valores é de {}'.format(mult))
    if choice == 3:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    if choice == 4:
        if n1 > n2:
            print('{} é maior'.format(n1))
        else:
            print('{} é maior'.format(n2))


print('Saindo...')



