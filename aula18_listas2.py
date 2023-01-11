'''pessoas = [['Pedro, 25'], ['Maria, 19'], ['João, 32']]
print(pessoas[1])
#===========================================================
teste = list()
teste.append('Leonardo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#===========================================================
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
#==========================================================='''
galera = []
dado = []
totMenor = 0
totMaior = 0
while True:
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    dado.append(nome)
    dado.append(idade)
    galera.append(dado[:])
    dado.clear()
    continuar = input('Continuar? [S/N]').upper()
    if continuar in 'N':
        break
for p in galera:
    if p[1] >= 18:
        totMaior += 1
        print(f'Você é velho, {p[0]}')
    else:
        totMenor += 1
        print(f'Você é jovem, {p[0]}')

print(f'{totMaior} maiores de 18')
print(f'{totMenor} menores de 18')


