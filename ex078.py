valores = []
maior = 0
menor = 0
for cont in range(5):
    v = int(input('Digite um valor: '))
    valores.append(v)
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'O maior valor foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valores[indice] == maior:
        print(f'{indice}...', end='')
print()
print(f'O menor valor foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valores[indice] == menor:
        print(f'{indice}...', end='')





