with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

cubes = {'red': 12, 'green' : 13, 'blue' : 14}

tot = 0
totp2 = 0
for line in lines:
    game_id = int(line.split(' ')[1][:-1])
    sets = line.split(':')[1].split(';')
    valid = True
    maxcounts = {'red' : 0, 'green' : 0, 'blue' : 0}
    for s in sets:
        colourcounts = {'red' : 0, 'green' : 0, 'blue' : 0}
        for countcolour in s.split(','):
            count = int(countcolour.split(' ')[1])
            colour = countcolour.split(' ')[2]
            colourcounts[colour] += count

            #part 2
            if count > maxcounts[colour]: 
                maxcounts[colour] = count

        for colour, maxval in cubes.items():
            if colourcounts[colour] > maxval:
                valid = False
                break
    if valid: 
        tot += game_id

    #part 2 product
    prod = 1
    for colour, count in maxcounts.items():
        prod *= count
    totp2 += prod
print(tot)
print(totp2)
