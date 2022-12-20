aula = int(input('Informe o número de aulas comparecidas: '))
if aula >= 40:
    av_1 = float(input('Informe a nota da AV1: '))
    av_2 = float(input('Informe a nota da AV2: '))
    av_3 = float(input('Informe a nota da AV3: '))
    media = (av_1 + av_2 + av_3) / 3
    if media >= 6:
        print(f'\nMédia: {media:.2f} - APROVADO!')
    else:
        print(f'\nMédia: {media:.2f} - REPROVADO!')
else:
    print('\nAluno REPROVADO por faltas.')
