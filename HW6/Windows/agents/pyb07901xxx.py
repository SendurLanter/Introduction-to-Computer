import ctypes
import sys
import random

MOVE = {
    'noAct': 0,
    'U_Act': 1,
    'D_Act': 2,
    'L_Act': 3,
    'R_Act': 4,
    'ACC_Act': 5
}

class view:
    def __init__(self,map):
        self.map = map
        self.isFood = self.getFood(3)
        self.isWall = self.getWall(3)
        
    def getFood(self,rad):
        isFood = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == ".":
                    isFood = isFood + [1]
                else:
                    isFood = isFood + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == ".":
                    isFood = isFood + [1]
                else:
                    isFood = isFood + [0]
        else:
            for x in range(49):
                if self.map[x] == ".":
                    isFood = isFood + [1]
                else:
                    isFood = isFood + [0]
        self.isFood = isFood
        return isFood


    def getWall(self,rad):
        isWall = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == "#":
                    isWall = isWall + [1]
                else:
                    isWall = isWall + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == "#":
                    isWall = isWall + [1]
                else:
                    isWall = isWall + [0]
        else:
            for x in range(49):
                if self.map[x] == "#":
                    isWall = isWall + [1]
                else:
                    isWall = isWall + [0]

        self.isWall = isWall
        return isWall


    def getbody(self,rad):
        isbody = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == "*":
                    isbody = isbody + [1]
                else:
                    isbody = isbody + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == "*":
                    isbody = isbody + [1]
                else:
                    isbody = isbody + [0]
        else:
            for x in range(49):
                if self.map[x] == "*":
                    isbody = isbody + [1]
                else:
                    isbody = isbody + [0]

        self.isbody = isbody
        return isbody


    def getopp(self,rad):
        isopp = []
        if rad == 1 :
            for x in [16,17,18,23,24,25,30,31,32] :
                if self.map[x] == "@":
                    isopp = isopp + [1]
                else:
                    isopp = isopp + [0]
        elif rad == 2 :
            for x in [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40] :
                if self.map[x] == "@":
                    isopp = isopp + [1]
                else:
                    isopp = isopp + [0]
        else:
            for x in range(49):
                if self.map[x] == "@":
                    isopp = isopp + [1]
                else:
                    isopp = isopp + [0]

        self.isopp = isopp
        return isopp


class pyAgent:
    def __init__(self):
        view = []
    # void getView(int rad);
    # void getFoodInView(int rad);
    # void getSnakeInView(int rad);
    
    def isOppDir(self, a1, a2):
        if (a1 == U_Act and a2 == D_Act) or (a1 == D_Act and a2 == U_Act) or (a1 == R_Act and a2 == L_Act) or (a1 == R_Act and a2 == R_Act) :
            return true
        return false
    
    
def randMove():
    r = random.randint(0,6)
    # 2/6%: just go ahead
    # 4/6%: 1/6% for each dir
    
    if( r == 0 ):
        return MOVE['noAct']
    elif( r == 1 ):
        return MOVE['U_Act']
    elif( r == 2 ):
        return MOVE['D_Act']
    elif( r == 3 ):
        return MOVE['L_Act']
    elif( r == 4 ):
        return MOVE['R_Act']
    elif( r == 5 ):
        return MOVE['ACC_Act']
    else:
        return MOVE['noAct']

