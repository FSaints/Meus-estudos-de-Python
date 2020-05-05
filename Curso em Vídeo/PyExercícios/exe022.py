nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Analisando nome...')
print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print(f'Seu nome com letras minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')



