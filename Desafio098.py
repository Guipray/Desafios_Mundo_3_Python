from time import sleep


def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(2)
    if início <= fim:
        for n in range(início, fim + 1, passo):
            print(n, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        for n in range(início, fim - 1, - passo):
            print(n, end=' ')
            sleep(0.5)
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
