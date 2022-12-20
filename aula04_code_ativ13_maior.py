print('-=' * 15)
print('MAIOR NÚMERO - Atividade 13')
print('-=' * 15)

maiorNumero = 0

for contador in range(1, 6):
    numero = int(input(f'Digite o {contador}º número: '))
    if numero > maiorNumero:
        maiorNumero = numero
print(f'\nO maior número é {maiorNumero}.')
