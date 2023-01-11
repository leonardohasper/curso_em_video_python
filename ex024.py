#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".


city = input('Digite o nome da cidade: ').title().split()

if 'Santo' in city[0]:
    print('Verdadeiro')
else:
    print('Falso')







