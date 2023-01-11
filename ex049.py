num = int(input('Digite um número pra ver sua tabuada: '))
cont = 0
for c in range (1, 11):
    mult = num * c
    print('{} x {} = {}'.format(num, c, mult))
    #mult = num * c
    #print(cont)
    #print(c)