import numpy as np

data = np.loadtxt('input.txt')
data = np.sort(data)

for i in data:
    r = 2020 - i
    if r in data:
        print ('The winning numbers are: ', i, r, i*r)
        break


    
for i in data[:40]:
    for k in data[:40]:
        for l in data[:40]:
            if i+k+l == 2020:
                print ('Solution to part 2 is:', i,k,l, i*k*l)
                break
