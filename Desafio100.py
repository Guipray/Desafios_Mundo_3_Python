from random import randint
from time import sleep


def sorteia(lista):
        print('Sorteando 5 valores da lista: ', end='')
        for cont in range(0, 5):
                lista.append(randint(1, 10))
                print(lista[cont], end=' ')
                sleep(0.5)
        print('PRONTO!')


def somaPar(lista):
        soma = 0
        for v in lista:
                if v % 2 == 0:
                        soma += v
        print(f'Somandos os valores pares de {números}, temos {soma}')


# Programa Principal
números = list()
sorteia(números)
somaPar(números)

