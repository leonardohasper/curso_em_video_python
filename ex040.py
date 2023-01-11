n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if 0 < media < 5:
    print('REPROVADO!')
elif 5 <= media < 6.9:
    print('RECUPERAÇÃO!')
elif 7 <= media < 10.1:
    print('APROVADO!')
else:
    print('DIGITE UMA NOTA VÁLIDA')





