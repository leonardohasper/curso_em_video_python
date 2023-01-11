numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze'
           , 'Doze', 'Treze')
c = 0
userInput = int(input('Digite um número: '))

while userInput not in range(0, 14):
    userInput = int(input('Tente Novamente. Digite um número de 0 a 13: '))

print(f'Você digitou: {numeros[userInput]}')

