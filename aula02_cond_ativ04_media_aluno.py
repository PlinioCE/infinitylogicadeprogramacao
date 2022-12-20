print('-=' * 15)
print('BOLETIM ALUNO - Atividade - 04')
print('-=' * 15)

nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
nota3 = float(input('Informe a 3ª nota: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    status = 'APROVADO!'
elif 4 <= media < 7:
    status = 'de RECUPERAÇÃO!'
else:
    status = 'REPROVADO!'
print(f'\nSua média é {media}, você está {status}')
