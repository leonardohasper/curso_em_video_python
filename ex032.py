#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
currentYear = date.today().year
#print(currentYear)

year = int(input('Digite um ano(Tecle 0 para analisar o ano atual):  '))
if year == 0:
    year = currentYear
    print(currentYear)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Bissexto')
else:
    print('Não é bissexto')
