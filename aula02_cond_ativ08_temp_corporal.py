print('-=' * 15)
print('TERMÔMETRO - Atividade 08')
print('-=' * 15)

temperatura = float(input('Informe a temperatura aferida(ºC): '))

if temperatura <= 37:
    situacao = 'NORMAL'
elif temperatura > 37 and temperatura <= 37.8:
    situacao = 'FEBRIL'
elif temperatura > 37.8 and temperatura <= 38.5:
    situacao = 'FEBRE LEVE'
elif temperatura > 38.5 and temperatura <=39.4:
    situacao = 'FEBRE MODERADA'
else:
    situacao = 'FEBRE GRAVE'
print(f'\nTemperatura: {temperatura}ºC'
      f'\nClassificação: {situacao}')
