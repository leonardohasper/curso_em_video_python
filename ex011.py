#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Para uma área de {}m², é necessário {:.1f} litro(s) de tinta '.format(area, tinta))