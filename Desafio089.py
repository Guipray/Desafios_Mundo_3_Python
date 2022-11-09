Boletim = []
cont = 0
while True:
    nome = str(input('Nome: '))
    Boletim.append([nome])
    nota1 = float(input('Nota 1: '))
    Boletim[cont].append([nota1])
    nota2 = float(input('Nota 2: '))
    Boletim[cont][1].append([nota2])
    cont += 1
    opção = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
for c in range(1, cont+1):
    média = (Boletim[c-1][1][0] + Boletim[c-1][1][1][0]) / 2
print('-='*30)
print('No. Nome         Média')
print('-'*30)
for c in range(1, cont+1):
    média = (Boletim[c - 1][1][0] + Boletim[c - 1][1][1][0]) / 2
    print(f'{c-1}   {Boletim[c-1][0]<15}', end='')
    print(f'{média:>.1f}')
print('-'*40)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas != 999:
        print(f'Notas de {Boletim[notas][0]}: {[Boletim[notas][1][0], Boletim[notas][1][1][0]]}')
    else:
        break
    print('-'*40)
print('Finalizando...')
