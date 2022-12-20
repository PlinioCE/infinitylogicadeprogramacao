nota = float(input('Digite sua nota: '))

if nota >= 7:
    print('APROVADO por média.')
    if nota > 9:
        print('PARABÉNS!')
    print('BOAS FÉRIAS!')
else:
    if nota >= 4 and nota < 7:
        print('RECUPERAÇÃO!!!')
        print('A prova estará disponível próxima semana!')
    else:
        print('REPROVADO!')
        print('Prova de recuperação indisponível!')
