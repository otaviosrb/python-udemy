perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for questao in perguntas:
    indice = 0
    print(f'Pergunta: {questao['Pergunta']}')
    print()
    print('Opções:')
    for opcao in questao['Opções']:
        print(f'{indice}) {opcao}')
        indice += 1
    opcao = int(input('Escolha uma opção: '))
    indice_resposta = questao['Opções'].index(questao['Resposta'])
    if opcao == indice_resposta:
        print('Acertou!')
        acertos += 1
        print()
    else:
        print('Errou!')
print(f'Você acertou {acertos}/{len(perguntas)}')


