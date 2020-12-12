import numpy as np
with open('input.txt', 'r') as f:
    lines = f.readlines()


direction = {'N':0,
             'E' : 90,
             'S' : 180,
             'W' : 270}

rdirection = {0 : 'N',
              90 : 'E',
              180 : 'S',
              270 : 'W'}


def count(inst, num, current_pos):
    if inst == 'N':
        pos = current_pos + (0,num)    
    elif inst == 'E':
        pos = current_pos + (num, 0)
    elif inst == 'S':
        pos = current_pos + (0,-num)
    elif inst == 'W':
        pos = current_pos + (-num, 0)
    else:
        raise (ValueError, 'WTF?')
    return pos
        

def drive(inst, num, current_pos, current_heading):
    if inst == 'F':
        heading = current_heading
        pos = count(heading, num, current_pos)
    elif inst == 'R':
        deg = direction[current_heading]
        heading = rdirection[(deg+num)%360]
        pos = current_pos
    elif inst == 'L':
        deg = direction[current_heading]
        heading = rdirection[(deg-num)%360]
        pos = current_pos
    else:
        pos= count(inst, num, current_pos)
        heading = current_heading
    return pos, heading

def set_waypoint(inst, num, waypoint):

    def rot_r(waypoint):
        return np.array((waypoint[1],-waypoint[0])) 

    def rot_l(waypoint):
        return np.array((-waypoint[1],waypoint[0])) 

    
    if inst == 'R':
        # Rotate Waypoint clockwise
        rots = num/90
        for i in range(int(rots)):
            waypoint = rot_r(waypoint)
    elif inst == 'L':
        # Rotate Waypoint clockwise
        rots = num/90
        for i in range(int(rots)):
            waypoint = rot_l(waypoint)  
    elif inst == 'N' :
        waypoint[1] += num
    elif inst == 'E' :
        waypoint[0] += num
    elif inst == 'S' :
        waypoint[1] -= num
    elif inst == 'W' :
        waypoint[0] -= num
    return waypoint
            

insts = []
pos = np.array([0,0])
heading = 'E'
for line in lines:
    i0 = line[0]
    i1 = int(line.strip()[1:])
    insts.append((i0, i1))
    
    pos, heading = drive(i0, i1, pos, heading)

print('The solution to part 1 is :',np.abs(pos).sum())


waypoint = np.array((10,1))
wps = [waypoint]
pos = np.array([0,0])
heading = 'E'
for line in insts:
    i0 = line[0]
    i1 = line[1]

    if i0 == 'F':
        pos += i1*waypoint
    else:
        waypoint = set_waypoint(i0, i1, waypoint)
    wps.append(waypoint)
    print(line, waypoint, pos)
        
print('The solution to part 2 is :',np.abs(pos).sum())
