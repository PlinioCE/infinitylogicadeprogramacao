print('-=' * 15)
print('INPECORONA - Atividade 04')
print('-=' * 15)

somaAssintomaticos = somaSintomasLeves = somaSintomasGraves = contagem = 0
porcentagemAssintomaticos = porcentagemLeves = porcentagemGraves = 0

print('\nSINTOMAS CONHECIDOS'
      '\n[ 1 ] - Assintomático'
      '\n[ 2 ] - Sintomas Leves'
      '\n[ 3 ] - Sintomas Graves')
for contagem in range(0, 10):
    contagem += 1
    sintoma = int(input(f'\nQuais os sintomas do {contagem}º paciente? '))
    if sintoma == 1:
        somaAssintomaticos += 1
        porcentagemAssintomaticos = (somaAssintomaticos * 100) / 10
    elif sintoma == 2:
        somaSintomasLeves += 1
        porcentagemLeves = (somaSintomasLeves * 100) / 10
    elif sintoma == 3:
        somaSintomasGraves += 1
        porcentagemGraves = (somaSintomasGraves * 100) / 10
    else:
        print('SINTOMA NÃO CADASTRADO!')
print()
print(f'========== RESULTADO =========='
      f'\nPACIENTES ASSINTOMÁTICOS : {porcentagemAssintomaticos}%'
      f'\nPACIENTES COM SINTOMAS LEVES: {porcentagemLeves}%'
      f'\nPACIENTES COM SINTOMAS GRAVES: {porcentagemGraves}%')
