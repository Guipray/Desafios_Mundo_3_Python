expressão = str(input('Digite uma expressão: '))
pilha = []
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    if simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
