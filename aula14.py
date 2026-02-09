# Manipulação de chaves e valores eem dicts

pessoa = {}

chave = 'nome'
pessoa[chave] = 'Otávio'
pessoa['sobrenome'] = 'Ribeiro'

print(pessoa)

pessoa[chave] = 'Sophia'
print(pessoa)

del pessoa['sobrenome']
print(pessoa)

# print(pessoa.get('sobrenome')) # Retorna None se a chave não existir
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])