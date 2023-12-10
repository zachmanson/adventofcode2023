with open('input.txt') as reader:
    grid = [line.rstrip('\n') for line in reader]

MAX_ROW = len(grid)
MAX_COL = len(grid[0])

connections = {
        '|': [1, 0, 1, 0],
        '-': [0, 1, 0, 1],
        'L': [1, 1, 0, 0],
        'J': [1, 0, 0, 1],
        '7': [0, 0, 1, 1],
        'F': [0, 1, 1, 0],
        '.': [0, 0, 0, 0],
        'S': [None, None, None, None] #S included here to get rid of Key error
        }

#find starting position
start = (0, 0)
for row in range(MAX_ROW):
    for col in range(MAX_COL):
        if grid[row][col] == 'S':
            start = (row, col)

#function to find neighbors of a node 
def get_neighbors(node):
    row = node[0]
    col = node[1]
    neighbors = []
    if grid[row][col] == 'S': #neighbors of S are all nodes pointing towards it
        if 0 <= row - 1 < MAX_ROW and connections[grid[row-1][col]][2] == 1:
            neighbors.append((row - 1, col)) #north
        if 0 <= col + 1 < MAX_COL and connections[grid[row][col+1]][3] == 1:
            neighbors.append((row, col + 1)) #east
        if 0 <= row + 1 < MAX_ROW and connections[grid[row+1][col]][0] == 1:
            neighbors.append((row + 1, col)) #south
        if 0 <= col - 1 < MAX_COL and connections[grid[row][col-1]][1] == 1:
            neighbors.append((row, col - 1)) #west
    else:
        node_connections = connections[grid[row][col]] #check if connections match
        if 0 <= row - 1 < MAX_ROW and connections[grid[row-1][col]][2] == 1 and node_connections[0] == 1:
            neighbors.append((row - 1, col)) #north
        if 0 <= col + 1 < MAX_COL and connections[grid[row][col+1]][3] == 1 and node_connections[1] == 1:
            neighbors.append((row, col + 1)) #east
        if 0 <= row + 1 < MAX_ROW and connections[grid[row+1][col]][0] == 1 and node_connections[2] == 1:
            neighbors.append((row + 1, col)) #south
        if 0 <= col - 1 < MAX_COL and connections[grid[row][col-1]][1] == 1 and node_connections[3] == 1:
            neighbors.append((row, col - 1)) #west
    return neighbors

#BFS. The farthest node is the last node visited
visited = [start]
queue = [(start[0], start[1], 0)]
last_visited = None

while queue:
    headrow, headcol, steps  = queue.pop(0)
    head = (headrow, headcol)
    last_visited = (head, steps)

    for neighbor in get_neighbors(head):
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append((neighbor[0], neighbor[1], steps + 1))

print(last_visited[-1]) #part 1

#figure out what S is
S_connections = [0, 0, 0, 0]

if 0 <= start[0] - 1 < MAX_ROW:
    S_connections[0] = connections[grid[start[0] - 1][start[1]]][2]
if 0 <= start[1] + 1 < MAX_COL:
    S_connections[1] = connections[grid[start[0]][start[1] + 1]][3]
if 0 <= start[0] + 1 < MAX_ROW:
    S_connections[2] = connections[grid[start[0] + 1][start[1]]][0]
if 0 <= start[1] - 1 < MAX_COL:
    S_connections[3] = connections[grid[start[0]][start[1] - 1]][1]

S = None
for key, val in connections.items():
    if S_connections == val:
        S = key

grid = [row.replace('S', S) for row in grid] #replace S with its character

#moving left to right, every time keep track of the number of times we cross a south facing pipe
#that is part of the visited nodes. If we visit an unvisited node before a pair of south facing pipes
#in the circuit is found, then that node is inside.
count = 0
for row in range(MAX_ROW):
    inside = False
    for col in range(MAX_COL):
        if (row, col) in visited and grid[row][col] in [key for key, val in connections.items() if val[2] == 1]:
            inside = not inside
        if (row, col) not in visited and inside:
            count += 1
print(count)
