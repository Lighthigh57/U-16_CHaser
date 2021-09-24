import CHaser
import random
#CHaser　ユーザー名 = Shun

ready_value = [] # フィールド情報を保存するリスト
result = [] #コマンドで得たマップ情報
priority = [] #優先度
mapdata = [[0]*15]*17 #Map情報を保管
infoOK = False #getready済みか
run = None #コマンド実行者
last = 0 #
CENTER_X = 8 
CENTER_Y = 9
nowx = CENTER_X
nowy = CENTER_Y


def main():
    global ready_value
    global run
    global priority
    global result

    ready_value = get_info()
    result = move("search",1)
    print(result)
    while True:
        ready_value = get_info()
        priority = [0]*9
        Checker()

def avoid_enemy(target):
    """
    敵から逃げるには?
    """
    global priority

    if target<3:
        priority[1] = -1
    else:
        priority[7] = -1

    if target == 0 or target == 6:
        priority[3] = -1
    else:
        priority[5] = -1

def Checker():
    """
    敵いたら潰します(笑)
    """
    global ready_value
    global run
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
                move("put",i)
                break
        if ready_value[i] == 2:
            priority[i] = -1
    else:
        #print(priority)
        max = priority[1]#最大値
        nowmax = [1]#最大値のある方向
        for i in range(3,8,2):
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
                move("look",1)
            else:
                move("walk",nowmax[random.randint(0,len(nowmax) - 1)])
            last = nowmax[random.randint(0,len(nowmax) - 1)]

def move(com,dir):
        """
        各種行動を起こします。
        Get_info忘れないで！
        """
        global run
        global infoOK

        if infoOK == False:
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
        infoOK = False

        return result    
    
def get_info():
        global run
        global infoOK

        infoOK = True
        return run.get_ready()    


"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    run = CHaser.Client()
    main()
