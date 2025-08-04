
produtos = {}
total = 0

for i in range(1, 4):
    nome = input(f'{i} > Digite o nome do produto: ')
    valor = float(input(f'{i} > Digite o valor do produto: '))

    total += valor
    produtos[nome] = valor

valor_final = total if total <= 100 else total * 0.9

print('Valor final da compra: ', valor_final)

print('Itens: ')

for key, value in produtos.items():
    print(f"{key}: R${value}")