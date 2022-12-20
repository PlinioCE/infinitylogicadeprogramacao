print('-=' * 20)
print('Boletim - Questão 05')
print('-=' * 20)

nome = str(input('Informe o nome do aluno: ')).strip().upper()
av1 = float(input('Informe a nota AV1: '))
av2 = float(input('Informe a nota AV2: '))
media = (av1 + av2) / 2
print()
if media >= 7:
    situacao = 'APROVADO(A) COM CONCEITO A.'
elif 5 <= media < 7:
    situacao = 'APROVADO(A) COM CONCEITO B.'
elif 4 <= media < 5:
    situacao = 'NECESSÁRIA REALIZAÇÃO DA AV3.'
else:
    situacao = 'REPROVADO(A).'
print(f'{nome}, {situacao}')
