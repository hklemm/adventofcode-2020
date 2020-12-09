import re

with open('input.txt','r') as f:
    rules = f.readlines()

containers = []
rule_book = {}
color_book = {}
    
for rule in rules:
    container, containee = rule.strip().split('bags contain')
    containers.append(container)
    one_rule = containee.rstrip('.').replace('bags', '').replace('bag', '').split(', ')
    #rule_book[container.strip()] = [re.sub('[0-9]', '', i).strip() for i in one_rule]
    counts = []
    for i in one_rule:
        i = i.strip()
        try:
            j = [int(i[0]), i[2:]]
        except ValueError:
            # print(i)
            j = [0, '']
        counts.append(j)
    rule_book[container.strip()] = counts

starting_bag = 'shiny gold'

bag_list = rule_book[starting_bag]

total_bags = 0
    

def traverse_bag_chain(rule_book, starting_bag):
    bag_count = -1
    res=[[1, starting_bag]]

    for bag in res:
        
        multiplier = bag[0]
        #print(bag, multiplier)
        rule = rule_book[bag[1]]
        #print(rule)
        if rule[0][0] != 0:
            bag_count+=multiplier
            rule = [[i[0]*multiplier, i[1]] for i in rule]
            res.extend(rule)
        else:
            bag_count+=multiplier
        #print (bag_count)
    return res, bag_count

res = traverse_bag_chain(rule_book, starting_bag)

print ('The result is %d'%res[1])









     
def factorialr(n):
    if n == 0:
        return 1
    else:
        return n*factorialr(n-1)
