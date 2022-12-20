print('-=' * 15)
print('INÍCIO, FIM e RAZÃO - Atividade 09')
print('-=' * 15)

numeroInicio = int(input('Digite o primeiro número: '))
numeroFim = int(input('Digite o último número: '))
razao = int(input('Digite a razão: '))

for contagem in range(numeroInicio, numeroFim + 1, razao):
    print(contagem, end=' ')
print()
