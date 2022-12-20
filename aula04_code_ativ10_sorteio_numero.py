from random import randrint

print('-=' * 15)
print('SORTEIO NÚMERO - Atividade 10')
print('-=' * 15)

numeroPc = randint(1, 10)
numeroJogador = 0

while numeroJogador != numeroPc:
    numeroJogador = int(input('Digite um número de 1 a 10: '))
    if numeroJogador != numeroPc:
        print('ERROU! Tente outra vez...')
        print()
print(f'ACERTOU! O número sorteado foi {numeroPc}. PARABÉNS!!! ')
