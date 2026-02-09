# Dicionários (tipo dict)
# {}
# Tipos imutáveis: str, int, float, bool, tuple
# Tipos mutáveis: dict, list

# pessoa = dict(nome='Otávio', sobrenome='Ribeiro')

pessoa = {
    'nome': 'Otávio',
    'sobrenome': 'Ribeiro',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'guianas', 'número': 97},
        {'rua': 'venezuela', 'número': 287},
    ],
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])