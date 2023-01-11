import math
catOposto = float(input('Comprimento do cateto oposto: '))
catAdja = float(input('Comprimento do cateto adjacente: '))

hipo = math.hypot(catAdja, catOposto)
print('{:.2f}'.format(hipo))
