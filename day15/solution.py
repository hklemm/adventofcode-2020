'''
numbers = {i:[] for i in range(10)}

numbers[0].append(1)
numbers[3].append(2)
numbers[6].append(3)

num_spoken = 6

for turn in range(4, 9): #2021):
    n = numbers.get(num_spoken,[])
    if len(n) == 1:
        # we are new
        numbers[num_spoken].append(turn)
        print('append first time', num_spoken, turn)
        num_spoken = 0
    elif len(n)>1:
        print n
        new_num = n[-1] - n[-2]
        numbers[num_spoken].append(turn)
        print('append to list', num_spoken, turn, new_num)
        num_spoken = new_num
    elif len(n)==0:
        numbers[num_spoken] = [i]
        print('number spoken first time', num, i)
    else:
        raise(ValueError, 'How did you get here?')
    print ('Turn: %d, Spoken: %d'%(turn, num_spoken))
''' 

innumber = [2,1,3]
innumber = [1,0,16,5,17,4]
numbers = {}

for i, innum in enumerate(innumber, 1):
    print(i)
    turn=i
    number_spoken = innum
    numbers[number_spoken] = [turn]

for turn in range(len(innumber) + 1, 30000001):
    last_spoken = numbers.get(number_spoken, [])
    if len(last_spoken) == 1:
        number_spoken=0
        try:
            numbers[number_spoken].append(turn)
        except KeyError:
            numbers[number_spoken] = [turn]
    elif len(last_spoken)>1:
        number_spoken = last_spoken[-1] - last_spoken[-2]
        try:
            numbers[number_spoken].append(turn)
        except KeyError:
            numbers[number_spoken] = [turn]
    if turn%100000 == 0:
        print('Turn: %d, number spoken: %d'%(turn, number_spoken))
