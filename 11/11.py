with open('input.txt') as reader:    
    grid = [line.rstrip('\n') for line in reader]

#all of this was only useful for part 1
def expand(grid):
    rows_to_expand = [i for i, row in enumerate(grid) if all(cell == '.' for cell in row)]
    row_offset = 0
    for row in rows_to_expand:
        new_row = ['.' for x in range(len(grid[0]))]
        grid.insert(row + 1 + row_offset, new_row)
        row_offset += 1

    transposed = list(map(list, zip(*grid)))
    col_offset = 0
    cols_to_expand = [i for i, col in enumerate(transposed) if all(cell == '.' for cell in col)]
    for col in cols_to_expand:
        new_col = ['.' for x in range(len(transposed[0]))]
        transposed.insert(col + 1 + col_offset, new_col)
        col_offset += 1

    return list(map(list, zip(*transposed)))

grid = expand(grid)
galaxies = [(r, c) for r, rowvals in enumerate(grid) for c, colvals in enumerate(rowvals) if colvals == '#']

total = 0
for i, (row_1, col_1) in enumerate(galaxies):
    for (row_2, col_2) in galaxies[i:]:
        total += abs(row_2 - row_1) + abs(col_2 - col_1)
print(total)


#part 2
#this could also be the solution to part 1, replacing 1000000 with 2, but I wanted to keep both
#approaches for reference
with open('input.txt') as reader:
    grid = [line.rstrip('\n') for line in reader]

empty_rows = [i for i, row in enumerate(grid) if all(cell == '.' for cell in row)]
transposed = list(map(list, zip(*grid)))
empty_cols = [i for i, col in enumerate(transposed) if all(cell == '.' for cell in col)]
galaxies = [(r, c) for r, rowvals in enumerate(grid) for c, colvals in enumerate(rowvals) if colvals == '#']

total = 0
for i, (row_1, col_1) in enumerate(galaxies):
    for (row_2, col_2) in galaxies[i:]:
        for r in range(min(row_1, row_2), max(row_1, row_2)):
            if r in empty_rows:
                total += 1000000
            else:
                total += 1
        for c in range(min(col_1, col_2), max(col_1, col_2)):
            if c in empty_cols:
                total += 1000000
            else:
                total += 1
print(total)

