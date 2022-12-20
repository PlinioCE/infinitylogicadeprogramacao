from random import randint

print('-=' * 15)
print('ACERTA NÚMERO - Atividade 14')
print('-=' * 15)

jogadaPc = randint(1, 10)
jogador = 0
while jogador != jogadaPc:
    jogador = int(input('Escolha um número de 1 a 10: '))
print('\nACERTOU!!!')
