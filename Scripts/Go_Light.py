import random
import Command

ready_value = [] # フィールド情報を保存するリスト
runner = None


def main():
    global ready_value
    global runner
    while True:
        ready_value = runner.get_info()
        rival_Checker()
    

def rival_Checker():
    """
    敵いたら潰します(笑)
    """
    global ready_value
    global runner

    for i in range(0,9):
        if ready_value[i] == 1:
            if i%2==0:
                pass
            else:
                runner.move("put",i)
                break
    else:
        runner.move("look",1)
    
    


"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    runner = Command.Command()
    main()