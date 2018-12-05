from itertools import combinations
from collections import Counter
from functools import reduce
import operator as op

def prod(xs):
    return reduce(op.mul, xs, 1)
import string

def parse_input():
    with open('2018/day05/in.txt', 'r') as f:
        while True:
            c = f.read(1)
            if c == '\n':
                break
            yield c


def opposite(x, y):
    return x.lower() == y.lower() and x != y

def reduce(stream):
    xs = []
    for c in stream:
        if xs and opposite(c, xs[-1]):
            xs.pop()
        else:
            xs.append(c)
    return xs

s = list(parse_input())

print('part 1', len(reduce(s)))
print('part 2', min([len(reduce(filter(lambda x: x.upper() != a, s))) for a in string.ascii_uppercase]))