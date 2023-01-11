'''num = [2, 5, 8, 4]
num.append(666) #adiciona 666 no final da lista
num.sort() #coloca a lista em ordem de valores
num.sort(reverse=True) #coloca a lista de trás pra frente
num.insert(0, 667) #insere o número 667 na posição 0
num.pop(0) #deleta a posição 0 da lista
print(f'Essa lista tem {len(num)} elementos') #mostra o tamanho da lista
if 5 in num:
    num.remove(5) #retira o PRIMEIRO elemento '5' da lista
else:
    print('Não achei o valor 5')

print(num)
#==================================================================================
valores = []
valores.append(666)
valores.append(667)
valores.append(668)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

#==================================================================================
valores = []
cont = 0
for cont in range(5):
    v = int(input('Digite 5 valores: '))
    valores.append(v)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

#==================================================================================
#ligação entre a e b
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
#==================================================================================
#cria uma cópia
a = [2, 3, 4, 7]
b = a[:]#   : = todos os itens de 'a'
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
