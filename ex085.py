lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Os números pares foram {sorted(lista[0])}')
print(f'Os números ímpares foram {sorted(lista[1])}')


'''lista = []
par = []
impar = []
for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    lista.append(num)

print(f'Os valores pares foram: {sorted(par)}')
print(f'Os valores ímpares foram: {sorted(impar)}')'''

