cont = 0
soma = 0
for c in range (1, 500+1):
    if c % 2 == 1:
        #print(c)
        if c % 3 == 0:
            #print(c)
            soma += c
            cont += 1
            #print(c)

print('A soma dos {} valores é: {}'.format(cont, soma))
