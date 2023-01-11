print(19 * '=')
print('CADASTRE UMA PESSOA')
print(19 * '=')
cont = 0
contMulher = 0
contHomem = 0

while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        cont += 1
        #print(cont)

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = input('Sexo: [M/F]').upper()
        if sexo == 'M':
            contHomem += 1
            #print(contHomem)

        if sexo == 'F' and idade < 20:
            contMulher += 1
            #print(contMulher)

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Deseja Continuar? [S/N]').upper()
    if continuar == 'N':
        break


print(f'{cont} pessoas com mais de 18 anos foram cadastradas.')
print(f'{contHomem} homens foram castrados')
print(f'{contMulher} mulher menores de 20 anos.')









