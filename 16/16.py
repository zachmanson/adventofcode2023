with open('input.txt') as reader:
    grid = [line.rstrip('\n') for line in reader]

MAX_ROW = len(grid)
MAX_COL = len(grid[0])

dirs = {
        'right' : (0, 1),
        'left' : (0, -1), 
        'up' : (-1, 0), 
        'down': (1, 0)
        }

def get_next(row, col, d):
    dr, dc = d
    next_nodes = []
    if grid[row][col] == '.' or (grid[row][col] == '-' and d in [dirs['left'], dirs['right']]) or (grid[row][col] == '|' and d in [dirs['up'], dirs['down']]):
        if 0 <= row + dr < MAX_ROW and 0 <= col + dc < MAX_COL:
            next_nodes.append((row + dr, col + dc, dr, dc))
    elif grid[row][col] == '/':
        dr, dc = -dc, -dr
        if 0 <= row + dr < MAX_ROW and 0 <= col + dc < MAX_COL:
            next_nodes.append((row + dr, col + dc, dr, dc))
    elif grid[row][col] == '\\':
        dr, dc = dc, dr
        if 0 <= row + dr < MAX_ROW and 0 <= col + dc < MAX_COL:
            next_nodes.append((row + dr, col + dc, dr, dc))
    else:
        if grid[row][col] == '|':
            for d in [dirs['up'], dirs['down']]:
                dr, dc = d
                if 0 <= row + dr < MAX_ROW and 0 <= col + dc < MAX_COL:
                    next_nodes.append((row + dr, col + dc, dr, dc))
        else:
            for d in [dirs['left'], dirs['right']]:
                dr, dc = d
                if 0 <= row + dr < MAX_ROW and 0 <= col + dc < MAX_COL:
                    next_nodes.append((row + dr, col + dc, dr, dc))

        
    return next_nodes


def get_energized(start):
    queue = [start] 
    energized = set()
    energized.add((0, 0, *dirs['right']))

    while queue:
        row, col, dr, dc = queue.pop(0)
        
        for nr, nc, ddr, ddc in get_next(row, col, (dr, dc)):
            if (nr, nc, ddr, ddc) not in energized: 
                energized.add((nr, nc, ddr, ddc))   
                queue.append((nr, nc, ddr, ddc))

    return len({(x, y) for x, y, dx, dy in energized})

print(get_energized((0, 0, *dirs['right']))) #part 1

#part 2
max_e = 0
for row in range(MAX_ROW):
    val = get_energized((row, 0, *dirs['right']))
    if val > max_e:
        max_e = val
    val = get_energized((row, MAX_COL - 1, *dirs['left']))
    if val > max_e:
        max_e = val

for col in range(MAX_COL):
    val = get_energized((0, col, *dirs['down']))
    if val > max_e:
        max_e = val
    val = get_energized((MAX_ROW - 1, col, *dirs['up']))

print(max_e)
