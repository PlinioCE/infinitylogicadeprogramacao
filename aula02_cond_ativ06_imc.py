print('-=' * 15)
print('VERIFICA IMC - Atividade 06')
print('-=' * 15)

peso = float(input('Informe seu peso(Kg): '))
altura = float(input('Informe sua altura(m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = 'ABAIXO DO PESO'
elif imc >= 18.5 and imc < 25:
    classificacao = 'PESO NORMAL'
elif imc >= 25 and imc < 30:
    classificacao = 'SOBREPESO'
elif imc >= 30 and imc < 40:
    classificacao = 'OBESIDADE GRAU I'
else:
    classificacao = 'ALERTA: OBESIDADE MÓRBIDA'
print(f'\nSeu IMC = {imc:.1f}'
      f'\nClassificação: {classificacao}.')
