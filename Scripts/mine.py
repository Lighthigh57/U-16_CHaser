import random
import Command

ready_value = [] # フィールド情報を保存するリスト
runner = None


def main():
    global ready_value
    global runner
    while(True):
        ready_value = runner.get_info()
        for i in range(1,8,2):
            if ready_value[i] == 1:
                runner.move("put",i)
                break
        else:
            check=True
            while check:
                result = random.randint(0,3)
                if ready_value[result] != 2:
                    move("walk",result*2+1)
                    check = False



"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    runner = Command.Command()
    main()