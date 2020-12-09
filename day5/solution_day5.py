import numpy as np

with open('input.txt', 'r') as f:
#with open('test.txt', 'r') as f:   
    lines = f.readlines()

rows=[]
cols=[]
row_nos = []
col_nos = []
seat_id = []
for line in lines:
    row = line[:7].replace('F','0').replace('B','1')
    col = line[7:-1].replace('L','0').replace('R','1')
    row_no = int(row, 2)
    col_no = int(col, 2)
    rows.append(row)
    cols.append(col)
    row_nos.append(row_no)
    col_nos.append(col_no)
    seat_id.append(8*row_no + col_no)

seat_arr = np.asarray(seat_id)
seat_arr = np.sort(seat_arr)
diff_seat = seat_arr[1:] - seat_arr[:-1]
ind=np.argwhere(diff_seat==2)[0,0]
print(seat_arr[ind:ind+2])

print('Seat Id=%d'%(seat_arr[ind] + 1))
