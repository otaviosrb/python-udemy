nome = 'Otávio Ribeiro'

tamanho_nome = len(nome)
i = 0
nome_modificado = ''
while i < len(nome):
    letra = nome[i]
    nome_modificado += f'-{letra}'
    i += 1

nome_modificado += '-'
print(nome_modificado)