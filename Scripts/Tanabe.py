import random

import CHaser

#PlayerName = Shun

ready_Value = []
priority = []
map_Data = [[0]*15]*17  # save map [x][y]
ready_OK = False  # getready?
run = None  # instance of CHaser
CENTER_X = 8  # Center in Map_X
CENTER_Y = 9  # Center in Map_Y
nowx = CENTER_X  # Setpivot for Map_X
nowy = CENTER_Y  # Setpivot for Map_Y


def main():
    global ready_Value
    global run
    global priority

    ready_Value = get_info()
    result = move("search", 1)
    last = 0
    print(result)
    while True:
        ready_Value = get_info()
        priority = [0]*9
        Checker(last)

def avoid_enemy(target):
    """
    敵から逃げるには?
    """
    global priority

    if target < 3:
        priority[1] = -1
    else:
        priority[7] = -1

    if target == 0 or target == 6:
        priority[3] = -1
    else:
        priority[5] = -1

def Checker(last):
    """
    敵いたら潰します(笑)
    """
    global ready_Value
    global run
    global priority

    for i in range(0, 9):
        if ready_Value[i] == 3:
            if i % 2 == 1:
                priority[i] = 1
        if ready_Value[i] == 1:
            if i % 2 == 0:
                avoid_enemy(i)
            else:
                move("put", i)
                break
        if ready_Value[i] == 2:
            priority[i] = -1
    else:
        max = priority[1]  # 最大値
        nowmax = [1]  # 最大値のある方向
        for i in range(3, 8, 2):
            if max < priority[i]:
                max = priority[i]
                nowmax = [i]
            elif max == priority[i]:
                nowmax += [i]
        else:
            if len(nowmax) != 1:
                if ((last == 1) and (7 in nowmax)):
                    nowmax.remove(7)
                if ((last == 3) and (5 in nowmax)):
                    nowmax.remove(5)
                if ((last == 5) and (3 in nowmax)):
                    nowmax.remove(3)
                if ((last == 7) and (1 in nowmax)):
                    nowmax.remove(1)
            if max == -1:
                move("look", 1)
            else:
                goto = nowmax[random.randint(0, len(nowmax) - 1)]
                move("walk", goto)
            last = goto

def move(com, dir):
    """
    各種行動を起こします。
    Get_info忘れないで！
    """
    global run
    global ready_OK

    if ready_OK == False:
        get_info()
        print("Warning!:You didn't get_info().")

    if com == "put":
        if dir == 1:
            result = run.put_up()
        if dir == 7:
            result = run.put_down()
        if dir == 3:
            result = run.put_left()
        if dir == 5:
            result = run.put_right()

    if com == "walk":
        if dir == 1:
            result = run.walk_up()
        if dir == 7:
            result = run.walk_down()
        if dir == 3:
            result = run.walk_left()
        if dir == 5:
            result = run.walk_right()

    if com == "look":
        if dir == 1:
            result = run.look_up()
        if dir == 7:
            result = run.look_down()
        if dir == 3:
            result = run.look_left()
        if dir == 5:
            result = run.look_right()

    if com == "search":
        if dir == 1:
            result = run.search_up()
        if dir == 7:
            result = run.search_down()
        if dir == 3:
            result = run.search_left()
        if dir == 5:
            result = run.search_right()

    print(com+" "+str(dir))
    ready_OK = False

    return result

def get_info():
    """Get_readyをします。"""
    global run
    global ready_OK

    ready_OK = True
    return run.get_ready()

def move_map(dir):
    """Mapの現在地の移動
    global map_Data
    if dir == 1:
        map_Data = map_Data[1:]+[[0]*5]
    elif dir == 7:
        map_Data = [[0]*9] + map_Data[:-1]
    else:
        map_Data = [list(x) for x in zip(*map_Data)]
        if dir == 3:
            map_Data = map_Data[1:]+[[0]*5]
        else:
            map_Data = [[0]*9] + map_Data[:-1]
        map_Data = [list(x) for x in zip(*map_Data)]
    print(map_Data)"""

def set_map(get):
    """Map更新
    global map_Data

    for i in range(-1, 2):
        for j in range(-1, 2):
            if get[(i+1)*3+(j+1)] == 2:
                d = 2
            else:
                d = 1
            map_Data[nowy+i, nowx+j] = d
    print(map_Data)
    """

if __name__ == "__main__":
    run = CHaser.Client()
    main()
