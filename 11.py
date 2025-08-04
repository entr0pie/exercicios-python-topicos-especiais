nota = float(input('? Digite a nota do aluno (entre 0 e 10): '))
frequencia = float(input('? Digite a frequência do aluno (porcentagem, entre 0 e 100): '))

if nota >= 0.6 and frequencia >= 75:
    print('Aprovado!')
else:
    print('Reprovado!')

"""
Foi necessário usar o operador AND porque as duas condições precisam ser verdadeiras 
(tanto a nota quanto a frequência).

Caso se use OR, o aluno será aprovado com nota acima de 0.6 OU frequência acima de 75% (
que não pode acontecer). 
"""