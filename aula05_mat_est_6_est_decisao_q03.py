print('-=' * 20)
print('Estastísticas População - Questão 03')
print('-=' * 20)

soma_idade = 0
for c in range(1, 6):
    idade = int(input(f'Informe a {c}ª idade: '))
    soma_idade += idade
media = soma_idade / c
print()
if media < 25:
    print(f'POPULAÇÃO JOVEM: Média = {media:.1f}')
elif 25 <= media < 65:
    print(f'POPULAÇÃO ADULTA: Média = {media:.1f}')
else:
    print(f'POPULAÇÃO IDOSA: Média = {media:.1f}')
