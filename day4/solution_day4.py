with open('input.txt', 'r') as f:
#with open('test.txt', 'r') as f:
    lines = f.readlines()

passports = []

current_passport = []
for line in lines:
    line = line.strip()
    if len(line) == 0:
        passports.append(current_passport)
        current_passport = []
    else:
        current_passport.extend(line.split())
passports.append(current_passport)
    

valids = 0
invalids = 0

valid = False
candidate = False

for passport in passports:
    valid = False
    
    if len(passport) < 7:
        valid = False
    elif len(passport) == 8:
        valid = True
    elif len(passport) == 7:
        if any([i.startswith('cid') for i in passport]):
            valid = False
        else:
            valid = True
    #print(passport, valid)
    if valid:
        valids += 1
    else:
        invalids += 1

print('Valids: %d, Invalids: %d'%(valids, invalids))


