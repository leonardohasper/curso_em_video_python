numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado')

c = 0
for num in numeros:
    if num % 2 == 0:
        c = c + 1
        #print('par')
        #print(c)

print(f'Os valores pares digitados foram {c}')




