lista = []
pares = []
ímpares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    opção = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        ímpares.append(v)
print(f'Os Valores digitados foram: {lista}')
print(f'Os valores pares digitados são: {pares}')
print(f'Os valores ímpares digitados são: {ímpares}')
