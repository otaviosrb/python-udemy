# Generator expression, Iterables e  Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
generator = (n for n in range(10))

# print(next(generator))

for n in generator:
    print(n)
