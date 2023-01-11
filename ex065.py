num = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N]')).upper()
c = 1
soma = num
maiorNum = num
menorNum = num

while continuar != 'N':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]')).upper()
    soma = soma + num
    c += 1
    media = soma / c
    #print(soma)

    if num > maiorNum:
        maiorNum = num
        #print(maiorNum)

    if num < menorNum:
        menorNum = num

print('Você digitou {} números e a média foi {:.2f}'.format(c, media))
print('O maior número foi {} e o menor foi {}'.format(maiorNum, menorNum))






