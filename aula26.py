#Exc List Comprehension

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pares_ao_quadrado = [
                    numero*numero
                    for linha in matriz 
                    for numero in linha
                    if numero % 2 == 0
]

print(pares_ao_quadrado)
 