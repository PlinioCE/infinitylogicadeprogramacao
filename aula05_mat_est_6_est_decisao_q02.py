print('-=' * 20)
print('Cálculos 2 número - Questão 02')
print('-=' * 20)

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
print()

soma = numero1 + numero2
produto = numero1 * numero2

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(f'SOMA: {numero1} + {numero2} = {soma}')
elif numero1 % 2 == 1 and numero2 % 2 == 1:
    print(f'PRODUTO: {numero1} x {numero2} = {produto}')
else:
    if numero1 > numero2:
        diferenca = numero1 - numero2
        print(f'SUBTRAÇÃO: {numero1} - {numero2} = {diferenca}')
    else:
        diferenca = numero2 - numero1
        print(f'SUBTRAÇÃO: {numero2} - {numero1} = {diferenca}')
