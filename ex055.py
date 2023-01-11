#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    pesoUsuario = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = pesoUsuario
        menor = pesoUsuario
    else:
        if pesoUsuario > maior:
            maior = pesoUsuario
        if pesoUsuario < menor:
            menor = pesoUsuario

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))




