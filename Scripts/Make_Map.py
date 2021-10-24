class Make_map():
    """
    Map生成します。
    MAPという名前のリストを使ってる。
    """

    MAP = []
    """記録中のマップ"""

    MX; MY
    """座標"""

    def __init__(self) -> None:
        global MAP
        global MY
        global MX

        MAP = [[" " for i in range(33)] for j in range(33)]
        MX = 0
        MY = 0


    def UpData(self, com, dir, get):
        global MX
        global MY   
        global MAP

        X = 0
        Y = 0
        R = 0

        print("UpdateData実行")

        if str(com) == "G":
            print("GetReadyのデータで更新")
            if MX - 1 < 0:
                print("Xのデータを修正")
                Y = 0
                for i in range(35):
                    for i in range(-1 * MX + 1):
                        MAP[Y].insert(0, "")
                    Y = Y + 1

                Y = 0
                for i in range(35):
                    for i in range(-1 * MX + 1):
                        del MAP[Y][33]
                    Y = Y + 1
                MX = -1 * MX + 1

            if MY - 1 < 0:
                print("Yのデータを修正")
                for i in range(-1 * MY + 1):
                    MAP.insert(0, ["" for i in range(35)])
                for i in range(-1 * MY + 1):
                    del MAP[35]
                MY = -1 * MY + 1

            print("get_ready()で更新中...")
            X = MX - 1
            Y = MY - 1
            R = 0
            for i in range(3):
                for j in range(3):
                    MAP[Y][X] = get[R]
                    X = X + 1
                    R = R + 1
                X = MX - 1
                Y = Y + 1

        elif str(com) == "S":
            print("Searchのデータで更新")
            if dir == "U":
                if MY - 9 < 0:
                    print("Yのデータを修正")
                    for i in range(-1 * MY + 9):
                        MAP.insert(0, ["" for i in range(35)])

                    for i in range(-1 * MY + 9):
                        del MAP[35]
                    MY = -1 * MY + 9

                print("Searchの上の情報で更新中...")
                X = MX
                Y = MY - 1
                R = 0
                for i in range(9):
                    MAP[Y][X] = get[R]
                    Y = Y - 1
                    R = R + 1

            if dir == "D":
                print("Searchの下の情報で更新中...")
                X = MX
                Y = MY + 1
                R = 0
                for i in range(9):
                    MAP[Y][X] = get[R]
                    Y = Y + 1
                    R = R + 1
                
            if dir == "L":
                if MX - 9 < 0:
                    print("Xのデータを修正")
                    Y = 0
                    for i in range(35):
                        for i in range(-1 * MX + 9):
                            MAP[Y].insert(0, "")
                        Y = Y + 1

                    Y = 0
                    for i in range(35):
                        for i in range(-1 * MX + 9):
                            del MAP[Y][33]
                        Y = Y + 1
                    MX = -1 * MX + 9

                print("Searchの左の情報で更新中...")
                X = MX - 1
                Y = MY
                R = 0
                for i in range(9):
                    MAP[Y][X] = get[R]
                    X = X - 1
                    R = R + 1
        
            if dir == "R":
                print("Searchの右の情報で更新中...")
                X = MX + 1
                Y = MY
                R = 0
                for i in range(9):
                    MAP[Y][X] = get[R]
                    X = X + 1
                    R = R + 1
            
        elif str(com) == "L":
            print("Lookのデータで更新")
            if dir == "U":
                if MX - 3 > 0:
                    print("Xのデータを修正")
                    Y = 0
                    for i in range(35):
                        for i in range(-1 * MX + 3):
                            MAP[Y].insert(0, "")
                        Y = Y + 1

                    Y = 0
                    for i in range(35):
                        for i in range(-1 * MX + 3):
                            del MAP[Y][33]
                        Y = Y + 1
                    MX = -1 * MX + 3
                
                if MY - 1 > 0:
                    for i in range(-1 * MY + 1):
                        MAP.insert(0, ["" for i in range(35)])

                    for i in range(-1 * MY + 1):
                        del MAP[35]
                    MY = -1 * MY + 1

                print("Lookの上のデータで更新中...")
                X = MX - 1
                Y = MY - 3
                R = 0
                for i in range(3):
                    for i in range(3):
                        MAP[Y][X] = get[R]
                        X = X + 1
                    X = MX - 1
                    Y = Y + 1

            if dir == "D":
                print("Lookの下のデータで更新中...")
                X = MX - 1
                Y = MY + 3
                R = 0
                for i in range(3):
                    for i in range(3):
                        MAP[Y][X] = get[R]
                        X = X + 1
                    X = MX - 1
                    Y = Y + 1
            
            if dir == "L":
                if MX - 3 > 0:
                    print("Xのデータを修正")
                    Y = 0
                    for i in range(35):
                        for i in range(-1 * MX + 3):
                            MAP[Y].insert(0, "")
                        Y = Y + 1

                    Y = 0
                    for i in range(35):
                        for i in range(-1 * MX + 3):
                            del MAP[Y][33]
                        Y = Y + 1
                    MX = -1 * MX + 3

                if MY - 1 > 0:
                    for i in range(-1 * MY + 1):
                        MAP.insert(0, ["" for i in range(35)])

                    for i in range(-1 * MY + 1):
                        del MAP[35]
                    MY = -1 * MY + 1

                print("Lookの左のデータで更新中...")
                X = MX - 3
                Y = MY - 1
                R = 0
                for i in range(3):
                    for i in range(3):
                        MAP[Y][X] = get[R]
                        X = X + 1
                    X = MX - 3
                    Y = Y + 1

            if dir == "R":
                print("Lookの右のデータで更新中...")
                X = MX + 3
                Y = MY - 1
                R = 0
                for i in range(3):
                    for i in range(3):
                        MAP[Y][X] = get[R]
                        X = X + 1
                    X = MX - 3
                    Y = Y + 1

        print("更新完了")