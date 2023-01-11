num = int(input('Digite um número: '))
c = 1
soma = num
while num != 999:
    num = int(input('Digite um número: '))
    c = c + 1
    soma = soma + num
    if num == 999:
        soma = soma - num

print('Foram digitados {} números e a soma entre eles foi de {}'.format(c, soma))



#print(c)





