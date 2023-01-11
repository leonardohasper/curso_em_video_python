#reajuste salarial

salario = float(input('Qual o salário do funcionário? '))
porCento = int(input('Qual a porcentagem de aumento? '))
aumento = (porCento / 100) * salario
print('Com um aumento de {}% o salário passa a ser de {} reais'.format(porCento, aumento + salario))

