print('-=' * 15)
print('INFINITY SCHOOL - Atividade 11')
print('-=' * 15)

nome = str(input('Informe o nome do aluno(a): '))
nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informa a 2ª nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    situacao = 'APROVADO com conceito A'
elif media >= 5 and media < 7:
    situacao = 'APROVADO com conceito B'
elif media >= 4 and media < 5:
    situacao = 'Necessário AVALIÇÃO FINAL'
else:
    situacao = 'REPROVADO'
print(f'\nALUNO(A): {nome}'
      f'\nMÉDIA: {media}'
      f'\nSITUAÇÃO: {situacao}!')
