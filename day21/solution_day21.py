with open('input.txt', 'r') as f:
    lines = f.readlines()

foods = {}
possibilities = {}
rpossibilities = {}
uniques = {}

contents={}

for line in lines:
    line = line.strip()
    f, a = line.split('(contains')
    fs = f.split()
    alls = a[:-1].split(',')
    alls = [i.strip() for i in alls]
    foods[tuple(fs)] = alls
    for a in alls:
        foodies = uniques.setdefault(a, set())
        a_list = possibilities.setdefault(a, [])
        a_list.append(fs)
        foodies = foodies.union(set(fs))
        possibilities[a] = a_list
        uniques[a] = foodies
    for f in fs:
        f_list = rpossibilities.setdefault(f, set())
        f_list = f_list.union(alls)
        rpossibilities[f] = f_list

not_allergen = []
allergens = []



for a in possibilities.keys():
    ingredients = list(possibilities[a])

    for ingredient in uniques[a]:
        inthere = [ingredient in i for i in ingredients]
        if all(inthere):
            allergens.append((ingredient, a))
        else:
            not_allergen.append((ingredient,a))

all_allergens = set([i[0] for i in allergens])
all_ingredients = set(rpossibilities.keys())

not_allergen = all_ingredients.difference(all_allergens)

res = 0
for ing in not_allergen:
    for f in foods.keys():
        if ing in f:
            res+=1
print(res)

allergen_map = {}
for i in allergens:
    l = allergen_map.setdefault(i[0], [])
    l.append(i[1])

clist = {}
ing_list = list(all_allergens)

while len(ing_list) > 0:
    for ing in ing_list:
        if len(allergen_map[ing]) == 1:
            the_allergen = allergen_map.pop(ing)[0]
            clist[the_allergen] = ing
            for a in allergen_map.values():
                if the_allergen in a:
                    a.remove(the_allergen)

            break

    ing_list.remove(ing)

k = sorted(list(clist.keys()))
res = ','.join([clist[i] for i in k])
print(res)