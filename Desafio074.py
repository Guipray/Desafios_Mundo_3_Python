from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n}', end=' ')
print(f'\nO maior valor é o número {max(números)}!\nO menor valor é o número {min(números)}!')
