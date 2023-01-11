import time
dadosAluno = {}
alunos = []
while True:
    dadosAluno['nome'] = str(input('Nome do Aluno: ')).title()
    dadosAluno['media'] = float(input('Média do Aluno: '))
    alunos.append(dadosAluno.copy())
    #print(f'Nome = {dadosAluno["nome"]}')
    #print(f'Média = {dadosAluno["media"]}')
    resp = str(input('Continuar?[S/N] ')).upper()
    if resp in 'N':
        break

for a in alunos:
    if a['media'] >= 7:
            print(f'Aluno {a["nome"]} com a média de {a["media"]} está APROVADO')
    else:
            print(f'Aluno {a["nome"]} com a média de {a["media"]} está REPROVADO')


