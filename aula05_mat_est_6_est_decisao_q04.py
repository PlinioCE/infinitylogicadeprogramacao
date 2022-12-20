print('-=' * 20)
print('Divisível por 6 - Questão 04')
print('-=' * 20)

numero = int(input('Digite um número: '))

if numero % 2 == 0 and numero % 3 == 0:
    print(f'{numero} : 6 = {numero / 6:.0f}')
else:
    print(f'O número {numero} NÃO é divisível por 6.')
