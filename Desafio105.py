def notas(*núm, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param núm: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resultado = dict()
    resultado['total'] = len(núm)
    resultado['maior'] = max(núm)
    resultado['menor'] = min(núm)
    resultado['média'] = sum(núm)/len(núm)
    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'BOA'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'RAZOÁVEL'
        else:
            resultado['situação'] = 'RUIM'
    return resultado


# Programa Principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
