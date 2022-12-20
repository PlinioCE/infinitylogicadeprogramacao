print('-=' * 15)
print('CONTAGEM REGRESSIVA - Atividade 08')
print('-=' * 15)

numero = int(input('Informe o início da contagem regressiva: '))
for contagem in range(numero, -1, -1):
    print(contagem, end=' ')
print()
