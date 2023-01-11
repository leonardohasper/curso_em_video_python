lista = []
listaPar = []
listaImpar = []

while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)

    if numeros % 2 == 0:
        listaPar.append(numeros)
    else:
        listaImpar.append(numeros)

    continuar = input('Deseja continuar? [S/N]')
    if continuar in 'nN':
        break

print(f'Todos os números digitados foram {sorted(lista)}')
print(f'Os números pares foram {sorted(listaPar)}')
print(f'Os números ímpares foram {sorted(listaImpar)}')
