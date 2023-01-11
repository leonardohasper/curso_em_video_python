#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Valor do salário: '))

if salario > 1250:
    reajuste1 = salario * 1.1
    print('O novo valor é de: {:.2f} reais'.format(reajuste1))

if salario <= 1250:
    reajuste2 = salario * 1.15
    print('O novo valor é de: {:.2f} reais'.format(reajuste2))