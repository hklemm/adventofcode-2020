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
    color_book[container.strip()] = [re.sub('[0-9]', '', i).strip() for i in one_rule]


shiny_containers = []

possibles = []

for bag,rule in color_book.items():
    if 'shiny gold' in rule:
        shiny_containers.append(bag)
        possibles.append(bag)

for bag in possibles:
    for container, rule in color_book.items():
        if bag in rule:
            possibles.append(container)
    
print('Solution, Problem 1:', len(set(possibles)))
