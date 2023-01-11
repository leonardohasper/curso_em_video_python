from datetime import date
anoHoje = date.today().year
trab = {'Nome': str(input('Nome: ')).title(),
               'Ano de Nascimento': int(input('Ano de Nascimento: ')),
               'Carteira de Trabalho': int(input('Carteira de Trabalho: ')),
               'Ano de Contratação': '',
               'Salário': '',
               'Aposentadoria': ''}

idade = anoHoje - trab['Ano de Nascimento']
trab['Idade'] = trab['Ano de Nascimento']
del trab['Ano de Nascimento']
trab['Idade'] = idade

if trab['Carteira de Trabalho'] != 0:
    trab['Ano de Contratação'] = int(input('Ano de Contratação: '))
    trab['Salário'] = float(input('Salário: '))
    tempoTrabalho = anoHoje - trab['Ano de Contratação']
    anosAposentar = 35 - tempoTrabalho
    trab['Aposentadoria'] = idade + anosAposentar
else:
    del trab['Ano de Contratação']
    del trab['Salário']
    del trab['Aposentadoria']

for k, v in trab.items():
    print(f'{k} = {v}')
