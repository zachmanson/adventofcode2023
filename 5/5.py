with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

seeds = [int(x) for x in lines[0].split(':')[1].split(' ') if x.isdigit()]
seeds2 = seeds
maps = [[] for x in range(7)]
i = 0
for line in lines[2:]:
    if not line.endswith('map:') and line != '':
        maps[i].append([int(x) for x in line.split(' ') if x.isdigit()])
    if line == '':
        i += 1


#ranges in full input are too big to store everything in lists
#only keep track of where the seeds move 
for m in maps:
    mapping = []
    for seed in seeds:
        default = True #flag for if mapping to self
        for dest, src, rnge in m:
            # if seeds mapping is not default
            if src <= seed < src + rnge:
                mapping.append(seed - src + dest) 
                default = False
                break
        # if it is default, it just keeps the same value
        if default:
            mapping.append(seed)
    seeds = mapping

print(min(seeds)) #part 1

seeds = [(seeds2[i], seeds2[i] + seeds2[i + 1]) for i in range(0, len(seeds2), 2)]
for m in maps:
    mapping = []
    while len(seeds) > 0:
        seed_start, seed_end = seeds.pop(0)
        default = True
        for dest, src, rnge in m:
            overlap_start = max(seed_start, src) #where does seed range overlaps source to dest range
            overlap_end = min(seed_end, src + rnge)
            if overlap_start < overlap_end: #if overlap exists
                mapping.append((overlap_start - src + dest, overlap_end - src + dest))
                default = False
                if overlap_start > seed_start: #put the ranges that were not in the overlap back 
                    seeds.append((seed_start, overlap_start)) #appending to seeds because we need to check this still
                if overlap_end > seed_end:
                    seeds.append((seed_end, overlap_end))
        if default:
            mapping.append((seed_start, seed_end))
    seeds = mapping

print(min(min(seeds)))
