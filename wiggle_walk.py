import sys

# memory limit exceed
def GetPositionV0(N,R,C,SR,SC,moves):

    matrix = [["" for x in range(C)] for y in range(R)] 
    
    matrix[SR-1][SC-1] = "X"

    for i in range(N):

        if(moves[i]=="N"):
            while matrix[SR-1][SC-1] == "X":
                SR -= 1

        elif(moves[i]=="S"):
            while matrix[SR-1][SC-1] == "X":
                SR +=1
        elif(moves[i]=="E"):
            while matrix[SR-1][SC-1] == "X":
                SC+=1
        elif(moves[i]=="W"):
            while matrix[SR-1][SC-1] == "X":
                SC-=1
        
        matrix[SR-1][SC-1] = "X"
    
    return SR,SC

# replace matrix by set to optimize space
def GetPosition(N,R,C,SR,SC,moves):
    mem = set()
    mem.add(str(SR-1)+":"+str(SC-1))

    for i in range(N):

        if(moves[i]=="N"):
            while  str(SR-1)+":"+str(SC-1) in mem:
                SR -= 1
        elif(moves[i]=="S"):
            while str(SR-1)+":"+str(SC-1) in mem:
                SR +=1
        elif(moves[i]=="E"):
            while str(SR-1)+":"+str(SC-1) in mem:
                SC+=1
        elif(moves[i]=="W"):
            while str(SR-1)+":"+str(SC-1) in mem:
                SC-=1
        
        mem.add(str(SR-1)+":"+str(SC-1))
    
    return SR,SC


# data = sys.stdin.readlines()

fo = open("wiggle_walk.txt", "r")
data = fo.readlines()
t = int(data[0].strip())

for i in range(1,len(data),2):
    p = list(map(int, data[i].strip().split(" ")))
    moves = data[i+1].strip()
    SR,SC =  GetPosition(p[0],p[1],p[2],p[3],p[4],moves)
    print("Case #"+str((i+1)//2)+": "+ str(SR) +" "+ str(SC))



