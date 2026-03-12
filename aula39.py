import importlib

import aula39_m

print(aula39_m.variavel)
for i in range(10):
    importlib.reload(aula39_m)

print('Fim')