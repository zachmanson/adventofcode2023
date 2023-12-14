with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

mirrors = []
mirror = []
for line in lines:
    if line == '':
        mirrors.append(mirror)
        mirror = []
    else:
        mirror.append(line)
mirrors.append(mirror)

def solve(mirror, part2 = False):
    N = len(mirror)
    for i in range(1, N):
        before = []
        after = []
        for j in range(min(i, N - i)):
            before.append(mirror[i - j - 1])
            after.append(mirror[i + j])

        if not part2:
            if before == after:
                return i

        else:
            count = 0
            for a, b in zip(before, after):
                for x, y in zip(a, b):
                    if x != y:
                        count += 1
            if count == 1:
                return i
    return 0
            
tot = 0
totp2 = 0
for m in mirrors:
    transposed = [''.join(row) for row in list(map(list, zip(*m)))]
    tot += (solve(m) * 100 + solve(transposed))
    totp2 += (solve(m, part2 = True) * 100 + solve(transposed, part2 = True))
print(tot)
print(totp2)
