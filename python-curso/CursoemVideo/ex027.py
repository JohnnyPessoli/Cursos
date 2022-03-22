nome = str(input('Digite seu nome: ')).strip()
nom = nome.split()
print(f'Seu primeiro nome é {nom[0]}')
print(f'Seu ultimo nome é {nom[len(nom)-1]}')
