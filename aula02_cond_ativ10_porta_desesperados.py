from random import randint

print('-=' * 15)
print('PORTA DOS DESESPERADOS - Atividade 10')
print('-=' * 15)

escolhaPorta = int(input('ESCOLHA UMA PORTA'
                         '\n[1] [2] [3] [4]: '))
premio = randint(1, 4)

if escolhaPorta == premio:
    print('PARABÉNS! Você ganhou o super prêmio: Uma BICICLETA CALOI zerada!')
else:
    print('Não foi desta vez!')
