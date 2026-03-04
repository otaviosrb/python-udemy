# Yield from

def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6

g2 = gen2(gen1)
for n in g2:
    print(n)
