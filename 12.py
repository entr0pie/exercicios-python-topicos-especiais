primeiro_valor = float(input('> Digite o primeiro valor: '))
segundo_valor = float(input('> Digite o segundo valor: '))

print('A média é: ', (primeiro_valor + segundo_valor) / 2)

"""
Precisamos usar a função float, pois a função input sempre 
retornará texto (string). Caso queiramos fazer operações
matemáticas, temos que converter para valores decimais.

Quando a soma é feita entre duas strings, acontece a con-
catenação delas (colocar uma após a outra).

Ex:

abra + cadabra = abracadabra
2 + 3 = 23
"""