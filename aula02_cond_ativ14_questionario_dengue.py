print('-=' * 15)
print('CONSULTA REMOTA - Atividade 14')
print('-=' * 15)

febre = str(input('FEBRE ALTA? [S/N]: ')).lower()
dorCabeca = str(input('DOR DE CABEÇA? [S/N]: ')).lower()
dorMuscular = str(input('DOR NO CORPO? [S/N]: ')).lower()
manchas = str(input('MANCHAS AVERMELHADAS? [S/N]: ')).lower()
sintoma = (febre, dorCabeca, dorMuscular, manchas).count('s')

if sintoma >= 3:
    print('\nSuspeita de dengue, procure um médico!')
else:
    print('\nPermaneça em repouso e observe a evolução dos sintomas.')
