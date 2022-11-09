num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-'*30)
print(f'Você digitou os valores ', end='')
for v in num:
    print(v, end=' ')
print(f'\nO maior valor é o {max(num)} nas posições ', end='')
for p, valor in enumerate(num):
    if valor == max(num):
        print(f' {p}...', end='')
print(f'\nO menor valor é o {min(num)} nas posições ', end='')
for p, valor in enumerate(num):
    if valor == min(num):
        print(f' {p}...', end='')
print('\nFim!')
