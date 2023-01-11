#Pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 parta viagens mais longas.


distance = int(input('Distância da Viagem: '))
if distance <= 200:
    total = distance * 0.5
    print('R$0.50 centavos por km. Valor a pagar: R${}'.format(total))
else:
    total2 = distance * 0.45
    print('R$0.45 centavos por km. Valor a pagar: R${}'.format(total2))
