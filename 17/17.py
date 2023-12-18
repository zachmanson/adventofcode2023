import heapq

with open('input.txt') as reader:
    grid = [line.rstrip('\n') for line in reader]

MAX_ROW = len(grid)
MAX_COL = len(grid[0])

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

def is_valid(r, c):
    return 0 <= r < MAX_ROW and 0 <= c < MAX_COL


start = (0, 0)
end = (MAX_ROW - 1, MAX_COL - 1)

def solve(start, part2 = False):
    #can start moving in right or down
    visited = {(*start, 0, 1, 1), (*start, 1, 0, 1)}
    pq = [(0, *start, 1, 0, 1)] #heat, pos, dir, steps. Heat needs to be first element because we want to pop according to lowest heat
    heapq.heappush(pq, (0, *start, 0, 1, 1))

    while pq:
        heat, row, col, dr, dc, steps = heapq.heappop(pq)

        if (row, col) == end:
            return heat

        for ddr, ddc in dirs:
            if (ddr, ddc) == (dr, dc):
                if steps < 3 and not part2 or steps < 10 and part2:
                    nr = row + ddr
                    nc = col + ddc
                    if is_valid(nr, nc) and (nr, nc, ddr, ddc, steps + 1) not in visited:
                        visited.add((nr, nc, ddr, ddc, steps + 1))
                        heapq.heappush(pq, (heat + int(grid[nr][nc]), nr, nc, ddr, ddc, steps + 1))
                else:
                    continue
            elif (ddr, ddc) != (dr, dc) and (ddr, ddc) != (-dr, -dc):
                nr = row + ddr
                nc = col + ddc
                if is_valid(nr, nc) and (nr, nc, ddr, ddc, 1) not in visited:
                    if part2:
                        if steps >= 4:
                            visited.add((nr, nc, ddr, ddc, 1))
                            heapq.heappush(pq, (heat + int(grid[nr][nc]), nr, nc, ddr, ddc, 1))
                    else:
                        visited.add((nr, nc, ddr, ddc, 1))
                        heapq.heappush(pq, (heat + int(grid[nr][nc]), nr, nc, ddr, ddc, 1))


print(solve(start))
print(solve(start, part2 = True))
