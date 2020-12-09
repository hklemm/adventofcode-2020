with open('input.txt', 'r') as f:
    d = f.readlines()

data = []
for line in d:
    l = line.strip()
    l = l.split()
    ll = [int(k) for k in l[0].split('-')] + [l[1][0]] + [l[2]]
    data.append(ll)

valid = 0
invalid = 0

for line in data:
    rmin = line[0]
    rmax = line[1]
    n = line[3].count(line[2])
    if rmin <=n <=rmax:
        valid += 1
    else:
        invalid += 1

print('Number of valid passwords: %d, number of invalid passwords: %d'%(valid, invalid))
        

new_valid = 0
new_invalid = 0
for line in data:
    ind0 = line[0]
    ind1 = line[1]
    letter = line[2]
    pwd = line[3]
    if (pwd[ind0-1] == letter) & (pwd[ind1-1] == letter): 
        new_invalid+=1
    elif (pwd[ind0-1] == letter) & (pwd[ind1-1] != letter):
        #print(line)
        new_valid += 1
    elif (pwd[ind0-1] != letter) & (pwd[ind1-1] == letter):
        new_valid +=1
    else:
        new_invalid +=1

print('Number of invalid passwords, with new rules: %d'%new_invalid)
