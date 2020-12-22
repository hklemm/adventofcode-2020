import re

with open('input.txt','r') as f:
    lines = f.readlines()


def construct_re(rule, rule_book):
    exp = rule_book[rule].strip()
    if exp.startswith('"'):
        ex = exp.replace('"','')
        return ex
    else:
        ex = exp.split()
        re = []
        for r in ex:
            if r.isdigit():
                re.append(construct_re(int(r), rule_book))
            else:
                re.append(r)
    return re
            
def create_re_string(exp, re = ''):
    for i in exp:
        if type(i) == list:
            rere = create_re_string(i, '')
            re = re + '(' + rere + ')'

        elif (i.isalpha()) or i == '|':
            re = re+i
        else:
            raise ValueError('How did you get here?')
    return re

    
    
rules = {}
data = []
    
data_section = False
for line in lines:
    line = line.strip()
    if line == '':
        data_section = True
        continue
    if data_section:
        data.append(line)
    else:
        line = line.split(':')
        rules[int(line[0])] = line[1].strip()




rule_0 = construct_re(0, rules)
o_string = create_re_string(rule_0)

res=0

for i in data:
    m = re.match(o_string, i)
    if m:
        if m.group() == i:
            res +=1
print('Solution to part 1: %d'%res)

# Part 2

exp_rules = {}

for i in rules:
    r = construct_re(i, rules)
    exp_rules[i] = create_re_string(r)

# Modify the rules
'''
8: 42 | 42 8
11: 42 31 | 42 11 31
'''

rule_42 = construct_re(42, rules)
string42 = create_re_string(rule_42)


rule_31 = construct_re(31, rules)
string31 = create_re_string(rule_31)
a = exp_rules[8]
rule_8 = '(('+a+')+)'


res = 0
matches = []

for i in range(1,max(len(x) for x in data)):
        rule_11 = f"(({string42})){{{i}}}({string31}){{{i}}}"
        pattern = f"^{rule_8}({rule_11})$"
        for entry in data:
            if re.match(pattern, entry):
                matches.append(entry)
                res +=1
print('Solution to part 2 is: %d', res)

