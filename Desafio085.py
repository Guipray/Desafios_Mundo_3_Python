valores = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print('-='*30)
print(f'Os valores pares são: {valores[0]}')
print(f'Os valores ímpares são: {valores[1]}')
