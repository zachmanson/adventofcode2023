from copy import deepcopy

with open('input.txt') as reader:
    grid = [line.rstrip('\n') for line in reader]

og_grid = deepcopy(grid)

MAX_ROW = len(grid)
MAX_COL = len(grid[0])


def tilt(grid):
    rocks = [(row, col) for row, row_val in enumerate(grid) for col, val in enumerate(row_val) if val == 'O']
    for row, col in rocks:
        while 0 <= row - 1 < MAX_ROW and grid[row - 1][col] == '.':
            grid[row - 1] = grid[row - 1][:col] + 'O' + grid[row - 1][col + 1:]
            grid[row] = grid[row][:col] + '.' + grid[row][col + 1:]
            row -= 1

    return grid

grid = tilt(grid)

tot = 0
for row in range(MAX_ROW):
    for col in range(MAX_COL):
        if grid[row][col] == 'O':
            tot += (MAX_ROW - row)
print(tot)

#part 2
grid = og_grid
seen = []
cycle_found = 0
i = 0
while True:
    #much easier to rotate entire grid and tilt up to tilt in all four directions
    for x in range(4):
        grid = tilt(grid)
        transposed = list(map(list, zip(*grid)))
        grid = [''.join(row[::-1]) for row in transposed]

    if tuple(grid) in seen:
        cycle_found = i
        break
    else:
        seen.append(tuple(grid))
    i += 1

offset = 0
for i in range(len(seen)):
    if seen[i] == tuple(grid):
        offset = i
        break

cycle_len = cycle_found - offset
idx = ((1000000000 - offset) % cycle_len) + offset - 1 
grid = seen[idx]

tot = 0
for row in range(MAX_ROW):
    for col in range(MAX_COL):
        if grid[row][col] == 'O':
            tot += (MAX_ROW - row)
print(tot)
