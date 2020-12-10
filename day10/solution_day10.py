import numpy as np


#data = np.loadtxt('test.txt')
data = np.loadtxt('input.txt')


stack_order = np.sort(data)
all_jolts = np.hstack(([0], stack_order, [stack_order[-1]+3]))
jolt_diff = all_jolts[1:] - all_jolts[:-1]

three_jolt = np.sum(jolt_diff == 3)
one_jolt = np.sum(jolt_diff == 1)

res= three_jolt*one_jolt
print('The solution to problem one is: %d'%res)

one_tracks = []
track = 0
for t in jolt_diff:
    if t == 1:
        track+=1
    else:
        one_tracks.append(track)
        track = 0


trans = {4 : 7,
         3 : 4,
         2 : 2,
         1 : 1,
         0 : 1}

poss = [trans[i] for i in one_tracks]
res = np.cumprod(poss)[-1]

print('The solution to the second question is: %d'%res)


