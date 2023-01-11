termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termosInicio = int(input('Digite quantos termos terá a PA: '))
cont = termo1
limit = termosInicio * razao
mais =
total = termosInicio
while total != 0:
    total = termosInicio + mais
    while cont <= limit:
        cont += razao
        total = cont + termo1
        print(cont, end=' ')
    print(termosInicio)
    mais = int(input('Quantos termos a mais você quer adicionar?\nDigite 0 para SAIR'))
print('Saindo...')










    # userInput = input('[1] para alterar a quantidade de termos\n[2] para novos valores\n[5]SAIR')

