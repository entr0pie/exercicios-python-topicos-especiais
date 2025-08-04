

def calcular_tabuada(numero: float, limite: int):
    for i in range(1, limite + 1):
        print(f'{numero} * {i} = {numero * i}')


print('Bem vindo à tabuada personalizada!')
numero = float(input('? Digite o numero para calcular: ')) 
limite = int(input('? Digite a quantidade de vezes para calcular: '))

calcular_tabuada(numero, limite)