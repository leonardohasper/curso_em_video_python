lista = list()
a = b = condicao_c = pos = 0
produto = True
while True:
    while produto == True:
        if pos == 1:
            condicao_c = preco
            c = item

        item = str(input('Nome do produto: ')).strip().title()
        preco = float(input('Valor: R$'))

        certo = str(input('está correto?[S / N]: ')).strip().upper()

        if certo in 'SN':
            if certo == 'N':
                print('correção')

            elif certo == 'S':
                # lista.append(item)
                # pos += 1
                a += preco
                continuar = str(input('continuar cadastro? ')).strip().upper()
                if preco > 1000:
                    b += 1
                if preco < condicao_c:
                    c = item
                if continuar in 'SN':
                    if continuar in 'S':
                        produto = True
                    elif continuar in 'N':
                        produto = False
                        break

    # print(a, b, c, condicao_c, produto, certo, pos, continuar)
    # print(lista)
    print(f'o total gasto na compra R${a:.2f}')
    print(f'{b} custam mais de R$1000')
    print(f'o produto mais barato é {c}')

    break