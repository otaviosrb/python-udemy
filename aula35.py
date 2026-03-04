try:
    print('ABRIU O ARQUIVO')
    8 / 0
except:
    print('DIVIDIU POR 0')
else:
    print('NÃO DEU ERRO')
finally:
    print('FECHOU O ARQUIVO')