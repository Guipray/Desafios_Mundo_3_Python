num = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado na memória!')
    else:
        print('O valor digitado já está presente na Lista!\nTente outro valor!')
    opção = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
num.sort()
print('=-'*30)
print(f'Você digitou os valores {num}')
