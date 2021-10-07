import random
import Command

#PlayerName = Light

priority = []
map_Data = [[0]*15]*17  # save map [x][y]
run = None  # instance of CHaser cliant
CENTER_X = 8  # Center in Map_X
CENTER_Y = 9  # Center in Map_Y
nowx = CENTER_X  # Setpivot for Map_X
nowy = CENTER_Y  # Setpivot for Map_Y
last = 0


def main():
    global run
    global priority

    last = 0
    while True:
        priority = [0]*9
        last = Checker(last,command.get_ready())

def solve_diagonal(target,com):
    """
    敵から逃げるには?
    """
    global priority

    if target < 3:
        y = 1
    else:
        y = 7

    if target == 0 or target == 6:
        x = 3
    else:
        x = 5

    if com == "avoid":
        priority[x] = -1
        priority[y] = -1
    else:
        priority[x] += 1
        priority[y] += 1

def Checker(last,ready_Value):
    """
    敵いたら潰します(笑)
    """
    global run
    global priority
    
    for i in range(0, 9):
        if ready_Value[i] == 3:
            if i % 2 == 1:
                priority[i] += 2
            else:
                solve_diagonal(i,"get")
        if ready_Value[i] == 1:
            if i % 2 == 0:
                solve_diagonal(i,"avoid")
            else:
                command.move("put", i)
                break
        if ready_Value[i] == 2:
            priority[i] = -1
    
    max = priority[1]  # 最大値
    nowmax = [1]  # 最大値のある方向
    for i in range(3, 8, 2):
        if max < priority[i]:
            max = priority[i]
            nowmax = [i]
        elif max == priority[i]:
            nowmax += [i]

    if len(nowmax) != 1:
        if ((last == 1) and (7 in nowmax)):
            nowmax.remove(7)
        elif ((last == 3) and (5 in nowmax)):
            nowmax.remove(5)
        elif ((last == 5) and (3 in nowmax)):
            nowmax.remove(3)
        elif ((last == 7) and (1 in nowmax)):
            nowmax.remove(1)
    if max == -1:
        command.move("look", 1)
        return 0
    else:
        goto = nowmax[random.randint(0, len(nowmax) - 1)]
        command.move("walk", goto)
    return goto

#-----Didn't use-----
if __name__ == "__main__":
    command = Command.Command()
    main()
