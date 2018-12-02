from itertools import combinations
from collections import Counter
from functools import reduce
import operator as op

def prod(xs):
    return reduce(op.mul, xs, 1)

def parse_input():
    return (x.strip() for x in open('2018/day02/in.txt', 'r'))


xs = list(parse_input())

# PART 1
codes = [2,3]

unique_counts = (set(Counter(x).values()) for x in xs)
checksum_counts = ([i in v for i in codes] for v in unique_counts)
checksum = prod(map(sum, zip(*checksum_counts)))
print(checksum)

# PART 2

diff = lambda a, b: [i for i, (x, y) in enumerate(zip(a,b)) if x != y]

pairs_with_diff = ((x, diff(*x)) for x in combinations(xs, 2))
(x, _), [i] = next(filter(lambda x: len(x[1]) == 1, pairs_with_diff))
common_letters = x[:i] + x[i:]
print(common_letters)