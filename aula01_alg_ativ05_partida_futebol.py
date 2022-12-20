print('-=' * 15)
print('PLACAR - Atividade 05')
print('-=' * 15)

mandante = str(input('TIME MANDANTE: '))
visitante = str(input('TIME VISITANTE: '))
golMandante = int(input(f'GOLS {mandante}: '))
golVisitante = int(input(f'GOLS {visitante}: '))
print('-=' * 15)

if golMandante > golVisitante:
    print(f'PLACAR FINAL'
          f'\n{mandante} {golMandante} x {golVisitante} {visitante}'
          f'\n{mandante} VENCEU!')
elif golVisitante > golMandante:
    print(f'PLACAR FINAL'
          f'\n{mandante} {golMandante} x {golVisitante} {visitante}'
          f'\n{visitante} VENCEU!')
else:
    print(f'PLACAR FINAL'
          f'\nEMPATE em {golMandante} x {golVisitante}')
