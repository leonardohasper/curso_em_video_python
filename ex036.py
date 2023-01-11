print('====================EMPRÉSTIMO BANCÁRIO====================')
valorCasa = int(input('Valor da casa: '))
salario = int(input('Salário do comprador: '))
anos = int(input('Quantos anos para pagar: '))

meses = anos * 12
prestacao = valorCasa / meses

if prestacao <= salario * 0.3:
    print('Empréstimo concedido!\nPrestação de {:.2f} reais durante {} meses.'.format(prestacao, meses))
elif prestacao > salario * 0.3:
    print('Empréstimo negado!\nPrestação de {:.2f} reais excede 30% do salário do comprador!'.format(prestacao))

#print('Valor da casa: {} reais\nSalário do comprador: {} reais\nTempo de pagamento: {} meses'.format(valorCasa, salario, meses))
