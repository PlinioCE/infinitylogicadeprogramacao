print('-=' * 15)
print('VERIFICA VELOCIDADE - Atividade 05')
print('-=' * 15)

velocidadeVia = int(input('Informe a velocidade da via(Km/h): '))
velocidadeVeiculo = int(input('Informe a velocidade do veículo(Km/h): '))

if velocidadeVeiculo <= velocidadeVia:
    velocidade = 'com VELOCIDADE PERMITIDA'
elif velocidadeVeiculo > velocidadeVia and velocidadeVeiculo < velocidadeVia + 20:
    velocidade = 'com ALTA VELOCIDADE'
elif velocidadeVeiculo >= velocidadeVia + 20 and velocidadeVeiculo <= velocidadeVia + 60:
    velocidade = 'MUITO RÁPIDO'
else:
    velocidade = 'VUADO'
print(f'\nA velocidade de {velocidadeVeiculo}Km/h indica que você está {velocidade}!')
