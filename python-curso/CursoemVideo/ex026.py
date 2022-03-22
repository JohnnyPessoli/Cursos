nom = str(input('Digite seu nome: ')).strip().upper()
print(f'{nom} tem {len(nom)} caracteres, destes tem um total de {nom.count("A")} "A"')
print(f'A primeira letra A apareceu na posição {nom.find("A")+1}')
print(f'A ultima ocorrência de A aparece na posiçao {nom.rfind("A")+1}')


