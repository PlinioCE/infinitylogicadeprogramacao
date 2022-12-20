print('-=' * 15)
print('INFINITY CAR - Atividade 06')
print('-=' * 15)

custoCarro = float(input('Informe o valor do custo de fabricação: R$ '))
distribuidor = custoCarro * 0.28
imposto = custoCarro * 0.45
valorCarro = custoCarro + distribuidor + imposto

print('\nValor de revenda do veículo: R$ {:.2f}'.format(valorCarro))
