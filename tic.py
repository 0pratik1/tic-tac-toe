import random
lis = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
l1=[]
def grid():
    for i in range(3):
        for j in range(5):
            if(j==1 or j==3):
                lis[i][j]="|"
            else:
                lis[i][j]=" "
def display():
    for i in range(3):
        for j in range(5):
            print(lis[i][j],end=" ")
        print("\n__________")

def insert_move(move):
    for i in range(3):
        for j in range(5):
            if(move==j and move<5):
                lis[0][j]="X"
            if (move-6== j and 5<move <11):
                lis[1][j] = "X"
            if (move-12== j and 11<move <17 ):
                lis[2][j] = "X"
def insert_comp(move):
    for i in range(3):
        for j in range(5):
            if(move==j and move<5):
                lis[0][j]="O"
            if (move-6== j and 5<move <11):
                lis[1][j] = "O"
            if (move-12== j and 11<move <17 ):
                lis[2][j] = "O"
def winning():
    if(lis[0][0]==lis[0][2] ==lis[0][4]!=" "):
        if(lis[0][0]=="X"):
            print("Congrats!,You Won")
            return False
        elif(lis[0][0]=="O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    elif (lis[1][0] == lis[1][2]== lis[1][4] !=" "):
        if (lis[1][0] == "X"):
            print("Congrats!,You Won")
            return False
        elif (lis[1][0] == "O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    elif (lis[2][0] == lis[2][2] == lis[2][4] !=" "):
        if (lis[1][0] == "X"):
            print("Congrats!,You Won")
            return False
        elif (lis[1][0] == "O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    elif(lis[0][0]==lis[1][0] ==lis[2][0]!=" " ):
        if (lis[1][0] == "X"):
            print("Congrats!,You Won")
            return False
        elif (lis[1][0] == "O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    elif (lis[0][2] == lis[1][2]  == lis[2][2]!=" " ):
        if (lis[1][2] == "X"):
            print("Congrats!,You Won")
            return False
        elif (lis[1][2] == "O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    elif (lis[0][4] == lis[1][4] == lis[2][4]!=" " ):
        if (lis[1][4] == "X"):
            print("Congrats!,You Won")
            return False
        elif (lis[1][4] == "O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    elif(lis[0][0]==lis[1][2]==lis[2][4] !=" "):
        if (lis[2][4] == "X"):
            print("Congrats!,You Won")
            return False
        elif (lis[2][4] == "O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    elif(lis[0][4]==lis[1][2] ==lis[2][0] !=" "):
        if (lis[1][2] == "X"):
            print("Congrats!,You Won")
            return False
        elif (lis[1][2] == "O"):
            print("Oops,YOU LOSS")
            return False
        else:
            return True
    else:
        return True
def computer_input():
    p=random.randint(1,9)
    while(l1.count(p)!=0):
        p=random.randint(1,9)
    return p

# if __name__ == '__main__':

grid()
display()

k=0
while(winning() or k==0):
    print("enter pos to procced")
    m=int(input())
    if(l1.count(m)==0):
        l1.append(m)
        insert_move(2*m-2)
        k=k+1
    else:
        print("enter valid position")
        m = int(input())
        l1.append(m)
        insert_move(2 * m - 2)
        k=k+1
    # display()


    o=computer_input()
    l1.append(o)
    insert_comp(2 * o - 2)
    display()
    k = k + 1
    # o = random.randint(1, 9)
    # if(l1.count(o)==0):
    #     l1.append(o)
    #     insert_comp(2*o-2)
    #     display()
    # else:
    #     o=random.randint(1,9)
    #     l1.append(o)
    #     insert_comp(2 * o - 2)
    #     display()
    if(k==9):
        print("MATCH DRAW,TRY AGAIN")
        break



