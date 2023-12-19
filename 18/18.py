from shapely.geometry import Polygon

with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

dirs = {
        'R' : (0, 1),
        'L' : (0, -1),
        'U' : (-1, 0),
        'D' : (1, 0)
        }

dirsp2 = {
        '0' : (0, 1),
        '2' : (0, -1),
        '3' : (-1, 0),
        '1' : (1, 0)
        }

start = (0, 0)
current = start
currentp2 = start

vertex = [start]
vertexp2 = [start]
per = 0
perp2 = 0

for line in lines:
    d, num_steps, colour = line.split(' ')
    num_steps = int(num_steps)
    colour = colour[2:-1]

    #part 1
    dr, dc = dirs[d]
    current = (current[0] + (dr * (num_steps)), current[1] + (dc * (num_steps)))
    vertex.append(current)
    per += num_steps
    
    #part 2
    num_steps = int(colour[:-1], 16)
    dr, dc = dirsp2[colour[-1]] 
    currentp2 = (currentp2[0] + (dr * (num_steps)), currentp2[1] + (dc * (num_steps)))
    vertexp2.append(currentp2)
    perp2 += num_steps

def calculate_area(v, perimeter):
    area = 0
    for i in range(len(v) - 1):
        area += v[i][0] * v[i+1][1]
        area -= v[i][1] * v[i+1][0]

    area += perimeter

    return (area // 2) + 1

print(calculate_area(vertex[::-1], per))
print(calculate_area(vertexp2[::-1], perp2))
