numero_1 = int(input('Digite o 1º número: '))
numero_2 = int(input('Digite o 2º número: '))
print()
for n in range(numero_1, numero_2+1):
    if n > 1:
        for p in range(2, n):
            if n % p == 0:
                break
        else:
            print(n, end=' ')
print()
