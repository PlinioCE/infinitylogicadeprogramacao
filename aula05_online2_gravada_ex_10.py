voto_branco = candidato_a = candidato_b = candidato_c = 0
eleitor = 10

for i in range(0, eleitor):
    print('*** PESQUISA ELEITORAL 2022 ***')
    print('-------------------------------')
    print('[1] - Candidato A'
          '\n[2] - Candidato B'
          '\n[3] - Candidato C'
          '\n[4] - Branco/Nulo')
    voto = int(input('Qual sua intenção de voto? '))
    print()
    if voto == 1:
        candidato_a += 1
    elif voto == 2:
        candidato_b += 1
    elif voto == 3:
        candidato_c += 1
    else:
        voto_branco += 1
print('*** RESULTADO DA PESQUISA ***')
print('-----------------------------')
print(f'Candidato A: {candidato_a * 100 / eleitor:.2f}% dos votos.')
print(f'Candidato B: {candidato_b * 100 / eleitor:.2f}% dos votos.')
print(f'Candidato C: {candidato_c * 100 / eleitor:.2f}% dos votos.')
print(f'Brancos/Nulos: {voto_branco * 100 / eleitor:.2f}% dos votos.')
