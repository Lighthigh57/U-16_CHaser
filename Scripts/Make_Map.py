class Make_map():
    """
    Map生成します。
    self.Mapという名前のリストを使ってる。
    """

    """座標"""

    def __init__(self) -> None:
        
        self.Map = [["" for i in range(35)] for j in range(35)]
        """保存したマップ"""

        self.mapX = 0
        """今のX座標（仮定）"""

        self.mapY = 0
        """今のY座標（仮定）"""


    def UpData(self, com, dir, get):

        x = 0
        y = 0
        r = 0

        print("UpdateData実行")

        if str(com) == "G":
            print("GetReadyのデータで更新")
            if self.mapX - 1 < 0:
                print("Xのデータを修正")
                y = 0
                for i in range(35):
                    for i in range(-1 * self.mapX + 1):
                        self.Map[y].insert(0, "")
                    y = y + 1

                y = 0
                for i in range(35):
                    for i in range(-1 * self.mapX + 1):
                        del self.Map[y][33]
                    y = y + 1
                self.mapX = -1 * self.mapX + 1

            if self.mapY - 1 < 0:
                print("Yのデータを修正")
                for i in range(-1 * self.mapY + 1):
                    self.Map.insert(0, ["" for i in range(35)])
                for i in range(-1 * self.mapY + 1):
                    del self.Map[35]
                self.mapY = -1 * self.mapY + 1

            print("get_ready()で更新中...")
            x = self.mapX - 1
            y = self.mapY - 1
            r = 0
            for i in range(3):
                for j in range(3):
                    self.Map[y][x] = get[r]
                    x = x + 1
                    r = r + 1
                x = self.mapX - 1
                y = y + 1

        elif str(com) == "S":
            print("Searchのデータで更新")
            if dir == "U":
                if self.mapY - 9 < 0:
                    print("Yのデータを修正")
                    for i in range(-1 * self.mapY + 9):
                        self.Map.insert(0, ["" for i in range(35)])

                    for i in range(-1 * self.mapY + 9):
                        del self.Map[35]
                    self.mapY = -1 * self.mapY + 9

                print("Searchの上の情報で更新中...")
                x = self.mapX
                y = self.mapY - 1
                r = 0
                for i in range(9):
                    self.Map[y][x] = get[r]
                    y = y - 1
                    r = r + 1

            if dir == "D":
                print("Searchの下の情報で更新中...")
                x = self.mapX
                y = self.mapY + 1
                r = 0
                for i in range(9):
                    self.Map[y][x] = get[r]
                    y = y + 1
                    r = r + 1
                
            if dir == "L":
                if self.mapX - 9 < 0:
                    print("Xのデータを修正")
                    y = 0
                    for i in range(35):
                        for i in range(-1 * self.mapX + 9):
                            self.Map[y].insert(0, "")
                        y = y + 1

                    y = 0
                    for i in range(35):
                        for i in range(-1 * self.mapX + 9):
                            del self.Map[y][33]
                        y = y + 1
                    self.mapX = -1 * self.mapX + 9

                print("Searchの左の情報で更新中...")
                x = self.mapX - 1
                y = self.mapY
                r = 0
                for i in range(9):
                    self.Map[y][x] = get[r]
                    x = x - 1
                    r = r + 1
        
            if dir == "R":
                print("Searchの右の情報で更新中...")
                x = self.mapX + 1
                y = self.mapY
                r = 0
                for i in range(9):
                    self.Map[y][x] = get[r]
                    x = x + 1
                    r = r + 1
            
        elif str(com) == "L":
            print("Lookのデータで更新")
            if dir == "U":
                if self.mapX - 3 > 0:
                    print("Xのデータを修正")
                    y = 0
                    for i in range(35):
                        for i in range(-1 * self.mapX + 3):
                            self.Map[y].insert(0, "")
                        y = y + 1

                    y = 0
                    for i in range(35):
                        for i in range(-1 * self.mapX + 3):
                            del self.Map[y][33]
                        y = y + 1
                    self.mapX = -1 * self.mapX + 3
                
                if self.mapY - 1 > 0:
                    for i in range(-1 * self.mapY + 1):
                        self.Map.insert(0, ["" for i in range(35)])

                    for i in range(-1 * self.mapY + 1):
                        del self.Map[35]
                    self.mapY = -1 * self.mapY + 1

                print("Lookの上のデータで更新中...")
                x = self.mapX - 1
                y = self.mapY - 3
                r = 0
                for i in range(3):
                    for i in range(3):
                        self.Map[y][x] = get[r]
                        x = x + 1
                    x = self.mapX - 1
                    y = y + 1

            if dir == "D":
                print("Lookの下のデータで更新中...")
                x = self.mapX - 1
                y = self.mapY + 3
                r = 0
                for i in range(3):
                    for i in range(3):
                        self.Map[y][x] = get[r]
                        x = x + 1
                    x = self.mapX - 1
                    y = y + 1
            
            if dir == "L":
                if self.mapX - 3 > 0:
                    print("Xのデータを修正")
                    y = 0
                    for i in range(35):
                        for i in range(-1 * self.mapX + 3):
                            self.Map[y].insert(0, "")
                        y = y + 1

                    y = 0
                    for i in range(35):
                        for i in range(-1 * self.mapX + 3):
                            del self.Map[y][33]
                        y = y + 1
                    self.mapX = -1 * self.mapX + 3

                if self.mapY - 1 > 0:
                    for i in range(-1 * self.mapY + 1):
                        self.Map.insert(0, ["" for i in range(35)])

                    for i in range(-1 * self.mapY + 1):
                        del self.Map[35]
                    self.mapY = -1 * self.mapY + 1

                print("Lookの左のデータで更新中...")
                x = self.mapX - 3
                y = self.mapY - 1
                r = 0
                for i in range(3):
                    for i in range(3):
                        self.Map[y][x] = get[r]
                        x = x + 1
                    x = self.mapX - 3
                    y = y + 1

            if dir == "R":
                print("Lookの右のデータで更新中...")
                x = self.mapX + 3
                y = self.mapY - 1
                r = 0
                for i in range(3):
                    for i in range(3):
                        self.Map[y][x] = get[r]
                        x = x + 1
                    x = self.mapX - 3
                    y = y + 1
        print(self.mapX,self.mapY)
        print("更新完了")