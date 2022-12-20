print('-=' * 15)
print('DETETIVE - Atividade 11')
print('-=' * 15)

nome = str(input('Digite seu nome: ')).title().strip()
print(f'\n{nome}, você terá que responder algumas perguntas para sua liberação.')
pergunta1 = str(input('\nTelefonou para a vítima? [S/N] ')).upper()
pergunta2 = str(input('Esteve no local do crime? [S/N] ')).upper()
pergunta3 = str(input('Mora próximo à vítima? [S/N] ')).upper()
pergunta4 = str(input('Devia para a vítima? [S/N] ')).upper()
pergunta5 = str(input('Já trabalhou com a vítima? [S/N] ')).upper()
contaSim = 0

if pergunta1 == 'S':
    contaSim += 1
if pergunta2 == 'S':
    contaSim += 1
if pergunta3 == 'S':
    contaSim += 1
if pergunta4 == 'S':
    contaSim += 1
if pergunta5 == 'S':
    contaSim += 1
if contaSim == 5:
    print('\nASSASSINO!')
elif contaSim >= 3:
    print('\nCÚMPLICE!')
elif contaSim == 2:
    print('\nSUSPEITO!')
else:
    print('\nINOCENTE!')
