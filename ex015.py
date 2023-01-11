#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

distancia = float(input('Quantos Km foram percorridos: '))
dias = int(input('Quantos dias o carro foi usado: '))
precoDia = dias * 60
precoDistancia = distancia * 0.15
precoTotal = precoDia + precoDistancia
print('O valor a pagar por {} dias utilizados e {} quilômetros rodados é de: {} reais'
      .format(dias, distancia, precoTotal))

