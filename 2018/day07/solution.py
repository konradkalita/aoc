from itertools import combinations, groupby
from collections import Counter
from functools import reduce, cmp_to_key
import operator as op


def parse_input():
    xs = (x.strip().split() for x in open('2018/day07/in.txt', 'r'))
    return ((x[1],x[7]) for x in xs)

xs = list(parse_input())
print(xs)
# PART 1
xs = list((i, set(map(lambda y: y[1], x))) for (i,x) in groupby(sorted(xs), key=lambda x:x[0]))
# xs = sorted(xs, key=cmp_to_key(cmp))
# print(xs[0], xs[5], cmp(xs[0], xs[5]))
top = []
keys = set()
first=[]
for _,x in xs:
    keys = keys | x
for x,_ in xs:
    if x not in keys:
        first.append(x)
    keys = keys - set(x)

print(keys)
print(first)
xs.append(('*', set(first)))
xs.append(('J', set()))

def find_empty(xs):
    xs = list(filter(lambda x: not x[1], xs))
    print(xs)
    xs = sorted(xs, key= lambda x: x[0])
    print(xs)
    return xs[-1]
while xs:
    e = find_empty(xs)
    xs.remove(e)
    top.append(e[0])
    for (i,s) in xs:
        if e[0] in s:
            s.remove(e[0])
print(''.join(top[::-1]))