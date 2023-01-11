contMulher = 0
maiorIdade = 0
menorIdade = 0
nomeVelho = ''
mediaIdade = 0
for c in range(1, 4):
    nome = input('Nome da {}ª pessoa: '.format(c))
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = int(input('Sexo da {}ª pessoa:\n[1] para Feminino\n[2] para Masculino'.format(c)))
    mediaIdade = mediaIdade + idade
    if sexo == 1 and idade < 20:
        contMulher += 1
    if sexo == 2 and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
mediaIdade = mediaIdade / c

print('O homem mais velho se chama {} e tem {} anos.'.format(nomeVelho, maiorIdade))
print('{} mulheres com menos de 20'.format(contMulher))
print('media de idade: {:.2f}'.format(mediaIdade))

