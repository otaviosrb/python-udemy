def criar_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))