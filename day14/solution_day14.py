import re
import copy

def encode_mask(mask):
    the_mask = {}
    for i,p in enumerate(mask[::-1]):
        if p != 'X':
            the_mask[i] = p
    return the_mask
    

def apply_mask(number, mask):
    n = bin(int(number))[2:]
    mask_len = max(mask.keys())
    dlen = mask_len+1 - len(n)
    if dlen > 0:
        new_n = ''.join(['0']*dlen+[n])
    else:
        new_n = n
    new_n = list(new_n)
    for i,p in mask.items():
        new_n[-(i+1)] = p
    res = int(''.join(new_n),2)
    return res
    
# with open('input.txt', 'r') as f:
with open('test.txt', 'r') as f:  
    data = f.readlines()


mem = {}
mask = {}
    
for line in data:
    if line.startswith('mask'):
        m = line.strip()
        m = m.split(' = ')[1]
        the_mask = encode_mask(m)
    elif line.startswith('mem'):
        ll = line.strip().split(' = ')
        key=re.search('[0-9]+', ll[0])
        res = apply_mask(ll[1], the_mask)
        mem[int(key.group())] = res

res = sum(mem.values())

print('The result is %d'%res)

############################## Part 2 ################################

with open('input.txt', 'r') as f:  
    data = f.readlines()

mem = {}
def get_memory_addresses(mem_addr, mask):
    n = bin(int(mem_addr))[2:]
    mask_len = len(mask)
    dlen = mask_len - len(n)
    if dlen > 0:
        new_n = ''.join(['0']*dlen+[n])
    else:
        new_n = n
    new_n = list(new_n)
    floatings = []
    for i,p in enumerate(mask):
        if p == '0':
            continue
        elif p == '1':
            new_n[i] = p
        elif p == 'X':
            floatings.append(i)

    addresses = [new_n]
    #print(len(floatings))
    for i in floatings:
        new_addresses = []
        #print(len(addresses))
        for addr in addresses:
            n1 = copy.deepcopy(addr)
            n2 = copy.deepcopy(addr)
            n1[i] = '0'
            n2[i] = '1'
            new_addresses.append(n1)
            new_addresses.append(n2)
        #print('len new:', len(new_addresses))
        addresses = copy.deepcopy(new_addresses)

    addresses = [int(''.join(i),2) for i in addresses]
    return addresses


for line in data:
    if line.startswith('mask'):
        m = line.strip()
        m = m.split(' = ')[1]
        the_mask = m
    elif line.startswith('mem'):
        ll = line.strip().split(' = ')
        key=re.search('[0-9]+', ll[0]).group()
        addr_keys = get_memory_addresses(key, the_mask)
        for k in addr_keys:
            mem[k] = int(ll[1])
        
print('The solution to part 2 is:', sum(mem.values()))
