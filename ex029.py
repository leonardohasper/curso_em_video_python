#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

carSpeed = int(input('Velocidade do carro: '))
if carSpeed > 80:
    ticket = (carSpeed - 80) * 7
    print('Você foi multado.. A multa é de {} reais.'.format(ticket))
else:
    print('Siga sua viagem!')
