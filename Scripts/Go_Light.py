import Command
import random
#CHaser　ユーザー名 = Shun

ready_value = [] # フィールド情報を保存するリスト
priority = [0,0,0,0,0,0,0,0,0] #
runner = None
last = 0

def main():
    global ready_value
    global runner
    global priority
    while True:
        ready_value = runner.get_info()
        for i in range(0,9):
            priority[i] = 0
        Checker()

def avoid_enemy(target):
    """
    敵から逃げるには?
    """
    global priority

    if target == 0:
        priority[1] = -1
        priority[3] = -1
    else:
        if target == 2:
            priority[1] = -1
            priority[5] = -1
        else:
            if target == 6:
                priority[3] = -1
                priority[7] = -1
            else:
                priority[5] = -1
                priority[7] = -1    

def Checker():
    """
    敵いたら潰します(笑)
    """
    global ready_value
    global runner
    global priority
    global last

    for i in range(0,9):
        if ready_value[i] == 3:
            if i%2==1:
                priority[i] = 1
        if ready_value[i] == 1:
            if i%2==0:
                avoid_enemy(i)
            else:
                runner.move("put",i)
                break
        if ready_value[i] == 2:
            priority[i] = -1
    else:
        print(priority)
        max = priority[1]#最大値
        nowmax = [1]#最大値のある方向
        for i in range(3,8,2):
            if max < priority[i]:
                max = priority[i]
                nowmax = [i]
            elif max == priority[i]:
                nowmax += [i]
            print(nowmax)
            if len(nowmax) != 1:
                if ((last == 1) and (7 in nowmax)):
                    nowmax.remove(7)
                if ((last == 3) and (5 in nowmax)):
                    nowmax.remove(5)
                if ((last == 5) and (3 in nowmax)):
                    nowmax.remove(3)
                if ((last == 7) and (1 in nowmax)):
                    nowmax.remove(1)

        runner.move("walk",nowmax[random.randint(0,len(nowmax) - 1)])
        last = nowmax[random.randint(0,len(nowmax) - 1)]
    
    
    


"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    runner = Command.Command()
    main()