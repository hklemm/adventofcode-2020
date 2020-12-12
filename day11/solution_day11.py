import numpy as np

with open('input.txt','r') as f:
    lines = f.readlines()

layout = [l.strip().replace('.','0').replace('L','1') for l in lines]

int_layout = np.asarray([[int(i) for i in l] for l in layout])

occupied  = np.zeros_like(int_layout)
occupied[0,0] = 1
new_occupation = np.zeros_like(occupied)

nrows, ncols = occupied.shape

def test_occupation(arr,i,k):

    ncols,nrows=arr.shape
    test_inds = [(i-1,k-1),(i-1,k),(i-1,k+1),(i,k-1),(i,k+1),(i+1,k-1),
                 (i+1,k),(i+1,k+1)]

    test = 0
    for t in test_inds:
        if (t[0] >=0) &  (t[1] >=0) &  (t[0] < ncols) &  (t[1] < nrows):
            test+=arr[t]
    return test


def test_occupation_lines(arr, i,k, debug=False):
    nc, nr = arr.shape
    # Get the visibility along the diagonal
    d = np.diag(arr,k-i)
    # There doesn't seem to be an easy way to get the "anti-diagonal"
    farr = np.fliplr(arr)
    fi, fk = i, arr.shape[1]-1-k
    dt = np.diag(farr, fk-fi)#[::-1]

    ul = d[:min(i,k)][::-1]
    lr = d[min(i,k)+1:] ######### errrr
    ur = dt[:min(fi,fk)][::-1]
    ll = dt[min(fi,fk)+1:]#[::-1]
    # print(arr, d, dt, ul, ur, ll, lr) 
    # 
    test_set = [arr[i+1:,k], arr[:i,k][::-1], arr[i,k+1:], arr[i,:k][::-1], ul, ur, ll, lr]
    if debug:
        print (d, dt)
        print ( 'down :', test_set[0])
        print ( 'up :', test_set[1])
        print ( 'right :', test_set[2])
        print ( 'left :', test_set[3])
        print ( 'upper left :', test_set[4])
        print ( 'upper right :', test_set[5])
        print ( 'lower left :', test_set[6])
        print ( 'lower right :', test_set[7])
    
    test_sum=0
    
    for t in test_set:
        if 1 in t:
            if 0 in t:
                p1 = np.argwhere(t== 1)
                p0 = np.argwhere(t== 0)
                if p1[0,0]<p0[0,0]:
                    test_sum+=1
                else:
                    continue
            else:
                test_sum+=1
        else:
            continue
    return test_sum




count = 0
while not (occupied == new_occupation).all():
    print(count)
    count +=1
    occupied = new_occupation.copy()
    for i in range(nrows):
        for k in range(ncols):
            if int_layout[i,k] >0:
                occ = test_occupation(occupied,i,k)
                if occupied[i,k] == 0:
                    if occ == 0:
                        new_occupation[i,k]=1
                    else:
                        new_occupation[i,k]=0
                elif occupied[i,k] == 1:
                    if occ <4:
                        new_occupation[i,k]=1
                    else:
                        new_occupation[i,k]=0
                else:
                    raise ValueError
    print (new_occupation)


print('The result for part 1 is: %d'%(occupied.sum()))


count = 0
occupations = []
occupied = int_layout.copy()
occupied -= 1
new_occupation = occupied.copy()
occupied[0,0] = 1
while not (occupied == new_occupation).all():
    print(count)
    count +=1
    occupied = new_occupation.copy()
    occupations.append(occupied)
    for i in range(nrows):
        for k in range(ncols):
            if int_layout[i,k] >0:
                occ = test_occupation_lines(occupied,i,k)
                if occupied[i,k] == 0:
                    if occ == 0:
                        new_occupation[i,k]=1
                    else:
                        new_occupation[i,k]=0
                elif occupied[i,k] == 1:
                    if occ <5:
                        new_occupation[i,k]=1
                    else:
                        new_occupation[i,k]=0
                else:
                    raise ValueError
    print (new_occupation)

occupied_seats = new_occupation
occupied_seats[occupied_seats<0] = 0
print('The second result is :', occupied_seats.sum())
