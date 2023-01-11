jogador = {'Nome do Jogador': '',
           'Número de Partidas': '',
           'Gols': [],
           'Total de Gols': ''}
gols = []
jogador['Nome do Jogador'] = str(input('Nome do Jogador: ')).title()
jogador['Número de Partidas'] = int(input(f'Quantas partidas {jogador["Nome do Jogador"]} jogou? '))
cont = 1
soma = 0
cont2 = 0
for n in range(jogador['Número de Partidas']):
    jogador['Gols'] = int(input(f'Quantos gols na partida {cont}? '))
    cont += 1
    soma = soma + jogador['Gols']
    gols.append(jogador['Gols'])

jogador['Gols'] = gols
jogador['Total de Gols'] = soma

print(jogador)
print('=-' * 30)
print(f'O jogador {jogador["Nome do Jogador"]} jogou {jogador["Número de Partidas"]} partidas.')

for p in range(jogador['Número de Partidas']):
    print(f'Na partida {cont2 + 1}, fez {jogador["Gols"][cont2]} gol(s)')
    cont2 += 1
print(f'Foi um total de {soma} gols.')