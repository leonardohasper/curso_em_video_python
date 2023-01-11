#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
dataAtual = date.today().year
contMenor = 0
contMaior = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento da {}ª pessoa:  '.format(c)))
    idade = dataAtual - ano
    if idade < 17:
        contMenor += 1
    elif idade >= 18:
        contMaior += 1

print('{} são maiores de idade\n{} são menores de idade'.format(contMaior, contMenor))

