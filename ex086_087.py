matriz = [[0, 0, 0], #l1
          [0, 0, 0], #l2
          [0, 0, 0]] #l3
          #c1#c2#c3
par = []
maiorValor = 0
listaC = []
linha1 = []
#o primeiro for irá percorrer as 3 linhas
for l in range(0, 3): #l = linha
    print(f'Linha {l}')
#o segundo for irá percorrer as 3 colunas
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Coluna {c}ª: '))
        #if para ver quais elementos são par
        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
        #if para ver quais elementos são da 3ª coluna
        if c == 2:
            listaC.append(matriz[l][c])
        #if para ver qual o maior valor da linha1
        if l == 1 and c == 0:
            maiorValor = matriz[1][c]
        else:
            if matriz[1][c] > maiorValor:
                maiorValor = matriz[1][c]

#for usado para a formatação da matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma de todos os pares é de: {sum(par)}')
print(f'A soma dos valores da 3ª coluna é: {sum(listaC)}')
print(f'O maior valor da 2ª linha é {maiorValor}')




































'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha, coluna}: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()


print(matriz % 2 == 0)'''
