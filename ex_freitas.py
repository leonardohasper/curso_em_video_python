lista = ['Dez', 'Nove', 'Oito', 'Sete', 'Seis', 'Katherine', 'Quatro', 'Três', 'Dois', 'Um']
i = len(lista)  #i = 10
while i >= 1:
    print('Início do While')
    print('i = {}'.format(i))
    print(lista[i-1])
    i = i - 1
    print('FIM DO LOOP')
    print('')
print('FIM DO WHILE')