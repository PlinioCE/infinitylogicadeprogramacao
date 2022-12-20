print('-=' * 15)
print('TABUADA - Atividade 15')
print('-=' * 15)

tabuada = int(input('Defina a a tabuada: '))
print(f'\nTABUADA DE {tabuada}')
print('-------------')

for contagem in range(1, 11):
    resultado = tabuada * contagem
    print(f'{tabuada} x {contagem:2} = {resultado}')
