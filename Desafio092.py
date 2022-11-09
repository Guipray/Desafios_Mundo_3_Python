from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - nasc
print('-='*40)
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')
