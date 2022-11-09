def voto(idade):
    from datetime import date
    data = date.today().year
    idade = data - nasc
    if 18 <= idade <= 64:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 65 or 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÂO VOTA.'


# Programa Principal
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
