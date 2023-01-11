listagem = []
while True:
    prod = str(input('Digite o nome do produto: ')).capitalize()
    listagem.append(prod)
    preco = float(input('Digite o preço do produto: '))
    listagem.append(preco)
    continuar = input('Deseja continuar? [S/N]').lower()
    if continuar == 'n':
        break

print(f'{"LISTA DE PRODUTOS":^25}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    else:
        print(f'R${listagem[pos]}')












