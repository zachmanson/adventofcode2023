from functools import lru_cache

with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

def get_candidates(s):
    if s == '?':
        return [',', '#']
    else:
        return s

@lru_cache(maxsize = None)
def count_combinations(springs, groups, group_size = 0):
    if len(springs) == 0: #if we are at the end springs
        if len(groups) == 0 and group_size == 0:
            return 1
        else:
            return 0
    
    count = 0
    #check one at a time
    candidates = get_candidates(springs[0]) 
    for c in candidates:
        if c == '#': #start counting groups
            count += count_combinations(springs[1:], groups, group_size + 1)
        else: #if we get a period
            if group_size > 0:
                if len(groups) > 0 and groups[0] == group_size: #if we have counted enough for a group
                    count += count_combinations(springs[1:], groups[1:], group_size = 0)
            else: #two periods in a row
                count += count_combinations(springs[1:], groups, group_size = 0) #move to next

    return count

tot = 0
totp2 = 0
for line in lines:
    springs, groups = line.split(' ')
    groups = [int(x) for x in groups.split(',')]
    #adding . to the end of springs is easier for checking the end of the string
    tot += count_combinations(tuple(springs + '.'), tuple(groups)) #need to pass in tuple for lru_cache
    totp2 += count_combinations(tuple(((springs + '?') * 5)[:-1] + '.'), tuple(groups * 5))

print(tot)
print(totp2)
