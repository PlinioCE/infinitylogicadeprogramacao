
'''soma = media = contador = 0
print('-=' * 10)
print('PROVA [LP-A03]')
print('-=' * 10)
numeroParada = int(input('Defina um código numérico para finalizar: '))
numero = int(input(f'Digite um número (Digite {numeroParada} para finalizar): '))
while numero != numeroParada:
    contador += 1
    soma += numero
    numero = int(input(f'Digite um número (Digite {numeroParada} para finalizar): '))
media = soma / contador
print(f'\nRESULTADO:'
      f'\nSOMA = {soma}'
      f'\nMÉDIA = {media:.2f}')'''

numero = soma = media = contador = 0
saida = ''

while saida in 'SIMsim':
    contador += 1
    numero = int(input(f'Digite um número: '))
    soma += numero
    saida = str(input('Deseja continuar? [S/N]: '))
    print()
media = soma / contador
print(f'\nRESULTADO:'
      f'\nSOMA = {soma}'
      f'\nMÉDIA = {media:.1f}')
