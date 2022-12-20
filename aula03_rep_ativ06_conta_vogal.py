print('-=' * 15)
print('CONTA VOGAL - Atividade 06')
print('-=' * 15)

somaVogal = 0
frase = str(input('Digite uma frase para contagem de vogais: ')).upper()
for vogal in frase:
    if vogal == 'A' or vogal == 'E' or vogal == 'I' or vogal == 'O' or vogal == 'U':
        somaVogal += 1
if somaVogal > 1:
    print(f'\nExistem {somaVogal} vogais na frase.')
else:
    print(f'\nExite {somaVogal} vogal na frase.')
