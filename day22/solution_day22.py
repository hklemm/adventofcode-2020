import copy
# fname = 'test.txt'
# fname = 'test2.txt'
fname = 'input.txt'
with open(fname, 'r') as f:
    lines = f.readlines()

deck1 = []
deck2 = []
p = None
for line in lines:
    if line.startswith('Player 1'):
        p = 1
        continue
    elif line.startswith('Player 2'):
        p = 2
        continue
    elif ((p == 1) and line[0].isdigit()):
        deck1.append(int(line.strip()))
    elif ((p == 2) and line[0].isdigit()):
        deck2.append(int(line.strip()))
    else:
        continue

d1 = copy.copy(deck1)
d2 = copy.copy(deck2)
    
def play_combat(deck1, deck2):
    while (len(deck1) > 0) and (len(deck2) > 0):
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)
    if len(deck1)> 0:
        return deck1, 1
    else:
        return deck2, 2


    
def play_recursive_combat(deck1, deck2):
    print('New Sub Round')
    deck_combos = []
    round = 0
    while (len(deck1) > 0) and (len(deck2) > 0):
        round+=1
        if ((deck1, deck2) in deck_combos):
            print('Recursion Stop triggered!')
            return deck1, 1

        deck_combos.append((deck1[:], deck2[:]))            
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 <= len(deck1) and c2 <= len(deck2):
            print ('c1 = %d, c2 = %d, starting sub round'%(c1, c2))
            d1 = deck1[:c1]
            d2 = deck2[:c2]
            d, p = play_recursive_combat(d1, d2)
            print('Player %d won sub-round'%p)
            if p == 1:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)

        elif c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)
    if len(deck1)> 0:
        return deck1, 1
    else:
        return deck2, 2


def calc_score(deck):
    res = 0
    for i, c in enumerate(deck[::-1], 1):
        res += i*c
    print('The result is: %d'%res)
    return res
    
winner, player = play_combat(deck1, deck2)
res1 = calc_score(winner)


winner,player= play_recursive_combat(d1, d2)
res=calc_score(winner)
print('Result, part 1: ', res1)
print('Result, part 2: ', res)