# !! TODO 5: implement your own actionToDo function here
def actionToDo(arg):
    # !! Here are some example for python to get view

    map = f.readline()
    View = view(map)
    
    #1圈內的牆座標
    wall=View.getWall(1)
    #1圈內蛇身體的座標
    body=View.getbody(1)
    #3圈內所有的'*''
    opp=View.getbody(3)


    #從上往下有敵人
    if opp[10]!=0 and opp[17] and opp[45]!=0:
        if wall[3]!=0:
            return 4
        else:
            return 3
    
    #從下往上有敵人
    if opp[31]!=0 and opp[38] and opp[3]!=0:
        if wall[3]!=0:
            return 4
        else:
            return 3

    #從左往右有敵人
    if opp[23]!=0 and opp[22] and opp[27]!=0:
        if wall[1]!=0:
            return 2
        else:
            return 1

    #從右邊往左有敵人
    if opp[21]!=0 and opp[26] and opp[25]!=0:
        if wall[1]!=0:
            return 2
        else:
            return 1
    

    #如果由下往上會碰到自己的身體
    if body[1]!=0 and body[3]!=0 and body[5]!=0:
        return 2

    #如果由下往上會碰到自己的身體
    if body[1]!=0 and body[3]!=0 and body[7]!=0:
        return 4

    #如果由左往右邊會碰到自己的身體
    if body[1]!=0 and body[5]!=0 and body[7]!=0:
        return 3

    #如果由左往右邊會碰到自己的身體
    if body[3]!=0 and body[5]!=0 and body[7]!=0:
        return 1

    if body[1]!=0 and body[7]!=0:
        if opp[22]==0 and opp[23]==0:
            return 3
        else:
            return 4

    if body[3]!=0 and body[5]!=0:
        if opp[10]==0 and opp[17]==0:
            return 1
        else:
            return 2

    #牆壁的部分
    #碰到右上角的情況
    if wall[1]!=0 and wall[3]!=0:
        #從右往左碰到右上角
        if body[5]!=0:
            return 2
        else:
            return 4

    #碰到左上角的情況
    if wall[1]!=0 and wall[5]!=0:
        #從左往右碰到左上角
        if body[3]!=0:
            return 2
        else:
            return 3

    #碰到右下角的情況
    if wall[5]!=0 and wall[7]!=0:
        #從上往下碰到右下角
        if body[1]!=0:
            return 3
        else:
            return 1

    #碰到左下角的情況
    if wall[3]!=0 and wall[7]!=0:
        #從上往下碰到左下角
        if body[1]!=0:
            return 4
        else:
            return 1

    #一般碰到牆壁的情況
    if wall[1]!=0:
        if body[7]!=0:
            return random.randint(3,4)
        else:
            return 2

    if wall[3]!=0:
        if body[5]!=0:
            return random.randint(1,2)
        else:
            return 4

    if wall[5]!=0:
        if body[3]!=0:
            return random.randint(1,2)
        else:
            return 3
            
    if wall[7]!=0:
        if body[1]!=0:
            return random.randint(3,4)
        else:
            return 1

    #第一圈偵查 如果附近有food
    ring=View.getFood(1)
    if ring[7]!=0:
        return 2
    if ring[1]!=0:
        return 1
    if ring[3]!=0:
        return 3
    if ring[5]!=0:
        return 4
    if ring[0]!=0:
        if body[3]!=0:
            return 1
        else:
            return 3
    if ring[2]!=0:
        if body[5]!=0:
            return 1
        else:
            return 4
    if ring[6]!=0:
        if body[3]!=0:
            return 2
        else:
            return 3
    if ring[8]!=0:
        if body[5]!=0:
            return 2
        else:
            return 4

    #第二圈偵查  如果附近有food則轉向
    ring=View.getFood(2)

    #從左往右的情況
    if body[3]!=0:
        if ring[14]!=0:
            return 4
        if ring[3]!=0 or ring[4]!=0 or ring[8]!=0 or ring[9]!=0:
            return 1
        if ring[18]!=0 or ring[19]!=0 or ring[23]!=0 or ring[24]!=0:
            return 2      
    #從上往下
    if body[1]!=0:
        if ring[22]!=0:
            return 2
        if ring[15]!=0 or ring[16]!=0 or ring[20]!=0 or ring[21]!=0:
            return 3
        if ring[18]!=0 or ring[19]!=0 or ring[23]!=0 or ring[24]!=0:
            return 4
    #由下往上
    if body[7]!=0:
        if ring[2]!=0:
            return 1
        if ring[0]!=0 or ring[1]!=0 or ring[5]!=0 or ring[6]!=0:
            return 3
        if ring[3]!=0 or ring[4]!=0 or ring[8]!=0 or ring[9]!=0:
            return 4

    #由右往左
    if body[5]!=0:
        if ring[10]!=0:
            return 3
        if ring[0]!=0 or ring[1]!=0 or ring[5]!=0 or ring[6]!=0:
            return 1
        if ring[15]!=0 or ring[16]!=0 or ring[20]!=0 or ring[21]!=0:
            return 2

    #第三圈偵查 如果附近有food就轉向
    ring=View.getFood(3)

    #由左往右
    if body[3]!=0:
        if ring[27]!=0:
            return 4
        if ring[4]!=0 or ring[5]!=0 or ring[6]!=0 or ring[13]!=0 or ring[20]!=0:
            return 1
        if ring[34]!=0 or ring[41]!=0 or ring[48]!=0 or ring[47]!=0 or ring[46]!=0:
            return 2

    #由上往下
    if body[1]!=0:
        if ring[45]!=0:
            return 2
        if ring[34]!=0 or ring[41]!=0 or ring[48]!=0 or ring[47]!=0 or ring[46]!=0:
            return 4
        if ring[28]!=0 or ring[35]!=0 or ring[42]!=0 or ring[43]!=0 or ring[44]!=0:
            return 3

    #由下往上
    if body[7]!=0:
        if ring[3]!=0:
            return 1
        if ring[4]!=0 or ring[5]!=0 or ring[6]!=0 or ring[13]!=0 or ring[20]!=0:
            return 4
        if ring[0]!=0 or ring[1]!=0 or ring[2]!=0 or ring[7]!=0 or ring[14]!=0:
            return 3

    #由右往左
    if body[5]!=0:
        if ring[21]!=0:
            return 3
        if ring[0]!=0 or ring[1]!=0 or ring[2]!=0 or ring[7]!=0 or ring[14]!=0:
            return 1
        if ring[28]!=0 or ring[35]!=0 or ring[42]!=0 or ring[43]!=0 or ring[44]!=0:
            return 2

    
    '''#隨機改變方向
    dice= random.randint(1,10)
    #由上往下
    if opp[3]!=0 and opp[10]!=0 and opp[17]!=0:
        if dice>9:
            if  body[3]!=0:
                return 4
            else:
                return 3

    #由左往右
    if opp[21]!=0 and opp[22]!=0 and opp[23]!=0:
        if dice>9:
            if body[1]!=0:
                return 2
            else:
                return 1

    #由右往左
    if opp[25]!=0 and opp[26]!=0 and opp[27]!=0:
        if dice>9:
            if body[7]!=0:
                return 1
            else:
                return 2

    #由下往上
    if opp[31]!=0 and opp[38]!=0 and opp[45]!=0:
        if dice>9:
            if body[5]!=0:
                return 3
            else:
                return 4'''

    # View.getWall(2)
    
    # view (radius = 1):
    # 00 01 02
    # 03 me 05
    # 06 07 08
        
    # view (radius = 2):
    # 00 01 02 03 04
    # 05 06 07 08 09
    # 10 11 me 13 14
    # 15 16 17 18 19
    # 20 21 22 23 24
    # Max radius is 3
    
    # view (radius = 3):
    # 00 01 02 03 04 05 06
    # 07 08 09 10 11 12 13
    # 14 15 16 17 18 19 20
    # 21 22 23 me 25 26 27
    # 28 29 30 31 32 33 34
    # 35 36 37 38 39 40 41
    # 42 43 44 45 46 47 48
    

f = open(sys.argv[1],'r')

print(actionToDo(1))