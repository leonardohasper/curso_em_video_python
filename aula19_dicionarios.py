#pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())          #mostra as chaves(keys), ou seja, 'nome', 'sexo' e 'idade'
#print(pessoas.values())          #mostra os valores(values), ou seja, 'Gustavo', 'M' e 22
#print(pessoas.items())            #mostra as keys e os values. Cria uma lista com tuplas dentro
#del pessoas['sexo']              #apaga a key e o valor
#pessoas['nome'] = 'Leonardo'      #altera o valor da key 'nome'

#for k, v in pessoas.items():
    #print(f'{k} = {v}')

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'RJ'}

brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil[0]['uf'])'''

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')






