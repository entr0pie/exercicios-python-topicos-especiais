qtd_alunos = int(input('? Digite a quantidade de alunos para calcular a média: '))

total_notas = 0
menor_nota = 100
maior_nota = 0

for i in range(0, qtd_alunos):
    nota = float(input(f'? Digite a nota do aluno {i + 1} (entre 0 até 100): '))
    
    total_notas += nota

    if (nota < menor_nota):
        menor_nota = nota

    if (nota > maior_nota):
        maior_nota = nota

print('A média é: ', total_notas / qtd_alunos)
print('A menor nota é: ', menor_nota)
print('A maior nota é: ', maior_nota)
