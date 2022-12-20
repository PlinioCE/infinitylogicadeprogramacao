from random import randint

print('-=' * 15)
print('JO-KEN-PO - Desafio 03')
print('-=' * 15)

print('LEGENDA:'
      '\nPEDRA [PD]'
      '\nPAPEL [PP]'
      '\nTESOURA [TS]\n')
jogador = str(input('Faça sua jogada: ')).upper()

pedra = jogador.count('PD')
papel = jogador.count('PP') + 1
tesoura = jogador.count('TS') + 2
pc = randint(1, 3)

if pc == 1:
      jogadaPc = 'PEDRA'
elif pc == 2:
      jogadaPc = 'PAPEL'
else:
      jogadaPc = 'TESOURA'

if (jogador == 'PD' and jogadaPc == 'TESOURA') or (jogador == 'PP' and jogadaPc == 'PEDRA') or (jogador == 'TS' and jogadaPc == 'PAPEL'):
      print(f'\nVocê VENCEU! O Computador jogou {jogadaPc}.')
elif (jogador == 'PD' and jogadaPc == 'PEDRA') or (jogador == 'PP' and jogadaPc == 'PAPEL') or (jogador == 'TS' and jogadaPc == 'TESOURA'):
      print(f'EMPATE! O Computador também jogou {jogadaPc}.')
else:
    print(f"\nVocê PERDEU! O Computador jogou {jogadaPc}.")
