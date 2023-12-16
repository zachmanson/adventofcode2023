with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

groups = []
for line in lines:
    for group in line.split(','):
        groups.append(group)

def hash_alg(string):
    c = 0 
    for char in string:
        c += ord(char)
        c *= 17
        c = c % 256
    return c


tot = 0
for g in groups:
    tot += hash_alg(g)

print(tot) #part 1

boxes = [[] for x in range(256)]
foclen_dict = {}

for g in groups:
    if '-' in g:
        label = g[:-1]
        idx = hash_alg(label)
        if label in boxes[idx]:
            boxes[idx].remove(label)
    else:
        label, foclen = g.split('=')

        idx = hash_alg(label)
        if label not in boxes[idx]:
            boxes[idx].append(label)

        foclen_dict[label] = int(foclen)
            
tot = 0
for i, val in enumerate(boxes):
    c = 0
    for label in val:
        c = (i + 1) * (val.index(label) + 1) * foclen_dict[label]
        tot += c

print(tot)
