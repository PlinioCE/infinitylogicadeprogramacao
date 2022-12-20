print('-=' * 15)
print('INFINITY BUS - Atividade 06')
print('-=' * 15)

origem = str(input('Informe a cidade de origem: '))
destino = str(input('Informe a cidade de destino: '))
distancia = float(input('Informe a distância aproximada em quilômetros: '))

if distancia > 250:
    preco = distancia * 0.65
else:
    preco = distancia * 0.85
print('\nTICKET VIAGEM')
print('-=' * 15)
print(f'ORIGEM: {origem}'
      f'\nDESTINO: {destino}'
      f'\nVALOR: R$ {preco:.2f}')
print('|| || ||| | ||| |||| || ||| |')
print('²¹³² ³³¹² ²¹³¹ ²²¹² ²²¹³ ²³²¹')
print('-=' * 15)
