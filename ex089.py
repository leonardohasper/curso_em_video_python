alunos = []
cont = 1
while True:
    nome = str(input(f'Nome do {cont}º aluno: ').title())
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    cont += 1

    continuar = str(input('Continuar? [S/N)')).upper()
    if continuar in 'N':
         break

print(f'{"No.":<4}{"NOME":<35}{"MEDIA":>25}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<35}{a[2]:>24.1f}')
print('=-'*32)
while True:
    inputChoice = int(input('Mostrar notas de qual aluno?(999 para cancelar)>>> '))
    if inputChoice == 999:
        print('FINALIZANDO...')
        break
    if inputChoice <= len(alunos):
        print(f'Mostrando notas de {alunos[inputChoice][0]}...{alunos[inputChoice][1]}')
