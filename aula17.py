# 3 - Métodos úteis dos dicts:

# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Otávio',
    'sobrenome': 'Ribeiro'
}

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Sophia',
#     'idade': 16,    
# })
# p1.update(nome='Sophia', idade=16)
tupla = (('nome', 'Sophia'), ('idade', 16))
lista = [['nome', 'Sophia'], ['idade', 16]]
p1.update(lista)
print(p1)