pessoas = []
dados = []
maiorPeso = 0
menorPeso = 0
while True:
    nome = str(input('Nome: ')).capitalize()
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)

    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]

    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]

        if dados[1] < menorPeso:
            menorPeso = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    continuar = input('Continuar? [S/N]').upper()
    if continuar in 'N':
        break

print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'Maior peso foi {maiorPeso}kg...Peso de: ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print('')
print(f'Menor peso foi {menorPeso}kg...Peso de: ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')

