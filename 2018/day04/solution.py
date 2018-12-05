from itertools import combinations, starmap
from collections import Counter
from functools import reduce
import operator as op
import re
from datetime import datetime
import numpy as np

def parse_record(rec):
    d, info = rec[:2], rec[2:]
    d = datetime.strptime(' '.join(d), '[%Y-%m-%d %H:%M]')
    if info[0] == 'falls':
        i = 'S'
    elif info[0] == 'wakes':
        i = 'W'
    else:
        i = int(info[1][1:])
    return d,i

def parse_input():
    p = r'#(\[.*\]) (.*)$'
    with open('2018/day04/in.txt', 'r') as f:
        return (parse_record(x.strip().split(' ')) for x in f.readlines())


xs = list(parse_input())
xs = sorted(xs, key=lambda x: x[0])
# for x in xs:
#     print(x)
# PART 1
curr = xs[0][1]
m = {curr: []}
for (d,i) in xs[1:]:
    if isinstance(i, int):
        curr = i
        if curr not in m: m[curr] = []
    else:
        m[curr].append((d,i))

rec = np.zeros((len(m), 60))
# print(rec.shape)
ids = list(m.keys())
for a, vs in enumerate(m.values()):
    ts = [d.minute for d, _ in vs]
    if not ts: continue
    s = min(ts)
    for i,j in zip(ts[::2], ts[1::2]):
        i = i - s
        rec[a,i:j] += 1
sums = rec.sum(axis=1)
mx = sums.max()
mx_i = sums.argmax()

print('part 1', mx*mx_i)

x = rec.argmax()
i, j = x // 60, x % 60
print('part 2', j * ids[i])
