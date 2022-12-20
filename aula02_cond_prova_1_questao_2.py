faixa_1 = faixa_2 = faixa_3 = faixa_4 = faixa_5 = 0
for p in range(1, 16):
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    if 0 < idade <= 15:
        faixa_1 += 1
    elif 15 < idade <= 30:
        faixa_2 += 1
    elif 30 < idade <= 45:
        faixa_3 += 1
    elif 45 < idade <= 60:
        faixa_4 += 1
    else:
        faixa_5 += 1
porc_faixa_1 = faixa_1 * 100 / 15
porc_faixa_5 = faixa_5 * 100 / 15
print(f'\nPessoas entre 0 e 15 anos: {faixa_1}'
      f'\nPessoas entre 16 e 30 anos: {faixa_2}'
      f'\nPessoas entre 31 e 45 anos: {faixa_3}'
      f'\nPessoas entre 46 e 60 anos: {faixa_4}'
      f'\nPessoas maiores que 60 anos: {faixa_5}')
print(f'\nPessoas entre 0 e 15 anos correspondem a {porc_faixa_1:.2f}%.'
      f'\nPessoas maiores que 60 anos correspondem a {porc_faixa_5:.2f}%.')
