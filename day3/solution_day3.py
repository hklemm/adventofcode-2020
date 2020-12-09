with open('input.txt', 'r') as f:
    forest = f.readlines()

forest = [i.strip() for i in forest]


def traverse_forest(forest, step_right, step_down):
    trees = 0
    grass = 0

    position = 0
    period = len(forest[0])
    
    for line in forest[::step_down]:
        if line[position] == '#':
            trees += 1
        else:
            grass += 1
        position = (position + step_right)%period
    return trees, grass


angles = [[1,1], [3,1], [5,1], [7,1], [1,2]]

result = 1
for sr, sd in angles:
    trees, grass = traverse_forest(forest, sr, sd)
    result*=trees
    print(trees, grass, result)

print('Overall result: %d'%result)
