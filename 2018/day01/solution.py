from itertools import accumulate, cycle

def parse_input():
    return (int(n) for n in open('2018/day01/in.txt', 'r').readlines())

# PART 1
print(sum(parse_input()))


# PART 2
def duplicates(xs):
    seen = set([0])
    for x in xs:
        if x in seen:
            yield x
        else:
            seen.add(x)

print(next(duplicates(accumulate(cycle(parse_input())))))