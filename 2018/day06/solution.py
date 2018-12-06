from itertools import starmap, groupby, product

def parse_input():
    return (tuple(map(int, x.strip().split(', '))) for x in open('2018/day06/in.txt', 'r'))

data = list(parse_input())

x_min, x_max = min(map(lambda x:x[0], data)), max(map(lambda x:x[0], data))
y_min, y_max = min(map(lambda x:x[1], data)), max(map(lambda x:x[1], data))

blacklist = set([None])
labeled_data = list(enumerate(data))

def dist(x, y, a, b): 
    return abs(x-a) + abs(y-b)

def closest(x,y): 
    xs = sorted(list(starmap(lambda id, p: (id, dist(x,y, *p)), labeled_data)), key=lambda x: x[1])
    r = None if xs[0][1] == xs[1][1] else xs[0][0]
    if x in (x_max, x_min) or y in (y_max, y_min):
        blacklist.add(r)
    return r

def sum_coordinates(x, y):
    return sum(map(lambda p: dist(x,y, *p), data))

grid = list(product(range(x_min, x_max+1), range(y_min, y_max+1)))
ps = list(filter(lambda x: x not in blacklist, starmap(closest, grid)))
grouped = list((x[0], len(list(x[1]))) for x in groupby(sorted(ps)) if x[0])

print('part 1', sorted(grouped, key=lambda x: x[1])[-1])
print('part 2', len(list(filter(lambda x: x < 10000, starmap(sum_coordinates, grid)))))


