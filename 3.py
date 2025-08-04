primeiro_num = float(input('Digite o primeiro número: '))
segundo_num = float(input('Digite o segundo número: '))

print('Soma: ', primeiro_num + segundo_num)
print('Subtração: ', primeiro_num - segundo_num)
print('Multiplicação: ', primeiro_num * segundo_num)

if segundo_num == 0:
    print('Divisão: não é possível dividir um número por zero.')
else:
    print('Divisão: ', primeiro_num / segundo_num)