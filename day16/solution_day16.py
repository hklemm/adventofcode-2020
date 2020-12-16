with open('input.txt' ,'r') as f:
    lines = f.readlines()

    
def test_ticket(ticket, rules):
    """ Checks if a ticket is valid according to the rules"""
    valid = True

    invalids = []
    for t in ticket:
        valid_rule = False
        for n, rule in rules.items():
            if (rule[0][0]<=t<=rule[0][1]) or (rule[1][0]<=t<=rule[1][1]):
                valid_rule=True
        if not valid_rule:
            invalids.append(t)
        valid = valid & valid_rule
    return valid, invalids

# Read the data
    
my_ticket_line = False
ticket_section = False
rules = {}
tickets = []
for line in lines:
    if line.startswith('your ticket'):
        my_ticket_line = True
    elif my_ticket_line:
        my_ticket = [int(i) for i in line.strip().split(',')]
        my_ticket_line = False
    elif line.startswith('nearby tickets'):
        ticket_section = True
    elif ticket_section:
        ticket = [int(i) for i in line.strip().split(',')]
        tickets.append(ticket)
    elif line.find(' or ')>0:
        l = line.strip().split(': ')
        ranges = l[1].split(' or ')
        rules[l[0]] = [[int(i) for i in ranges[0].split('-')],
                       [int(i) for i in ranges[1].split('-')],]
    else:
        continue

# get the valid tickets

all_invalids = []
valid_tickets = []
for t in tickets:
    valid, invalids = test_ticket(t, rules)
    if not valid:
        all_invalids.extend(invalids)
    else:
        valid_tickets.append(t)

print (all_invalids, sum(all_invalids))

# sort out which field contains which info.
# we assume for each field that i could be anywhere.
# If we then find a ticket where the rule is violated for one entry,
# we chuck it out.

hopefuls = { rule : list(range(len(rules))) for rule in rules}

for ticket in valid_tickets:
    for i,t in enumerate(ticket):
        for n, rule in rules.items():
            if (rule[0][0]<=t<=rule[0][1]) or (rule[1][0]<=t<=rule[1][1]):
                continue
            else:
                try:
                    hopefuls[n].remove(i)
                except ValueError:
                    continue


# Now that we know which info could be stored in which line,
# we distill this information by taking out the entries with only one
# possibility.

taken_rows = []
ticket_code = {}

while len(hopefuls) > 0:    
    for h, l in hopefuls.items():
        if len(l) == 1:
            taken_rows.extend(l)
            ticket_code[h] = l[0]
            hopefuls.pop(h)
            break
    print(h, l)
    for ll in hopefuls.values():
        try:
            ll.remove(l[0])
        except ValueError:
            continue
        
departure_items = [i for i in ticket_code.keys() if i.startswith('departure')]
res=1
for i in departure_items:
    res*=my_ticket[ticket_code[i]]
print('Result 2: ',res)
