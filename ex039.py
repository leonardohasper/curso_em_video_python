from datetime import date
birthYear = int(input('Informe o Ano de Nascimento: '))
currentYear = date.today().year
age = currentYear - birthYear

if 0 < age < 18:
    difference = 18 - age
    print('Você tem {} anos. Faltam {} anos para o seu alistamento militar.'.format(age, difference))
elif age == 18:
    print('Você tem {} anos. Chegou a hora de se alistar.'.format(age))
elif 100 > age > 18:
    difference2 = age - 18
    print('Você tem {} anos. Seu alistamento foi há {} anos.'.format(age, difference2))
else:
    print('DIGITE UM ANO VÁLIDO')





