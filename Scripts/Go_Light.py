import Command

ready_value = [] # フィールド情報を保存するリスト
priority = [0,0,0,0,0,0,0,0,0] #
runner = None


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

    for i in range(0,9):
        if ready_value[i] == 3:
            if i%2==1:
                priority[i] = 1
        elif ready_value[i] == 1:
            if i%2==0:
                avoid_enemy(i)
            else:
                runner.move("put",i)
                break
        elif ready_value[i] == 2:
            priority[i] = -1
            pass
    else:
        max = 1
        for i in range(3,8,2):
            if priority[max] < priority[i]:
                max = i
        runner.move("walk",max)
    
    
    


"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    runner = Command.Command()
    main()