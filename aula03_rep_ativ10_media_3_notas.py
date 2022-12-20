print('-=' * 15)
print('MÉDIA 3 NOTAS - Atividade 10')
print('-=' * 15)

somaNota = mediaNota = 0
for contagem in range(1, 4):
    nota = float(input(f'Digite a {contagem}ª nota: '))
    somaNota += nota
mediaNota = somaNota / 3
print(f'\nMÉDIA: {mediaNota:.1f}')
