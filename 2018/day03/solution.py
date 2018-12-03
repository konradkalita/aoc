from itertools import chain, starmap
from collections import namedtuple
from functools import reduce
import operator as op
import re
import numpy as np

Claim = namedtuple('Claim', ['id', 'x', 'y', 'w', 'h'])

def parse_input():
    p = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    with open('2018/day03/in.txt', 'r') as f:
        return (Claim(*(map(int, re.search(p, x).groups()))) for x in f.readlines())


xs = list(parse_input())
xs = sorted(xs)

# PART 1

M = np.zeros((1000, 1000))
for (_,x,y, w, h) in xs:
    M[x:x+w, y:y+h] += 1

print(np.sum(M > 1))

# PART 2

intersect = lambda a, b: a.x <= b.x <= a.x + a.w and (a.y <= b.y <= a.y + a.h or b.y <= a.y <= b.y + b.h )
for i, a in enumerate(xs):
    if not any((intersect(a, b) or intersect(b, a) for b in chain(xs[:i], xs[i+1:]))):
        print(a.id)
