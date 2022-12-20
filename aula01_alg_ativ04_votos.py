print('-=' * 25)
print('TSE - Calcula % VOTOS - Atividade 04')
print('-=' * 25)

municipio = str(input('Informe o município: '))
eleitores = int(input('Informe o número de eleitores: '))
votoValido = int(input('Informe o número de votos válidos: '))
votoBranco = int(input('Informe o número de votos em branco: '))
votoNulo = int(input('Informe o número de votos nulos: '))

porcentagemVotoValido = (votoValido * 100) / eleitores
porcentagemVotoBranco = (votoBranco * 100) / eleitores
porcentagemVotoNulo = (votoNulo * 100) / eleitores

print()
print('-=' * 25)
print('O municipio de {} contém {} eleitores.'.format(municipio, eleitores))
print('VOTOS VÁLIDOS: {:.2f}%'
      '\nVOTOS BRANCOS: {:.2f}%'
      '\nVOTOS NULOS: {:.2f}%'.format(porcentagemVotoValido, porcentagemVotoBranco, porcentagemVotoNulo))
print('-=' * 25)
