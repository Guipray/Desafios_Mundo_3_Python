def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
mensagem = str(input('Escreva algo para mostrar na tela: '))
escreva(mensagem)
