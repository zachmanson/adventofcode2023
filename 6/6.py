with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

times = [int(x) for x in lines[0].split(':')[1].split(' ') if x.isdigit()]
distances = [int(x) for x in lines[1].split(':')[1].split(' ') if x.isdigit()]

def hold_button(t, totaltime):
    return t * (totaltime - t)

result = 1
for maxt, maxd in zip(times, distances):
    count = 0
    for t in range(maxt):
        d = hold_button(t, maxt)
        if d > maxd:
            count += 1
    result *= count
print(result)

#part 2
time = int(''.join([str(x) for x in times]))
distance = int(''.join([str(x) for x in distances]))
count = 0
for t in range(time):
    d = hold_button(t, time)
    if d > distance:
        count += 1
print(count)
