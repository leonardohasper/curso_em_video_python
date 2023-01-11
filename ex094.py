import time
pessoa = {}
pessoas = []
c = 0
somaIdade = 0
mulheres = []
while True:
    pessoa["nome"] = str(input('Nome: ')).title()
    c += 1
    while True:
        pessoa["sexo"] = str(input('Sexo:[F/M]')).upper()
        if pessoa["sexo"] in 'FM':
            break
        else:
            print('Resposta inválida! Tente novamente')

    if pessoa["sexo"] == 'F':
        mulheres.append(pessoa["nome"])
    pessoa["idade"] = int(input('Idade: '))
    somaIdade += pessoa["idade"]
    media = somaIdade / c

    pessoas.append(pessoa.copy())
    resp = str(input('Continuar?[S/N] ')).upper()
    if resp not in 'NS':
        while True:
            print('ERRO! Responda apenas com S ou N')
            resp = str(input('Continuar?[S/N] ')).upper()
            if resp == 'N':
                break
    if resp in 'N':
            break

print('FINALIZANDO...')
time.sleep(1)
print(f'Pessoas Cadastradas: {c}')
time.sleep(1)
print(f'Média de Idade: {media:.2f} anos')
time.sleep(1)
for m in mulheres:
    print(f'Mulheres cadastradas: {mulheres}')
time.sleep(1)
print('Pessoas com idade acima da média:')
for pessoa in pessoas:
    if pessoa["idade"] > media:
        print(f'{pessoa["nome"]} com {pessoa["idade"]} anos')

