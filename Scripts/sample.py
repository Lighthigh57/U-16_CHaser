import CHaser # 同じディレクトリに CHaser.py がある前提

def main():
    value = [] # フィールド情報を保存するリスト
    client = CHaser.Client() # サーバーと通信するためのインスタンス

    while(True):
        value = client.get_ready() # サーバーに行動準備が完了したと伝える
        value = client.search_left() # サーバーに行動内容を伝える

        value = client.get_ready() # 行動する前には必ず get_ready() する
        if value[7] != 2:
            value = client.walk_down()
        else:
            value = client.put_up()

        value = client.get_ready()
        value = client.look_up()

        value = client.get_ready()
        value = client.put_right()

"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    main()