nome = input('Digite seu nome: ')
primeira_nota = float(input('Digite a sua primeira nota: '))
segunda_nota = float(input('Digite a sua segunda nota: '))

media = (primeira_nota + segunda_nota) / 2
if media >= 6:
    print("aprovado!")
else:
    print('reprovado!')