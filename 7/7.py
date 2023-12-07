from functools import cmp_to_key

with open('input.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

def count_chars(string):
    counts = {}
    for c in string:
        if c in counts: 
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def get_hand_value(hand):
    counts = count_chars(hand)

    if len(counts) == 1: # five of a kind
        return 6
    elif len(counts) == 2: 
        if 4 in counts.values():
            return 5 #four of a kind
        else:
            return 4 #full house 
    elif len(counts) == 3:
        if 3 in counts.values():
            return 3 #3 of a kind
        else:
            return 2 #two pair
    elif len(counts) == 4:
        return 1 #one pair
    else:
        return 0 #high card

def compare(a, b, part2 = False):
    card1, (value1, bid1) = a
    card2, (value2, bid2) = b

    if value1 > value2: 
        return 1
    elif value1 < value2:
        return -1
    else:
        order = '23456789TJQKA'
        if part2:
            order = 'J23456789TQKA'
        value = {val: i for i, val in enumerate(order)}

        for c1, c2 in zip(card1, card2):
            if value[c1] > value[c2]:
                return 1
            elif value[c1] < value[c2]:
                return -1
        return 0

hands = {}
for line in lines:
    cards, bid = line.split(' ')
    hands[cards] = (get_hand_value(cards), int(bid))

hands = dict(sorted(hands.items(), key = cmp_to_key(compare)))

tot = 0
for i, val in enumerate(hands.items()):
    bid = val[1][1]
    tot += (i + 1) * bid
print(tot)

#part 2
hands = {}
cardtypes = '23456789TQKA'
for line in lines:
    cards, bid = line.split(' ')
    max_value = 0
    if 'J' in cards:
        temp = cards
        for new in cardtypes:
            wildcard = temp.replace('J', new)
            value = get_hand_value(wildcard)
            if value > max_value:
                max_value = value
        hands[cards] = (max_value, int(bid))
    else:
        hands[cards] = (get_hand_value(cards), int(bid))

hands = dict(sorted(hands.items(), key = cmp_to_key(lambda x, y: compare(x, y, part2 = True))))
tot = 0
for i, val in enumerate(hands.items()):
    bid = val[1][1]
    tot += (i + 1) * bid
print(tot)
