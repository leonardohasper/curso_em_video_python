peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt*2)
print('{:.2f}'.format(imc))

if imc <= 18.5:
    print('Abaixo do peso')
elif 18.6 <= imc <= 25:
    print('Normal')
elif 25.1 <= imc <= 30:
    print('Sobrepeso')
elif 30.1 <= imc <= 40:
    print('Obesidade')
elif imc >= 41:
    print('Obesidade mórbida')
else:
    print('OPÇÃO INVÁLIDA')
