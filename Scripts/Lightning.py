import random
import Command

#PlayerName = Light

priority = []
"""priority = 優先度"""

run = None
"""instance of Command class"""

last = 0
"""last direction"""

side = 0
"""My Cliant's side"""

map = None
"""Map on firld"""

CHECK_ZONE = 15
"""Interval of Map_Check"""

def main():
    global run
    global priority

    turn = 0
    last = 0
    while True:
        priority = [0]*9
        last = Checker(last, run.get_ready(), turn)
        turn += 1

def map_Check(map):
    """マップを調べて取り残さない"""
    pass

def solve_diagonal(target, com):
    """斜めに物が見えた時の処理"""
    global priority
    if target < 3:  # Where this is for X
        y = 1
    else:
        y = 7
    if target == 0 or target == 6:  # Where this is for X
        x = 3
    else:
        x = 5
    if com == "avoid":  # if this is enemy
        priority[x] = -1
        priority[y] = -1
    else:  # if this is item
        priority[x] += 1
        priority[y] += 1


def Checker(last, ready_Value, turn) -> int:
    """
    敵いたら潰します(笑)
    """
    global run
    global priority
    if turn>0 and turn % CHECK_ZONE:
        map_Check(run.get_map())
    else:
        pass

    for i in range(0, 9):  # Safe Command
        if ready_Value[i] == 3:  # Can I get now?
            if i % 2 == 1:
                priority[i] += 1
            else:
                solve_diagonal(i, "get")

    else:  # Danger Command
        for i in range(0, 9):
            if ready_Value[i] == 1:  # Can I put there now?
                if i % 2 == 0:
                    solve_diagonal(i, "avoid")
                else:
                    run.move("put", i)
                    break
            if ready_Value[i] == 2:  # There is a block?
                priority[i] = -1

    max = priority[1]  # maximum value
    nowmax = [1]  # direction index who it has maximum

    # find maximum value in priority list(look like search sort)
    for i in range(3, 8, 2):
        if max < priority[i]:
            max = priority[i]
            nowmax = [i]
        elif max == priority[i]:
            nowmax += [i]

    if len(nowmax) != 1:  # remove last place
        if ((last == 1) and (7 in nowmax)):
            nowmax.remove(7)
        elif ((last == 3) and (5 in nowmax)):
            nowmax.remove(5)
        elif ((last == 5) and (3 in nowmax)):
            nowmax.remove(3)
        elif ((last == 7) and (1 in nowmax)):
            nowmax.remove(1)
    if max == -1:  # I should go to Danger Zone!!!
        run.move("look", 1)
        return 0
    else:
        goto = nowmax[random.randint(0, len(nowmax) - 1)]

        run.move("walk", goto)
    return goto


if __name__ == "__main__":
    while(True):
        side = int(input("please tell me hot or cool... (cool->0 / hot->1) :"))
        if side == 0 or side == 1:
            break
        else:
            print("you have to enter 0 or 1!")

    run = Command.Command()  # Set Command instance
    main()