#num = int(input('Digite um número inteiro: '))
soma = 0
cont = 0

while True:
    num = int(input('Digite um número inteiro: '))

    if num == 999:
        break

    cont += 1
    soma += num
    #print(cont)
    #print(soma)

print(f'{cont} números foram digitados\n{soma} foi a soma dos números')


