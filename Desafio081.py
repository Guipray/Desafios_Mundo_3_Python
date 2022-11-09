lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opção = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} valores, e são eles {lista}.')
lista.sort(reverse=True)
print(f'Em ordem decrescente fica: {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
