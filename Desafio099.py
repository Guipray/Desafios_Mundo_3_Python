from time import sleep


def maior(* núm):
    print('-=' * 30)
    print('Analisando os valores passados...')
    ma = cont = 0
    for v in núm:
        print(v, end=' ')
        sleep(0.5)
        if cont == 0:
            ma = v
        else:
            if v > ma:
                ma = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor da informado foi {ma}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
