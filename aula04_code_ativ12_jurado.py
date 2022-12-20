print('-=' * 15)
print('JURADO - Atividade 12')
print('-=' * 15)

nota = float(input('Informe sua nota(0 - 10): '))

while nota > 10:
    print('VALOR INVÁLIDO!')
    nota = float(input('\nInforme sua nota(0 - 10): '))
print(f'\nNOTA = {nota}')
