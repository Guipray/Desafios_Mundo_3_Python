from random import randint
from time import sleep
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
sorteados = []
for c in range(0, jogos):
    sorteados.append([])
    for n in range(0, 6):
        sorteados[c].append(randint(1, 60))
        if sorteados[c].count(sorteados[c][n]) > 1:
            del sorteados[c][n]
            sorteados[c].append(randint(1, 60))
print('-='*5, f'Sorteando {jogos} jogos', '-='*5)
for c in range(0, jogos):
    sorteados[c].sort()
    sleep(1)
    print(f'Jogo {c+1}: {sorteados[c]}')
sleep(1)
print('-='*5, '< Boa sorte! >', '-='*5)
