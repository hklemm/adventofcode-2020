import itertools
import numpy as np
with open('input.txt', 'r') as f:
    lines = f.readlines()


def embed(arr):
    new_shape = [i+2 for i in arr.shape]
    new_arr = np.zeros(new_shape, dtype=int)
    new_arr[1:-1,1:-1,1:-1] = arr
    return new_arr
    
def gen_neighbours(i,j,k, shape):
    combos = []
    for m,n in enumerate((i,j,k)):
        nmax = shape[m] - 1        
        if ((n>0) and (n<nmax)):
            il = [n-1, n, n+1]
        elif n==0:
            il = [n, n+1]
        elif n==nmax:            
            il = [n, n-1]
        combos.append(il)
    res=list(itertools.product(*combos))
    res.remove((i,j,k))
    return res

            
def cycle(arr):

    embedding = embed(arr)
    res = np.zeros_like(embedding)
    the_shape = res.shape
    for i in range(the_shape[0]):
        for j in range(the_shape[1]):
            for k in range(the_shape[2]):
                inds = gen_neighbours(i,j,k,the_shape)
                state = embedding[i,j,k]
                nvals = [embedding[ind] for ind in inds]
                nstate = sum(nvals)
                if (state == 1) and ((nstate==2) or (nstate==3)):
                    res[i,j,k]=1
                elif (state == 0) and (nstate==3):
                    res[i,j,k] = 1
                else:
                    res[i,j,k] = 0
                # if k == 1:
                #     print ('i = ', i, 'j = ', j,'state =', state, 'nstate =',  nstate, 'res =', res[i,j,k])

    return res
                    
    
    

start = []
for l in lines:
    start.append([int(i) for i in l.strip().replace('.', '0').replace('#','1')])

start = np.asarray(start).reshape(8,8,1)
cube = start.copy()

for i in range(6):
    cube = cycle(cube)

print('Solution to part 1:', cube.sum())
    
######################################################## Part 2 ##################################################
def embed_4d(arr):
    new_shape = [i+2 for i in arr.shape]
    new_arr = np.zeros(new_shape, dtype=int)
    new_arr[1:-1,1:-1,1:-1,1:-1] = arr
    return new_arr
    
def gen_neighbours_4d(i,j,k,l, shape):
    combos = []
    
    for m,n in enumerate((i,j,k,l)):
        nmax = shape[m] - 1        
        if ((n>0) and (n<nmax)):
            il = [n-1, n, n+1]
        elif n==0:
            il = [n, n+1]
        elif n==nmax:            
            il = [n, n-1]
        combos.append(il)
    res=list(itertools.product(*combos))
    res.remove((i,j,k,l))
    return res

            
def cycle_4d(arr):

    embedding = embed_4d(arr)
    res = np.zeros_like(embedding)
    the_shape = res.shape
    for i in range(the_shape[0]):
        for j in range(the_shape[1]):
            for k in range(the_shape[2]):
                for l in range(the_shape[3]):
                    inds = gen_neighbours_4d(i,j,k,l,the_shape)
                    state = embedding[i,j,k,l]
                    nvals = [embedding[ind] for ind in inds]
                    nstate = sum(nvals)
                    if (state == 1) and ((nstate==2) or (nstate==3)):
                        res[i,j,k,l]=1
                    elif (state == 0) and (nstate==3):
                        res[i,j,k,l] = 1
                    else:
                        res[i,j,k,l] = 0
                    # if k == 1:
                    #     print ('i = ', i, 'j = ', j,'state =', state, 'nstate =',  nstate, 'res =', res[i,j,k])

    return res
                    
with open('input.txt', 'r') as f:
    lines = f.readlines()

start = []
for l in lines:
    start.append([int(i) for i in l.strip().replace('.', '0').replace('#','1')])

start = np.asarray(start).reshape(len(start),len(start),1,1)

cube = start.copy()

for i in range(6):
    cube = cycle_4d(cube)

print('Solution to part 2:', cube.sum())
