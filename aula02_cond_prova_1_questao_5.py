numero = int(input('Digite um número: '))
f = 1
print(f'\n{numero}! = ', end='')
for n in range(numero, 0, -1):
    f *= n
    if n == 1:
        print(f'{n} = ', end='')
    else:
        print(f'{n} * ', end='')
print(f)
