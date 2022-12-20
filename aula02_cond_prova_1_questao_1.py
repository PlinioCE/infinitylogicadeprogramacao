sexo = conta_homens = conta_mulheres = 0
habitantes = int(input('Quantos habitantes há na cidade? '))
for p in range(1, habitantes+1):
    sexo = int(input('Qual o sexo? [1-M / 2-F]: '))
    if sexo == 1:
        conta_homens += 1
    elif sexo == 2:
        conta_mulheres += 1
print()
print('-' * 17)
print('IBGE - Censo 2019')
print('-' * 17)
print(f'Pessoas do sexo MASCULINO: {conta_homens}')
print(f'Pessoas do sexo FEMININO: {conta_mulheres}')
