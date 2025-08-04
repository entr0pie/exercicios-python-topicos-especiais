
def calcular_partes_da_divisao(numerador: float, denominador: float):
    parte_inteira = numerador // denominador
    parte_fracionaria = numerador % denominador

    return [parte_inteira, parte_fracionaria]

def calcular_qtd_notas(valor: float) -> float:
    notas_cem, restante  = calcular_partes_da_divisao(valor, 100)
    notas_cinquenta, restante = calcular_partes_da_divisao(restante, 50)
    notas_vinte, restante = calcular_partes_da_divisao(restante, 20)
    notas_dez, restante = calcular_partes_da_divisao(restante, 10)

    return {
        '100': notas_cem,
        '50': notas_cinquenta,
        '20': notas_vinte,
        '10': notas_dez
    }

print('Bem vindo ao caixa automático!')
valor = float(input('? Digite o valor que deseja retirar: '))

qtd_notas = calcular_qtd_notas(valor)

print('Notas de 100: ', qtd_notas['100'])
print('Notas de 50: ', qtd_notas['50'])
print('Notas de 20: ', qtd_notas['20'])
print('Notas de 10: ', qtd_notas['10'])