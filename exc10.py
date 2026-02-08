def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'

resultado_multiplicacao = multiplicacao(1, 2, 3, 4, 5)
print(resultado_multiplicacao)

print(par_impar(2))
print(par_impar(3))
print(par_impar(314))
print(par_impar(729))
