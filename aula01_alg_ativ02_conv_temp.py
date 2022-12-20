print('-=' * 20)
print('CONVERSOR DE TEMPERATURA - Atividade 02')
print('-=' * 20)

fahrenheit = float(input('Insira a temperatura em ºF: '))
celsius = (fahrenheit - 32) * (5 / 9)

print('\nA temperatura {:.1f}ºF, equivale a {:.1f}ºC.'.format(fahrenheit, celsius))
