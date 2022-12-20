from random import randrange

print('-=' * 15)
print('SORTEIO NÚMERO - Atividade 01')
print('-=' * 15)

numero = 0
sorteio = randrange(1, 10)
while numero != sorteio:
    numero = int(input('\nDigite um número: '))
    if numero > sorteio:
        print(f'O número {numero} é MAIOR que o sorteado!')
    elif numero < sorteio:
        print(f'O número {numero} é MENOR que o sorteado!')
    else:
        print(f'O número {numero} é IGUAL ao sorteado, {sorteio}.')
print('\nFim')
