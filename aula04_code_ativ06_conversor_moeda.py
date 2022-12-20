print('-=' * 15)
print('CONVERSOR DE MOEDA - Atividade 06')
print('-=' * 15)

valorReal = float(input('Digite o valor: R$ '))
taxaCambio = float(input('Qual o valor do dólar? R$ '))
valorDolar = valorReal / taxaCambio

print(f'\nR$ {valorReal:.2f} = US$ {valorDolar:.2f}')
