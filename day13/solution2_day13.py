import numpy as np

#Python program for Extended Euclidean algorithm
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)



def find_chinese_multiples(data):
    """Given a list or an array of tuples [(a0,m0), (a1,m1), (a2,m2) ...], 
    this algorithm finds a number x, so that for each element of the tuple:
    
    x = a0 mod(m0)
    x = a1 mod(m1)
    x = a2 mod(m2)
    ...

    This is called Chinese Remainder Theorem on Wikipedia, where I also
    got the idea for the algorithm.

    """
    data = data.tolist() #Make sure we have python ints for arbitrary precision
    a1, m1 = data[0]

    for ak, mk in data[1:]:
        _, n1, nk= egcd(m1, mk)
        x = a1*mk*nk + ak*m1*n1        
        a = m1*mk
        if x < 0:
            mult = -x//a + 1
            x = x + a*mult
        else:
            x = x - (x//a)*a # We do things modulo the whole shebang)
        a1 = x
        m1 *= mk

    return x, a


            
# Example from Wikipedia to see if my algo works
example = np.array(((0,3),(3,4),(4,5)))

# First bus example
t2 = '67,7,59,61'
example = np.array(((0,67),(1,7),(2,59),(3,61)))
#example = np.array(((0,7),(1,13),(4,59),(6,31), (7,19)))

ee = example.copy()
ee[:,0] = (example[:,1] - example[:,0])%example[:,1]

t2 = '67,7,59,61'
t3 = '67,x,7,59,61'
t4 = '67,7,x,59,61'
t5 = '1789,37,47,1889'

tests = [t2,t3,t4,t5]

tas = []

ttests = []

for t in tests:
    # print(t)
    busses = t.strip().replace('x','nan')
    busses = np.fromstring(busses, sep=',')
    print(busses)
    dta = []
    for i,b in enumerate(busses):
        if np.isfinite(b):
            dta.append((i, int(b)))
    dta=np.asarray(dta)
    tas.append(np.asarray(dta))
    ee = dta.copy()
    ee[:,0] = (dta[:,1] - dta[:,0])
    ee[0,0] = 0
    ttests.append(ee)


with open('input.txt', 'r') as f:
    data = f.readlines()

time = int(data[0].strip())

busses = data[1].strip().replace('x','nan')
busses = np.fromstring(busses, sep=',')

dt = np.ceil(time/busses)*busses - time
i = np.nanargmin(dt)
res = dt[i]*busses[i]
print('Result 1: %f'%res)

dta = []
for i,b in enumerate(busses):
    if np.isfinite(b):
        dta.append((i, int(b)))
dta=np.asarray(dta)
ee = dta.copy()
ee[:,0] = (dta[:,1] - dta[:,0])
ee[0,0] = 0

tfinal = ee
res = [754018, 779210, 1261476, 1202161486]

for t,r in zip(ttests, res):
    print (find_chinese_multiples(t)[0] - r)


res = find_chinese_multiples(tfinal)
print('The solution to part 2 is:%d'%res[0])
