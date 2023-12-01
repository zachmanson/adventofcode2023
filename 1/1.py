with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]


tot = 0
for line in lines:
    digits = [x for x in line if x.isdigit()]
    digits = [digits[0], digits[-1]]
    together = ''.join(digits)
    tot += int(together)

print(tot)


#part 2

numbers_dict = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'zero' : 0}

tot = 0
for line in lines:
    for i in range(len(line)):
        for name, val in numbers_dict.items():
            if line[i:].startswith(name):
                line = line[:i] + str(val) + line[i+1:]

    digits = [x for x in line if x.isdigit()]
    digits = [digits[0], digits[-1]]
    together = ''.join(digits)
    tot += int(together)

print(tot)

