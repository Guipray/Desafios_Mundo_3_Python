números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    opção = ''
    while opção != 'N':
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            print(f'Você digitou o número {números[num]}')
            break
        print('Comando Inválido! Tente Novamente!')
    opção = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print('Fim!')
