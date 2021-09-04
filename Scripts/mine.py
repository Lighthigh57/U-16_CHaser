import CHaser # 同じディレクトリに CHaser.py がある前提
import random
import Command

value = [] # フィールド情報を保存するリスト
client = None


def main():
    global value
    global client
    while(True):
        value = client.get_ready()
        for i in range(1,8,2):
            if value[i] == 1:
                command(i)
                break
        else:
            check=True
            while check:
                result = random.randint(0,3)
                if value[result] != 2:
                    command(result*2+1)
                    check = False


def command(target):

    """
    位置に合わせて関数実行
    """
    global value
    global client
    if target == 1:
        if value[target] == 1:
            client.put_up()
        else:
            client.walk_up()
    if target == 3:
        if value[target] == 1:
            client.put_left()
        else:
            client.walk_left()
    if target == 5:
        if value[target] == 1:
            client.put_right()
        else:
            client.walk_right()
    if target == 7:
        if value[target] == 1:
            client.put_down()
        else:
            client.walk_down()
"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    client = CHaser.Client()
    
    main()