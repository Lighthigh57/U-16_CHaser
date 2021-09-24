import Command
import random
#CHaser　ユーザー名 = Shun

ready_value = [] # フィールド情報を保存するリスト
result = []
priority = []#
mapdata = [[0]*15]*17
infoOK = False
runner = None
last = 0
centerx = 8
centery = 9


def main():
    global ready_value
    global runner
    global priority
    global nowy 
    global result

    ready_value = runner.get_info()
    result = move("search",1)
    print(result)
    while True:
        ready_value = runner.get_info()
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
        global runner
        global infoOK

        result = []

        if infoOK == False:
            get_info()
            print("Warning!:You didn't get_info().")

        if com == "put":
            if dir == 1:
                result = runner.put_up()
                
            if dir == 7:
                result = runner.put_down()
                
            if dir == 3:
                result = runner.put_left()
                
            if dir == 5:
                result = runner.put_right()
                
        if com == "walk":
            if dir == 1:
                result = runner.walk_up()
                
            if dir == 7:
                result = runner.walk_down()
                
            if dir == 3:
                result = runner.walk_left()
                
            if dir == 5:
                result = runner.walk_right()
                
        if com == "look":
            if dir == 1:
                result = runner.look_up()
                
            if dir == 7:
                result = runner.look_down()
                
            if dir == 3:
                result = runner.look_left()
                
            if dir == 5:
                result = runner.look_right()
                
        if com == "search":
            if dir == 1:
                result = runner.search_up()
                
            if dir == 7:
                result = runner.search_down()
                
            if dir == 3:
                result = runner.search_left()
                
            if dir == 5:
                result = runner.search_right()
        
        print(com+" "+str(dir))
        infoOK = False

        return result    
    
def get_info(self):
        global runner
        global infoOK

        infoOK = True
        return runner.get_ready()    


"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    runner = Command.Command()
    main()
