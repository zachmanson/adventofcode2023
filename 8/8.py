from math import gcd
from functools import reduce

with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

def lcm_list(numbers):
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    return reduce(lcm, numbers)

directions = lines[0]

network = {}
starting_nodes = []
for line in lines[2:]:
    node, links = line.split(' = ')
    links = links[1:-1].split(', ')
    network[node] = links
    if node.endswith('A'):
        starting_nodes.append(node)


current = 'AAA'
steps = 0 
while current != 'ZZZ':
    for d in directions:
        if d == 'L':
            current = network[current][0]
        else:
            current = network[current][1]
        steps += 1
 
print(steps) #part 1

steps_to_Z = []

for node in starting_nodes:
    steps = 0
    current = node
    while not current.endswith('Z'):
        for d in directions:
            if d == 'L':
                current = network[current][0]
            else:
                current = network[current][1]
            steps += 1

    steps_to_Z.append(steps)

print(lcm_list(steps_to_Z))
