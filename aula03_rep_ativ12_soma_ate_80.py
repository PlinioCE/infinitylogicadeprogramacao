print('-=' * 15)
print('SOMA ÍMPARES e PARES até 80 - Atividade 12')
print('-=' * 15)

numero = int(input('Digite até o número deseja somar: '))
somaPar = somaImpar = 0

for contagem in range(0, numero + 1):
    if contagem % 2 == 0 and contagem <= 80:
        somaPar += contagem
    else:
        somaImpar += contagem
print(f'\nSOMA PARES até 80: {somaPar}'
      f'\nSOMA ÍMPARES: {somaImpar}')
