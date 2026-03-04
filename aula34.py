try:
    a = 18
    b = 0
    print('Linha 1'[1000])
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero') 
except NameError:
    print('Nome não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')