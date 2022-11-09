lista = list()
dados = dict()
sidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Tente novamente! O sexo deve ser M ou F!')
    dados['idade'] = int(input('Idade: '))
    sidade += dados['idade']
    lista.append(dados.copy())
    while True:
        opcao = str(input("Você quer continuar? [Sim/Não] ")).upper()[0]
        if opcao in 'SN':
            break
        print('Tente novamente! Digite Sim ou Não!')
    if opcao == 'N':
        break
print('-=' * 30)
print(f'foram cadastradas {len(lista)} pessoas')
midade = sidade / len(lista)
print(f'A média de idade é de {midade:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= midade:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\nFinalizado!')
