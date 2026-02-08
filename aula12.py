# Args

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma1_a_5 = soma(1, 2, 3, 4, 5)
print(soma1_a_5)

print(sum((1, 2, 3, 4, 5)))

numeros = 1, 2, 3, 4, 5
outra_soma = soma(*numeros)
print(outra_soma)