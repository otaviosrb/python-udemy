# Método Set - add, update, clear, discard
s1 = set()
s1.add('Otávio')
s1.add(1)
s1.update('Olá mundo!')
s1.update(('Olá mundo iterável!', 2, 3, 4))
# s1.clear()
s1.discard('Otávio')
# print(s1)

# Operadores Set - | & - ^
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # Une
s3 = s1 & s2 # Item em ambos
s3 = s1 - s2 # Item somente no set da esquerda
s3 = s1 ^ s2 # Item que não estão em ambos
print(s3)