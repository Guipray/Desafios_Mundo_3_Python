num = (int(input('Digite um valor: ')), int(input('Digite um outro valor: ')),
       int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print(f'Você digitou os seguintes valores: {num}.')
print(f'O valor 9 apareceu {num.count(9)} vez(es).')
if 3 not in num:
    print(f'O valor 3 não foi digitado!')
else:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição ')
print(f'Os números pares são:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
