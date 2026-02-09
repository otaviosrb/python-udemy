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

letras = 'abcd'
acertos = 0
for questao in perguntas:
    print(f'Pergunta: {questao['Pergunta']}')
    print('\nOpções:')
    for i, opcao in enumerate(questao['Opções']):
        print(f'{letras[i]}) {opcao}')
    while True:
        opcao = input('Escolha uma opção: ').lower().strip()
        if opcao in letras and len(opcao) == 1:
            break
        print(f'Opção inválida! Escolha entre: {', '.join(letras)}')
    indice_resposta = questao['Opções'].index(questao['Resposta'])
    letra_resposta = letras[indice_resposta]
    if opcao == letra_resposta:
        print('Acertou!\n')
        acertos += 1
    else:
        print('Errou!')
print(f'\nVocê acertou {acertos}/{len(perguntas)}!')


