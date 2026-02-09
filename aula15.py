# Métodos úteis dos dicts:

# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome': 'Otávio',
    'sobrenome': 'Ribeiro',
    # 'idade': '18',
}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.setdefault('idade', 0))
