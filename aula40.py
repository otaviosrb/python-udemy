# from sys import path

# import aula40_package.modulo
# from aula40_package import modulo
# from aula40_package.modulo import soma_do_modulo
# from aula40_package.modulo import *

# # print(*path, sep='\n')
# print(soma_do_modulo(2,3))
# print(variavel)

import aula40_package
from aula40_package import soma_do_modulo

print(aula40_package.dobra(4))
print(soma_do_modulo(2,4))