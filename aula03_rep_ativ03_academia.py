print('-=' * 15)
print('MÉDIA ACADEMIA - Atividade 03')
print('-=' * 15)

soma = media = contagem = 0
decisao = 'N'

while decisao not in 'Ss':
    nota = float(input('Informe a nota: '))
    contagem += 1
    soma += nota
    decisao = str(input('Deseja finalizar? [S/N] '))
media = soma / contagem
print(f'\nMÉDIA: {media:.1f}')
