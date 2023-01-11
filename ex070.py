total = maisMil = prodBarato = cont = 0
while True:
    nomeProduto = str(input('Digite o nome do produto: ').title())
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    total = total + preco

    if preco > 1000:
        maisMil += 1

    if cont == 1:
        prodBarato = preco
    else:
        if preco < prodBarato:
            prodBarato = preco
            nomeBarato = nomeProduto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]').upper().strip())

    if continuar == 'N':
        break

print(f'O total da compra foi {total} reais')
print(f'{maisMil} produto(s) custando acima de 1000 reais')
print(f'O produto mais barato foi {nomeBarato} e custou {prodBarato} reais')
