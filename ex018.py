import math

angulo = int(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(seno, cos, tan))
