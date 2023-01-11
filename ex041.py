from datetime import date
birthYear = int(input('Ano de nascimento: '))
currentYear = date.today().year
print(currentYear)
age = currentYear - birthYear

if 0 < age <= 9:
    print('MIRIM!')
elif 10 <= age <= 14:
    print('INFANTIL!')
elif 15 <= age <= 19:
    print('JUNIOR!')
elif 20 <= age <= 22:
    print('SENIOR!')
elif 23<= age <100:
    print('MASTER!')
else:
    print('OPÇÃO INVÁLIDA!')








