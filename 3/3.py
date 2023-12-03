with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

MAX_ROW = len(lines)
MAX_COL = len(lines[0])

symbols = [*'!@#$%^&*()-_=+[]{};:/?<>`~']
dirs = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

def next_to_symbol(row, col, number):
    for i in range(len(number)):
        c = col + i
        for dr, dc in dirs:
            nr = row + dr
            nc = c + dc
            if 0 <= nr < MAX_ROW and 0 <= nc < MAX_COL:
                if lines[nr][nc] in symbols:
                    return True
    return False

checked = set()
tot = 0
for row, rowvals in enumerate(lines):
    for col, item in enumerate(lines[row]):
        if item.isdigit() and (row, col) not in checked:
            checked.add((row, col))
            number = ''
            i = 0
            while col + i < MAX_COL and lines[row][col+i].isdigit():
                number += lines[row][col+i]
                checked.add((row, col+i))
                i += 1
            if next_to_symbol(row, col, number):
                tot += int(number)
print(tot)

#part 2
#basically rewrote everything here lol I should have checked symbols instead of numbers in part 1

def get_adj_nums(row, col):
    checked = set()
    adj_num = []
    for dr, dc in dirs: #look in all directions
        nr = row + dr
        nc = col + dc
        start = nc 
        #get to the starting digit of a number if we look in a direction and see a digit
        if 0 <= nr < MAX_ROW and 0 <= nc < MAX_COL and (nr, nc) not in checked and lines[nr][nc].isdigit():
            while start - 1 >= 0 and lines[nr][start - 1].isdigit():
                start -= 1
            #scan in the number and marked down that we checked these positions
            number = ''
            i = 0
            while start + i < MAX_COL and lines[nr][start + i].isdigit():
                checked.add((nr, start + i))
                number += lines[nr][start + i]
                i += 1
            if number is not '':
                adj_num.append(int(number))
    return adj_num


tot = 0
for row, rowvals in enumerate(lines):
    for col, item in enumerate(lines[row]):
        if item == '*':
            adj_nums = get_adj_nums(row, col)
            if len(adj_nums) == 2:
                prod = 1
                for num in adj_nums:
                    prod *= num
                tot += prod
print(tot)
