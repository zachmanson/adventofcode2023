from itertools import groupby

with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

def all_equal(a):
    g = groupby(a)
    return next(g, True) and not next(g, False)

tot = 0
totp2 = 0
for line in lines:
    numbers = [int(x) for x in line.split(' ')]
    last_nums = [numbers[-1]]
    first_nums = [numbers[0]]
    while not all_equal(numbers):
        numbers = [x - y for x, y in zip(numbers[1:], numbers[:-1])]
        last_nums.append(numbers[-1])
        first_nums.append(numbers[0])

    diff = first_nums[-1]
    for x in reversed(first_nums[:-1]):
        diff = x - diff
    
    totp2 += diff
    tot += sum(last_nums)

print(tot)
print(totp2)
