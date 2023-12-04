with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

tot = 0
copies = [1 for x in range(len(lines))]
for game_idx, line in enumerate(lines):
    points = 0
    matches = 0
    game, data = line.split(':')
    winning_numbers, my_numbers = data.split('|')
    winning_numbers = [x for x in winning_numbers.split(' ') if x.isdigit()]
    my_numbers = [x for x in my_numbers.split(' ') if x.isdigit()]
    for n in my_numbers:
        if n in winning_numbers:
            matches += 1
    if matches > 0:
        points = 2**(matches - 1)
        #part 2
        for i in range(game_idx + 1, game_idx + matches + 1):
            copies[i] += copies[game_idx]
    tot += points

print(tot)
print(sum(copies))
