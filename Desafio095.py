jogadores = list()
jogador = dict()
gols = list()
while True:
    print('-' * 30)
    gols.clear()
    jogador.clear()
    while True:
        jogador['nome'] = str(input('Nome do Jogador: '))
        if jogador['nome'] == '':
            print('Você esqueceu de adicionar o nome!')
        else:
            break
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('Opção inválida! Digite Sim ou Não!')
    if opcao == 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
soma = 0
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-' * 40)
    mostrar = int(input('Mostar dados de qual jogador? '))
    if mostrar == 999:
        break
    if mostrar < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]["nome"]}:')
        for i, g in enumerate(jogadores[mostrar]['gols']):
            print(f'    No jogo {i + 1} fez {g} gosl.')
    else:
        print('Este jogador não existe! Tente Novamente!')
print('Fim!')
