

import numpy as np

data = np.loadtxt('input.txt')

max_offset = 25


def test_alphabet(alphabet, d):
    for i in alphabet:
        if d-i in alphabet:
            return True
    return False

for i,d in enumerate(data[max_offset:], start=max_offset):
    alphabet = data[i-max_offset:i]
    res = test_alphabet(alphabet, d)
    # print (i, d, res)
    if not res:
        break

# desired_result = 217430975
desired_result = d
print('Result for part 1 is: %d'%desired_result)

ind = 0
starting_point=0
last_point = 0
dsum = data[starting_point]
found_sequence = False
while not found_sequence:
    ind+=1
    dsum+=data[ind]
    # print(ind, dsum)
    if dsum == desired_result:
         print(starting_point, ind)
         found_sequence = True
    if dsum > desired_result:
        starting_point += 1
        ind = starting_point
        dsum = data[starting_point]
        


assert data[starting_point:ind+1].sum() == desired_result
# data[470:487].sum() - desired_result

dd = data[starting_point:ind+1]

n0 = dd.min()
n1 = dd.max()

print ('The result is :', n0 + n1)
