import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

# List comprehension

lista = []
# for numero in range(10):
#     lista.append(numero)

lista = [numero * 2 for numero in range(10)]
# print(lista)

# Mapeamento de dados
produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
]

novos_produtos = [{**produto, 'preço': produto['preço'] * 1.05}
                  if produto['preço'] > 20 else {**produto}
                  for produto in produtos
]
# print(*novos_produtos, sep = '\n')
# p(novos_produtos)

# Filtros
# lista = [n for n in range(10) if n < 5]
novos_produtos = [{**produto, 'preço': produto['preço'] * 1.05}
                  if produto['preço'] > 20 else {**produto}
                  for produto in produtos
                  if produto['preço'] > 10
]

p(novos_produtos)
