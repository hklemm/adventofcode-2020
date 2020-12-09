
import re

'''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
'''

def verify_yr(byr, min_yr, max_yr):
    if len(byr) != 4:
        return False
    elif (int(byr) < min_yr) or (int(byr)>max_yr):
        return False
    else:
        return True

    
def verify_byr(byr):
    return verify_yr(byr, 1920, 2002)

def verify_iyr(byr):
        return verify_yr(byr, 2010, 2020)

def verify_eyr(byr):
        return verify_yr(byr, 2020, 2030)
    

def verify_hgt(hgt):
    if hgt.endswith('cm'):
        hgt = int(hgt[:-2])
        if 150 <= hgt <= 193:
            return True
        else:
            return False
    elif hgt.endswith('in'):
        hgt = int(hgt[:-2])
        if 59 <= hgt <= 76:
            return True
        else:
            return False
    else:
        return False

def verify_hcl(hcl):
    if len(hcl) == 7 and hcl.startswith('#'):
        res = re.match('[0-9abcdef]*', hcl[1:])
        return res.group() == hcl[1:]
    else:
        return False


def verify_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def verify_pid(pid):
    res = re.match('[0-9]{9}', pid)
    if res is None:
        return False
    else:
        return res.group() == pid

def verify_cid(cid):
    return True


def verify_passport(passport):
    fields = ['byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid']

    verification_dict = {'byr' : verify_byr,
                         'eyr' : verify_eyr,
                         'iyr' : verify_iyr,
                         'hgt' : verify_hgt,
                         'hcl' : verify_hcl,
                         'ecl' : verify_ecl,
                         'pid' : verify_pid,
                         'cid' : verify_cid,
                         }

    
    if len(passport) < 7:
        return False
    else:
        result = True
        for field in fields:
            try:
                entry = passport[field]
                verifier = verification_dict[field]
                result = result and verifier(entry)
            except KeyError:
                result = False
        return result



with open('input.txt', 'r') as f:
    lines = f.readlines()

passports = []

current_passport = {}
for line in lines:
    line = line.strip()
    if len(line) == 0:
        passports.append(current_passport)
        current_passport = {}
    else:
        ll = line.split()
        ldict = {i.split(':')[0] : i.split(':')[1] for i in ll}
        current_passport.update(ldict)
passports.append(current_passport)

valids = 0
invalids = 0

for passport in passports:
    res = verify_passport(passport)
    if res:
        valids += 1
    else:
        invalids += 1
print('Valids: %d, Invalids: %d'%(valids, invalids))
