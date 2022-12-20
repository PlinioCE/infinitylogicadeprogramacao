print('-=' * 15)
print('POSITIVO ou NEGATIVO - Atividade 04')
print('-=' * 15)

numero = int(input('Digite um número: '))

if numero >= 0:
    resultado = 'POSITIVO'
else:
    resultado = 'NEGATIVO'
print(f'O número {numero} é {resultado}!')
