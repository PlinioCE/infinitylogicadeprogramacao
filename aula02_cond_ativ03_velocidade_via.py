print('-=' * 19)
print('CONTROLE DE VELOCIDADE - Atividade 03')
print('-=' * 19)

velocidadeVia = int(input('Informe a velocidade da via(Km/h): '))
velocidadeVeiculo = int(input('Informe a velocidade do veículo(Km/h): '))

if velocidadeVeiculo > velocidadeVia:
    print(f'\nSua velocidade está acima do permitido ({velocidadeVia}Km/h).')
else:
    print(f'\nSua velocidade está compatível com a da via({velocidadeVia}Km/h).')
