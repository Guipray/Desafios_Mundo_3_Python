times = ('Corinthians', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avaí', 'América-MG',
         'Palmeiras', 'Bragantino', 'Internacional', 'Fluminense', 'Goiás', 'Cuiabá', 'Athletico-PR', 'Flamengo',
         'Juventude', 'Ceará SC', 'Atlético-GO', 'Fortaleza')
print(f'Lista de Times do Brasileirão: {times}.')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os últimos 4 são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}.')
print(f'O América-MG está na {times.index("América-MG")+1}ª posição')
