import sys
import numpy as np

def get_max_size(board,start_r,end_r,start_col,end_col,limit):

    counter = 0
    min_val = 1000
    max_val = 0

    if(start_r == end_r or start_col == end_col):
        return 0

    for r in range(start_r,end_r):
        for c in range(start_col,end_col):
            if(board[r,c] > max_val):
                max_val = board[r,c]
            if(board[r,c] < min_val):
                min_val = board[r,c]
    
            if(max_val - min_val > limit):
                case1 = get_max_size(board,start_r,end_r,start_col,end_col-1,limit)
                case2 = get_max_size(board,start_r,end_r,start_col+1,end_col,limit)
                case3 = get_max_size(board,start_r,end_r-1,start_col,end_col,limit)
                case4 = get_max_size(board,start_r+1,end_r,start_col,end_col,limit)
                return max(case1,case2,case3,case4)

            counter+=1
    
    return counter

# data = sys.stdin.readlines()

fo = open("circuit_board.txt", "r")
data = fo.readlines()
t = int(data[0].strip())

i = 1
test = 1

while i < len(data):
    p = list(map(int, data[i].strip().split(" ")))
    R = p[0]
    C = p[1]
    K = p[2]

    i+=1
    board = list()
    for j in range(i,i+R):
        board.append(list(map(int, data[i].strip().split(" "))))
        np_board = np.array(board)
        i+=1
    res = get_max_size(np_board,0,R,0,C,K)
    print("Case #"+str(test)+": "+str(res))
    test +=1