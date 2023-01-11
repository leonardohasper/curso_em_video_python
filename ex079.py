valores = []
while True:
    valor = int(input('Digite um valor:  '))
    if valor not in valores:
        valores.append(valor)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado! Digite outro valor...')
    continuar = input('Deseja Continuar? [S/N]').upper()
    if continuar == 'N':
        break

print(f'Você digitou os valores {sorted(valores)}')