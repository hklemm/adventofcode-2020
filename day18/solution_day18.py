import re
import copy
from bisect import bisect_left


with open('input.txt', 'r') as f:
    lines = f.readlines()
    

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError



def parse_eqn(eqn):
    operator = None
    constituents = eqn.split()
    for s in constituents:
        if s.isdigit():
            i = int(s)
            if operator == '+':
                res += i
            elif operator == '*':
                res *= i
            elif operator is None:
                res = i
            else:
                raise ValueError('Unknown Operator')
        
        elif s in ['+', '*']:
            operator = s
        elif s in ['(', ')']:
            raise ValueError('Bracket')
        else:
            continue
    return res


def parse_eqn_2(eqn):
    operator = None
    constituents = eqn.split()

    while '+' in constituents:
        i = constituents.index('+')
        b = constituents.pop(i+1)
        constituents.pop(i)
        constituents[i-1] = str(int(constituents[i-1]) + int(b))
        
    for s in constituents:
        if s.isdigit():
            i = int(s)
            if operator == '+':
                raise ValueError('illegal addition')
            elif operator == '*':
                res *= i
            elif operator is None:
                res = i
            else:
                raise ValueError('Unknown Operator')
        
        elif s in ['+', '*']:
            operator = s
        elif s in ['(', ')']:
            raise ValueError('Bracket')
        else:
            continue
    return res




def parse_string(eqn, parser):
    eqn = eqn.strip()
    open_brackets = [m.start() for m in re.finditer(r'\(', eqn)]
    close_brackets = [m.start() for m in re.finditer(r'\)', eqn)]

    res_parts = []
    
    while len(close_brackets)>0:
        #print (eqn)
        c = close_brackets.pop(0)
        o = find_lt(open_brackets, c)
        open_brackets.remove(o)
        #print (o, c)
        sub_eqn = eqn[o+1:c]
        #print(sub_eqn)
        res = parser(sub_eqn)        
        eqn = eqn[:o]+ str(res) + ' '*(c+1-o-len(str(res))) + eqn[c+1:]
        #print (eqn)
    res = parser(eqn)
    return res


res = [parse_string(i, parse_eqn) for i in lines]
print('Result Problem 1:', sum(res))
res2 = [parse_string(i, parse_eqn_2) for i in lines]
print('Result Problem 2:', sum(res2))
