print('-=' * 15)
print('-=         HORÓSCOPO        -=')
print('-=' *15)

dia = int(input('Informe seu DIA de nascimento: '))
mes = int(input('Informe seu MÊS de nascimento: '))

if (21 <= dia <= 31 and mes == 3) or (1 <= dia <= 20 and mes == 4):
    signo = 'ÁRIES'
elif (25 <= dia <= 30 and mes == 4) or (1 <= dia <= 20 and mes == 5):
    signo = 'TOURO'
elif (21 <= dia <= 31 and mes == 5) or (1 <= dia <= 20 and mes == 6):
    signo = 'GÊMEOS'
elif (21 <= dia <= 30 and mes == 6) or (1 <= dia <= 22 and mes == 7):
    signo = 'CÂNCER'
elif (23 <= dia <= 31 and mes == 7) or (1 <= dia <= 22 and mes == 8):
    signo = 'LEÃO'
elif (23 <= dia <= 31 and mes == 8) or (1 <= dia <= 22 and mes == 9):
    signo = 'VIRGEM'
elif (23 <= dia <= 30 and mes == 9) or (1 <= dia <= 22 and mes == 10):
    signo = 'LIBRA'
elif (23 <= dia <= 31 and mes == 10) or (1 <= dia <= 21 and mes == 11):
    signo = 'ESCORPIÃO'
elif (22 <= dia <= 30 and mes == 11) or (1 <= dia <= 21 and mes == 12):
    signo = 'SAGITÁRIO'
elif (22 <= dia <= 31 and mes == 12) or (1 <= dia <= 20 and mes == 1):
    signo = 'CAPRICÓRNIO'
elif (21 <= dia <= 31 and mes == 1) or (1 <= dia <= 18 and mes == 2):
    signo = 'AQUÁRIO'
elif (19 <= dia <= 29 and mes == 2) or (1 <= dia <= 20 and mes == 3):
    signo = 'PEIXES'
else:
    signo = 'NÃO ENCONTRADO'
print(f'\nNascimento: {dia}/{mes}\nSigno: {signo}')
