# CALCULADORA
import os


def limpar():
    os.system('cls')

while True:
    entrada_n1 = input('Digite um número: ')
    entrada_n2 = input('Digite outro número: ')
    try:
        n1 = int(entrada_n1)
        n2 = int(entrada_n2)
        break
    except:
        limpar()
        print('Digite valores númericos')

while True:
    sinal = input('Selecione a operação [+ - / x]: ')
    if sinal in ['+','-','/','x']:
        break
    limpar()
    print('Selecione uma operação válida!')

if sinal == '+':
    resultado = n1 + n2
elif sinal == '-':
    resultado = n1 + n2
elif sinal == '/':
    resultado = n1 / n2
elif sinal == 'x':
    resultado = n1 * n2

print()
print(f'{n1} {sinal} {n2} = {resultado}')


        