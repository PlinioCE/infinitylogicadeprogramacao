print('-=' * 15)
print('VERIFICAR TEMPERATURA - Atividade 02')
print('-=' * 15)

temperaturaOk = False
temperatura = float(input('Informe sua temperatura em ºC: '))

if temperatura <= 37:
    temperaturaOk = True
else:
    temperaturaOk = False

if temperaturaOk:
    print(f'\nTEMPERATURA OK! ACESSO LIBERADO.')
else:
    print(f'\nTEMPERATURA ACIMA DO PERMITIDO! ACESSO NEGADO.')
