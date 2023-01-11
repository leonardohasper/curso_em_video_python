import time
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
ordem = sorted(times)
libertadores = times[0:5]
rebaixamento = times[-4:20]

print('Analisando a tabela do Brasileirão...')
time.sleep(2)
print(f'Os times em ordem alfabética são: {ordem}')
time.sleep(3)
print(f'Os times no G5 que foram para a libertadores são:{libertadores}')
time.sleep(3)
print(f'Os times rebaixados foram: {rebaixamento}')
time.sleep(3)
print(f'O Coritiba ficou na {times.index("Coritiba") + 1}ª posição')













