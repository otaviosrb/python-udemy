# raise

def nao_aceito_zero(n):
    if n == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    return True

def aceito_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'{n} deve ser int ou float | '
            f'{tipo_n.__name__} enviado'
        )
    return True

def divide(n, d):
    aceito_int_ou_float(n)
    aceito_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))

