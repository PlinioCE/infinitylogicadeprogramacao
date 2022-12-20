print('-=' * 15)
print('MAIOR NÚMERO - Atividade 08')
print('-=' * 15)

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))

if numero1 > numero2:
    maiorNumero = numero1
elif numero1 < numero2:
    maiorNumero = numero2
else:
    print(f'{numero1} = {numero2}')
print(f'\nO maior número é {maiorNumero}.')
