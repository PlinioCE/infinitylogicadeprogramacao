print('-=' * 20)
print('Par ou Ímpar - Questão 01')
print('-=' * 20)

numero = int(input('Digite um número: '))
print()

if numero > 0:
    if numero % 2 == 0:
        print(f'O número \'{numero}\' é POSITIVO e PAR!')
    else:
        print(f'O número \'{numero}\' é POSITIVO e ÍMPAR!')
elif numero < 0:
    if numero % 2 == 0:
        print(f'O número \'{numero}\' é NEGATIVO e PAR!')
    else:
        print(f'O número \'{numero}\' é NEGATIVO e ÍMPAR!')
else:
    print(f'O número \'{numero}\' é NULO!')
