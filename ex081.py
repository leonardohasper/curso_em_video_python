lista = []
cont = 0
cont5 = 0
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    cont += 1

    continuar = input('Quer continuar?[S/N] ').upper()
    if continuar == 'N':
        break

lista.sort(reverse=True)
print(f'Você digitou {cont} números.')

if 5 in lista:
    cont5 += 1
    print(f'O valor 5 está na lista e foi digitado {lista.count(5)} vezes.')
else:
    print('O valor 5 não está na lista')

print(f'A ordem decrescente da lista é {lista}')


