print('-=' * 20)
print('Boletim - Questão 10')
print('-=' * 20)
while True:
    nome = str(input('Informe o nome do aluno: ')).strip().upper()
    av1 = float(input('Informe a nota AV1: '))
    while av1 not in range(0, 11):
        print('Nota AV1 inválida!')
        av1 = float(input('\nInforme a nota AV1: '))
    av2 = float(input('Informe a nota AV2: '))
    while av2 not in range(0, 11):
        print('Nota AV2 inválida!')
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
    saida = ' '
    while saida not in 'SN':
        saida = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
        print()
    if saida == 'N':
        print('*** FINALIZANDO SISTEMA ***')
        break
