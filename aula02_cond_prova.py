print('-=' * 15)
print('-=         HORÓSCOPO        -=')
print('-=' *15)

dia = int(input('Informe seu DIA de nascimento: '))
mes = int(input('Informe seu MÊS de nascimento: '))

if (21 <= dia <= 31 and mes == 3) or (dia >= 1 and dia <= 20 and mes == 4):
    signo = 'ÁRIES'
elif (dia >= 25 and dia <= 30 and mes == 4) or (dia >= 1 and dia <= 20 and mes == 5):
    signo = 'TOURO'
elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <= 20 and mes == 6):
    signo = 'GÊMEOS'
elif (dia >= 21 and dia <= 30 and mes == 6) or (dia >= 1 and dia <= 22 and mes == 7):
    signo = 'CÂNCER'
elif (dia >= 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <= 22 and mes == 8):
    signo = 'LEÃO'
elif (dia >= 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <= 22 and mes == 9):
    signo = 'VIRGEM'
elif (dia >= 23 and dia <= 30 and mes == 9) or (dia >= 1 and dia <= 22 and mes == 10):
    signo = 'LIBRA'
elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <= 21 and mes == 11):
    signo = 'ESCORPIÃO'
elif (dia >= 22 and dia <= 30 and mes == 11) or (dia >= 1 and dia <= 21 and mes == 12):
    signo = 'SAGITÁRIO'
elif (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <= 20 and mes == 1):
    signo = 'CAPRICÓRNIO'
elif (dia >= 21 and dia <= 31 and mes == 1) or (dia >=1 and dia <= 18 and mes == 2):
    signo = 'AQUÁRIO'
elif (dia >= 19 and dia <= 29 and mes == 2) or (dia >= 1 and dia <= 20 and mes == 3):
    signo = 'PEIXES'
else:
    signo = 'NÃO ENCONTRADO'
print(f'\nNascimento: {dia}/{mes}\nSigno: {signo}')
