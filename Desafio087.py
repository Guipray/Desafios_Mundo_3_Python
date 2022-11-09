valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f'Digite um valor na posição [{l}][{c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}', end=']')
        if valores[l][c] % 2 == 0:
            soma += valores[l][c]
    print()
for l in range(0, 3):
    soma3 += valores[l][2]
for c in range(0, 3):
    if c == 0:
        maior = valores[1][c]
    elif valores[1][c] > maior:
        maior = valores[1][c]
print('-='*30)
print(f'A soma de todos os valores pares digitados foi {soma}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha da matrix é {maior}.')
