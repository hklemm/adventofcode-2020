import itertools
import numpy as np
import scipy.ndimage as sn
with open('input.txt', 'r') as f:
#with open('test.txt') as f:
    lines = f.readlines()

def embed(arr):
    new_shape = [i+2 for i in arr.shape]
    new_arr = np.zeros(new_shape, dtype=int)
    slicer = tuple([slice(1,-1)]*len(new_shape))
    #new_arr[1:-1,1:-1,1:-1] = arr
    new_arr[slicer] = arr
    return new_arr


start = []
for l in lines:
    start.append([int(i) for i in l.strip().replace('.', '0').replace('#','1')])

dcube = len(start)
start = np.asarray(start).reshape(dcube,dcube,1)
cube = start.copy()

pattern = np.ones((3,3,3))
cube = embed(cube)

cube4d = start.copy()
cube4d = cube4d.reshape(dcube,dcube,1,1)
pattern4d = np.ones((3,3,3,3))
cube4d = embed(cube4d)


for i in range(6):
    rc = sn.convolve(cube, pattern, mode='constant', cval=0)
    res = np.zeros_like(rc)
    res[(cube==0)&(rc==3)] = 1
    res[(cube==1)&((rc==4)|(rc==3))] = 1
    cube = embed(res)

    rc4d = sn.convolve(cube4d, pattern4d, mode='constant', cval=0)
    res4d = np.zeros_like(rc4d)
    res4d[(cube4d==0)&(rc4d==3)] = 1
    res4d[(cube4d==1)&((rc4d==4)|(rc4d==3))] = 1
    cube4d = embed(res4d)

print(res.sum(), res4d.sum())
