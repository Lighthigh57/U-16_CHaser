#coding:utf-8

import CHaser # 同じディレクトリに CHaser.py がある前提
import random

map_x_size = 15
map_y_size = 17


class new_client(CHaser.Client):
    '''メインとなるクラス'''
    def __init__(self):
        # はじめにcoolかhotかを入力
        while(True):
            self.temp = int(input("please tell me hot or cool... (cool->0 / hot->1) :"))
            if self.temp == 0 or self.temp == 1:
                break
            else:
                print("you have to enter 0 or 1!")
        
        super(new_client, self).__init__()
        self.x = 0; self.y = 0 #座標指定
        self.field_map = [[-1 for i in range(15)] for j in range(17)]
        self.walked_map = [[0 for i in range(15)] for j in range(17)]
        self.value = []; self.view = {"?"," ","E","/","V","I"}
        self.before_move = 0
        self.next_move = 0
        self.ready = False
        self.unkmp = []
        self.nwalmp = []
        self.safe_map = []
        self.wall_pos = [1,3,5,7]

    def seek_nwal(self):
        """歩いてないところを隣接マス内から探す"""
        adjx = [self.x, self.x-1, self.x+1, self.x]
        adjy = [self.y-1, self.y, self.y, self.y+1]
        nwalmp = []
        for i in range(4):
            if adjx[i]<15 and adjx[i]>-1 and adjy[i]<17 and adjy[i]>-1:
                if self.field_map[adjy[i]][adjx[i]]!=2 and self.walked_map[adjy[i]][adjx[i]]==0:
                    nwalmp.append(dir_conv(adjx[i]-self.x, adjy[i]-self.y))
        print(f"隣接マスの中で情報の無いマスは{len(nwalmp)}個です")
        return nwalmp

    def seek_nwal_l(self, dirs):
        adjx = [self.x, self.x-1, self.x+1, self.x]
        adjy = [self.y-1, self.y, self.y, self.y+1]
        usex = []
        usey = []
        nwalnu = 0
        if self.value[dirs]==2:
            return 0
        elif dirs==1:
            usex = adjx
            usey = [i-2 for i in adjy]
        elif dirs==3:
            usex = [i-2 for i in adjx]
            usey = adjy
        elif dirs==5:
            usex = [i+2 for i in adjx]
            usey = adjy
        elif dirs==7:
            usex = adjx
            usey = [i+2 for i in adjy]
        for i in range(4):
            if usex[i]<15 and usex[i]>-1 and usey[i]<17 and usey[i]>-1:
                if self.field_map[usey[i]][usex[i]] != 2 and self.walked_map[usey[i]][usex[i]] == 0:
                    nwalnu += 1
        return nwalnu

    def isnwal(self, dirv):
        if len(self.seek_nwal()) > 0:
            for i in self.seek_nwal():
                if i == dirv:
                    return True
            return False
        else:
            return False


    def conv_map(self):
        gm = [["?" for i in range(15)] for j in range(17)]
        for i in range(len(self.field_map)):
            for j in range(len(self.field_map[i])):
                gm[i][j] = self.view[(self.field_map[i][j] + 1)]
        rtn = [""]*17
        c = 0
        csh = ""
        for l in gm:
            for b in l:
                csh += b
            rtn[c] = csh
            csh = ""
            c += 1
        return rtn

    def nget_ready(self):
        """get_readyして、周りの情報をマップに格納"""
        if not self.ready:
            print("getready now")
            self.value = self.get_ready()
            self.safe_map = []
            for i in range(1,8,2):
                if self.value[i] != 2:
                    self.safe_map.append(i)
            a = 0
            for i in range(3):
                for j in range(3):
                    print("value[{0}] = [{1}, {2}]".format(a, self.y+i-1, self.x+j-1))
                    if self.x+j-1<15 and self.x+j-1>-1 and self.y+i-1<17 and self.y+i-1>-1:
                        self.field_map[self.y+i-1][self.x+j-1] = self.value[a]
                    a += 1
            self.field_map[self.y][self.x] = 4
            self.walked_map[self.y][self.x] = 1
            print("Current map:")
            for u in self.conv_map():
                print(u)
            print("")
            for q in self.walked_map:
                print(q)
            self.ready = True
            self.check_enemy()
            return self.value
        else:
            print("getready重ね掛けなう")

    def nlook_up(self):
        self.value = self.look_up()
        a = 0
        for i in range(3):
            for j in range(3):
                # print("value[{0}] = [{1}, {2}]".format(a, self.y+i-1, self.x+j-1))
                if self.x+j-1<15 and self.x+j-1>-1 and self.y+i-3<17 and self.y+i-3>-1:
                    self.field_map[self.y+i-3][self.x+j-1] = self.value[a]
                a += 1
        return self.value

    def nlook_left(self):
        self.value = self.look_left()
        a = 0
        for i in range(3):
            for j in range(3):
                # print("value[{0}] = [{1}, {2}]".format(a, self.y+i-1, self.x+j-1))
                if self.x+j-3<15 and self.x+j-3>-1 and self.y+i-1<17 and self.y+i-1>-1:
                    self.field_map[self.y+i-1][self.x+j-3] = self.value[a]
                a += 1
        return self.value

    def nlook_right(self):
        self.value = self.look_right()
        a = 0
        for i in range(3):
            for j in range(3):
                # print("value[{0}] = [{1}, {2}]".format(a, self.y+i-1, self.x+j-1))
                if self.x+j+1<15 and self.x+j+1>-1 and self.y+i-1<17 and self.y+i-1>-1:
                    self.field_map[self.y+i-1][self.x+j+1] = self.value[a]
                a += 1
        return self.value

    def nlook_down(self):
        self.value = self.look_down()
        a = 0
        for i in range(3):
            for j in range(3):
                # print("value[{0}] = [{1}, {2}]".format(a, self.y+i-1, self.x+j-1))
                if self.x+j-1<15 and self.x+j-1>-1 and self.y+i+1<17 and self.y+i+1>-1:
                    self.field_map[self.y+i+1][self.x+j-1] = self.value[a]
                a += 1
        return self.value

    # 移動して、マップ格納リストの自分の位置を更新する
    def nwalk_up(self):
        self.value = self.walk_up()
        print("I walked to [{0}, {1}]→[{2}, {3}]".format(self.x, self.y, self.x, self.y-1))
        self.y -= 1
        return self.value

    def nwalk_left(self):
        self.value = self.walk_left()
        print("I walked to [{0}, {1}]→[{2}, {3}]".format(self.x, self.y, self.x-1, self.y))
        self.x -= 1
        return self.value

    def nwalk_right(self):
        self.value = self.walk_right()
        print("I walked to [{0}, {1}]→[{2}, {3}]".format(self.x, self.y, self.x+1, self.y))
        self.x += 1
        return self.value

    def nwalk_down(self):
        self.value = self.walk_down()
        print("I walked to [{0}, {1}]→[{2}, {3}]".format(self.x, self.y, self.x, self.y+1))
        self.y += 1
        return self.value

    #---引数に何か行動したい方向の数字入れるだけで動く 楽したい人向け関数とゆかいな仲間たち---

    def walk(self, dirv):
        if self.ready:
            if dirv == 1 and self.value[1] != 2:
                print("walk([{0}, {1}] → [{0}, {2}])".format(self.x, self.y, self.y-1))
                self.nwalk_up()
            elif dirv == 3 and self.value[3] != 2:
                print("walk([{0}, {1}] → [{2}, {1}])".format(self.x, self.y, self.x-1))
                self.nwalk_left()
            elif dirv == 5 and self.value[5] != 2:
                print("walk([{0}, {1}] → [{2}, {1}])".format(self.x, self.y, self.x+1))
                self.nwalk_right()
            elif dirv == 7 and self.value[7] != 2:
                print("walk([{0}, {1}] → [{0}, {2}])".format(self.x, self.y, self.y+1))
                self.nwalk_down()
            else:
                print("walk value is wrong!({})".format(dirv))
                self.search_up()
            self.before_move = dir_rev(dirv)
            self.ready = False

    def see(self, dirv):
        if self.ready:
            if dirv == 1:
                self.nlook_up()
            elif dirv == 3:
                self.nlook_left()
            elif dirv == 5:
                self.nlook_right()
            elif dirv == 7:
                self.nlook_down()
            else:
                print("see value is wrong!({})".format(dirv))
                self.search_up()
            self.ready = False

    def attack(self, dirv):
        if self.ready:
            if dirv == 1:
                self.put_up()
            elif dirv == 3:
                self.put_left()
            elif dirv == 5:
                self.put_right()
            elif dirv == 7:
                self.put_down()
            else:
                print("attack value is wrong!({})".format(dirv))
                self.search_up()
            self.ready = False

    def issafe(self, dirv=-1):
        if dirv == -1:
            print("checking of around...")
            b = 0
            for i in range(1, 9, 2):
                if self.value[i] == 2:
                    b += 1 
            return True if b < 3 else False
        else:
            print("checking of side..({})".format(dirv))
            if not self.ready:
                self.nget_ready()
            if self.value[dirv]==1:
                return False
            else:
                self.see(dirv)
                if dirv==1 or dirv==7:
                    if dirv==1 and self.value[7]==2:
                        return False
                    elif dirv==7 and self.value[1]==2:
                        return False
                    elif self.value[4]==2 and self.value[dir_rev(dirv)-1]==2 and self.value[dir_rev(dirv)+1]==2:
                        return False
                    elif self.value[4]==1 or self.value[dir_rev(dirv)-1]==1 or self.value[dir_rev(dirv)+1]==1:
                        return False
                    else:
                        return True
                elif dirv==3 or dirv==5:
                    if dirv==3 and self.value[5]==2:
                        return False
                    elif dirv==5 and self.value[3]==2:
                        return False
                    elif self.value[4]==2 and self.value[dir_rev(dirv)-3]==2 and self.value[dir_rev(dirv)+3]==2:
                        return False
                    elif self.value[4]==1 or self.value[dir_rev(dirv)-3]==1 or self.value[dir_rev(dirv)+3]==1:
                        return False
                    else:
                        return True

    def check_enemy(self):
        """敵が攻撃可能な位置にいるか確認していたら攻撃 斜め位置にいたらputしてこっちに誘導"""

        for i in range(1, 9, 2):
            if self.value[i] == 1:
                self.attack(i)
                return None
        for i in range(0, 8, 2):
            if self.value[i] == 1 and self.issafe():
                if i < 4:
                    if self.value[i+3]==0 and (self.value[1]==0 or self.value[1]==3):
                        self.attack(i+3)
                    elif self.value[i+3]==3 and self.value[1]==0:
                        self.attack(1)
                    elif (i==0 and self.value[1]==2 and self.value[3]==2) or (i==2 and self.value[1]==2 and self.value[5]==2):
                        self.free_move()
                    else:
                        print("wait for the enemy")
                        self.search_up()
                        self.ready = False
                if i > 4:
                    if self.value[i-3]==0 and (self.value[1]==0 or self.value[1]==3):
                        self.attack(i-3)
                    elif self.value[i-3]==3 and self.value[1] == 0:
                        self.attack(1)
                    elif (i==6 and self.value[7]==2 and self.value[3]==2) or (i==8 and self.value[7]==2 and self.value[5]==2):
                        self.free_move()
                    else:
                        print("wait for the enemy")
                        self.search_up()
                        self.ready = False

    def free_getheart(self):
        print("進行方向以外のハートをチェックします")
        for i in range(1,9,2):
            if self.value[i] == 3 and self.issafe(i):
                print("安全圏内にハートを発見、ゲットします({})".format(i))
                self.nget_ready()
                self.walk(i)
                return None
            elif self.value[i] == 3:
                print("ハートを発見しましたが、安全圏内ではありませんでした({})".format(i))
        for i in range(0,9,2):
            if self.value[i] == 3:
                if i < 4:
                    if self.value[0]!=1 and self.value[2]!=1 and self.value[1]!=2:
                        print("斜めの位置にハートを発見しました。接近します({})".format(i))
                        self.nget_ready()
                        self.walk(1)
                        return None
                    else:
                        self.nget_ready()
                        if i==0 and self.value[3]!=2 and self.value[6]!=1:
                            print("斜めの位置にハートを発見しました。接近します({})".format(i))
                            self.nget_ready()
                            self.walk(3)
                            return None
                        elif i==2 and self.value[5]!=2 and self.value[8]!=1:
                            print("斜めの位置にハートを発見しました。接近します({})".format(i))
                            self.nget_ready()
                            self.walk(5)
                            return None
                        else:
                            self.free_move()
                elif i > 4:
                    if self.value[6]!=1 and self.value[8]!=1 and self.value[7]!=2:
                        print("斜めの位置にハートを発見しました。接近します({})".format(i))
                        self.nget_ready()
                        self.walk(7)
                        return None
                    else:
                        self.nget_ready()
                        if i==6 and self.value[3]!=2 and self.value[0]!=1:
                            print("斜めの位置にハートを発見しました。接近します({})".format(i))
                            self.nget_ready()
                            self.walk(3)
                            return None
                        elif i==8 and self.value[5]!=2 and self.value[2]!=1:
                            print("斜めの位置にハートを発見しました。接近します({})".format(i))
                            self.nget_ready()
                            self.walk(5)
                            return None
                        else:
                            self.free_move()
        print("安全圏内にハートを発見できませんでした")
        self.free_move()

    def get_heart(self):
        if self.before_move != 0:
            print("進行方向にハートがあるかチェックします")
            if self.value[dir_rev(self.before_move)] == 3:
                if self.issafe(dir_rev(self.before_move)):
                    print("進行方向の安全圏内にハートを発見、ゲットします({})".format(dir_rev(self.before_move)))
                    self.nget_ready()
                    self.check_enemy()
                    self.walk(dir_rev(self.before_move))
                else:
                    print("進行方向にハートを発見しましたが、安全圏内ではありませんでした")
                    self.free_getheart()
            else:
                print("進行方向にハートがありませんでした")
                self.free_getheart()
        else:
            self.free_getheart()

    def free_move(self):
        print("into the 'free_move'.")
        if not self.issafe():
            for r in self.wall_pos:
                if self.value[r] != 2:
                    self.walk(r)
        elif self.go_straight():
            print("the 'go_straight' is True.")
        elif len(self.seek_nwal()) == 1 and self.value[self.seek_nwal()[0]]!=2 and self.issafe():
            print("情報を優先して移動しました({})".format(self.seek_nwal()))
            self.walk(self.seek_nwal()[0])
        else:
            print("情報のある位置が一つに絞れませんでした")
            lista = [[0 for i in range(2)] for i in range(4)]
            o = 0
            if len(self.seek_nwal())>1:
                for i in self.seek_nwal():
                    lista[o][0] = self.seek_nwal_l(i)
                    lista[o][1] = i
                    o += 1
            else:
                for i in self.wall_pos:
                    lista[o][0] = self.seek_nwal_l(i)
                    lista[o][1] = i
                    o += 1
            nwalnow = []
            big = lista[0][1]
            for i in lista:
                if big < i[0]:
                    big = i[0]
            for t in lista:
                if big == t[0]:
                    nwalnow.append(t[1])
            pct_mp = []
            for i in self.safe_map:
                if i != self.before_move:
                    pct_mp.append(i)
            if len(pct_mp) > 0:
                self.nget_ready()
                dirand = random.choice(pct_mp)
                print("周囲の情報量が同じ向きがあったのでランダムで移動します({})".format(dirand))
                self.walk(dirand)
            else:
                self.nget_ready()
                dirand = random.choice(self.safe_map)
                print("例外なのでランダムで移動します({0}) 選択肢は{1}個で、{2}でした".format(dirand,len(self.safe_map),self.safe_map))
                self.walk(dirand)

    def go_straight(self):
        print("into the 'go_straight'.")
        if self.before_move != 0:
            if self.isnwal(dir_rev(self.before_move)):
                print("情報を優先して進行方向に移動しました({})".format(dir_rev(self.before_move)))
                self.walk(dir_rev(self.before_move))
                return True
            else:
                print(f"進行方向は既に行っていました({dir_rev(self.before_move)})")
                return False
        else:
            print("進行方向の情報がありませんでした")
            return False

    def first_move(self):
        """
        最初の挙動　自機の位置を確認\n
        ※ 注意！first_move関数内ではまだ座標を把握していないので、field_mapに書き込む関数を使うとエラーが起こります
        """
        print("checking your coordinates...")
        self.value = self.get_ready()
        if self.temp == 0:
            self.x = 9
            self.y = 9
            self.value = self.search_left()
            for i in range(9):
                if self.value[8-i] == 2:
                    self.x-=1
                else:
                    break
            self.value = self.get_ready()
            self.value = self.search_up()
            for i in range(9):
                if self.value[8-i] == 2:
                    self.y-=1
                else:
                    break
        else:
            self.x = 5
            self.y = 7
            self.value = self.search_right()
            for i in range(9):
                if self.value[8-i] == 2:
                    self.x+=1
                else:
                    break
            self.value = self.get_ready()
            self.value = self.search_down()
            for i in range(9):
                if self.value[8-i] == 2:
                    self.y+=1
                else:
                    break
        print("I'm on [{self.x},{self.y}].")

def dir_conv(x, y):
    """座標の変化の割合を引数にすると方向が返ってくる"""
    if y == -1:
        return 1
    elif x == -1:
        return 3
    elif x == 1:
        return 5
    elif y == 1:
        return 7
    else:
        raise ValueError(f"[{x}, {y}] value is wrong!")

def dir_rev(dira):
    """方向を引数に入れると逆が返る"""
    if dira == 1:
        return 7
    elif dira == 3:
        return 5
    elif dira == 5:
        return 3
    elif dira == 7:
        return 1
    else:
        raise ValueError(f"[{dira}] value is wrong!")

ncli = new_client()

# Main
if __name__ == "__main__":
    print("program boot.")

    ncli.first_move()
    loop_num = 0

    while(True):
        print("entered loop for the {}th time".format(loop_num))
        ncli.nget_ready()
        ncli.get_heart()
        loop_num += 1