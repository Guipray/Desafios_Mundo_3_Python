num = []
menor = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao fim da Lista!')
    else:
        p = 0
        while p < len(num):
            if n <= num[p]:
                num.insert(p, n)
                print(f'Adicionado na {p+1}ª posição.')
                break
            p += 1
print(f'Os valores que você digitou são: {num}')
