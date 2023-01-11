valores = []
for c in range(1, 6):
    valor = int(input(f'Digite o {c}º valor: '))
    if c == 1:
        valores.append(valor)
    elif valor > valores[len(valores)-1]:
        


print(valores)
