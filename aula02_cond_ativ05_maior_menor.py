print('-=' * 15)
print('MAIOR e MENOR - Atividade 05')
print('-=' * 15)

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))

if numero1 != numero2 and numero1 != numero3 and numero2 != numero3:
    if numero1 > numero2 and numero1 > numero3:
        maior = numero1
    elif numero2 > numero1 and numero2 > numero3:
        maior = numero2
    else:
        maior = numero3

    if numero1 < numero2 and numero1 < numero3:
        menor = numero1
    elif numero2 < numero1 and numero2 < numero3:
        menor = numero2
    else:
        menor = numero3
    print(f'\nO maior número é {maior} e o menor é {menor}.')

elif numero1 == numero2 and numero1 != numero3 and numero2 != numero3:
    if numero1 > numero3:
        maior = numero1
        menor = numero3
    else:
        maior = numero3
        menor = numero1
    print(f'\nO maior número é {maior} e o menor é {menor} e o primeiro número é igual ao segundo.')
elif numero1 != numero2 and numero1 == numero3 and numero2 != numero3:
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1
    print(f'\nO maior número é {maior} e o menor é {menor} e o primeiro número é igual ao terceiro.')
elif numero1 != numero2 and numero1 != numero3 and numero2 == numero3:
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1
    print(f'\nO maior número é {maior} e o menor é {menor} e o segundo número é igual ao terceiro.')
else:
    print(f'\nTodos os números são iguais.')
