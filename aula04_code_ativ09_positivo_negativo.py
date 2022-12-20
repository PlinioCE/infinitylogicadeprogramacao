print('-=' * 15)
print('POSITIVO ou NEGATIVO - Atividade 09')
print('-=' * 15)

numero = int(input('Digite um número: '))

if numero > 0:
    print(f'\nO número {numero} é POSITIVO!')
elif numero < 0:
    print(f'\nO número {numero} é NEGATIVO!')
else:
    print(f'\nO número {numero} é NULO!')
