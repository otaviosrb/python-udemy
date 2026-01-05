num_inteiro = input('Digite um número inteiro: ')

try:
    if int(num_inteiro) % 2 == 0:
        print(f'{num_inteiro} é par')
    else:
        print(f'{num_inteiro} é ímpar')
except:
    print('Você não digitou um número inteiro')