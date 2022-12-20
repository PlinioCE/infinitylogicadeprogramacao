print('-=' * 15)
print('NÚMERO SECRETO - Atividade 07')
print('-=' * 15)

numeroSecreto = 173

numero = int(input('Digite uma palpite do número secreto: '))

if numero > numeroSecreto:
    print(f'O número {numero} é MAIOR que o número secreto!')
elif numero < numeroSecreto:
    print(f'O número {numero} é MENOR que o número secreto!')
else:
    print(f'PARABÉNS!!! O número secreto era {numeroSecreto}.')
