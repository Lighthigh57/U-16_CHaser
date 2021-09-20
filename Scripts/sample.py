import CHaser # 同じディレクトリに CHaser.py がある前提
import random

"""
このファイルを直接実行したときに実行する関数．
実行するまでの経緯はファイルの下部に記載．


"""
def main():
    value = []
    client = CHaser.Client()

    while(True):
        value = client.get_ready()
        value = client.search_left()

        number = random.randint(0, 3)
        if number == 0:
            client.walk_up()
        elif number == 1:
            client.walk_down()
        elif number == 2:
            client.walk_left()
        elif number == 3:
            client.walk_right()
        """
        value = client.get_ready()
        if value[7] != 2:
            value = client.walk_down()
        else:
            value = client.put_up()

        value = client.get_ready()
        value = client.look_up()

        value = client.get_ready()
        value = client.put_right()

        """
        

"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    main()