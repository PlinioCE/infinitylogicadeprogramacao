print('-=' * 15)
print('PLACAR PARTIDA - Atividade 09')
print('-=' * 15)

mandante = str(input('MANDANTE: '))
visitante = str(input('VISITANTE: '))
golsMandante = int(input('GOLS MANDANTE: '))
golsVisitante = int(input('GOLS VISITANTE: '))

if golsMandante > golsVisitante:
    resultado = (f'{mandante} venceu!'
                 f'\n{visitante} perdeu!')
elif golsMandante < golsVisitante:
    resultado = (f'{visitante} venceu!'
                 f'\n{mandante} perdeu!')
else:
    resultado = 'Empate!!!'
print(f'\nFIM DE JOGO'
      f'\n{mandante} {golsMandante} x {golsVisitante} {visitante}'
      f'\n{resultado}')
