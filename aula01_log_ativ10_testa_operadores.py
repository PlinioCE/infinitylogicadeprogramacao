print('-=' * 20)
print('TESTA OPERADORES ARITMÉTICOS - Atividade 10')
print('-=' * 20)

numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))

adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
media = adicao / 2

print(f'ADIÇÃO: {numero1} + {numero2} = {adicao}'
      f'\nSUBTRAÇÃO: {numero1} - {numero2} = {subtracao}'
      f'\nMULTIPLICAÇÃO: {numero1} x {numero2} = {multiplicacao}'
      f'\nDIVISÃO: {numero1} : {numero2} = {divisao}'
      f'\nMÉDIA: ({numero1} + {numero2}) / 2 = {media}')
