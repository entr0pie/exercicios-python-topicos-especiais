peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obeso')