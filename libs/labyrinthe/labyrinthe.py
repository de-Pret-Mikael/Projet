"▲▶▼◀■□"

import random
class cell:
    count = 0
    def __init__(self,x,y,wall=False):
        self.id = "{},{}".format(x,y)
        self.x = x
        self.y = y
        self.wall = wall
        if not self.wall:
            self.numb = self.__class__.count
            self.__class__.count +=1
        else:
            self.numb = -1

    def cellAdj(self,xMax,yMax):
        dic = {}
        xMax = 2*xMax
        yMax = 2*yMax
        if self.y-1 != 0:
            dic["top"] = self.y-1
        if self.x+1 != xMax:
            dic["right"] = self.x+1
        if self.y+1 != yMax:
            dic["down"] = self.y+1
        if self.x-1 != 0:
            dic["left"] = self.x-1
        return dic

class labyrinthe:
    def __init__(self,height=3,width=3):
        self.height = height
        self.width = width
        self.laby = []
        self.wall = []

    def buildGrid(self):
        line = self.height
        rows = self.width
        for y in range(0,2*line+1):
            self.laby.append([])
            for x in range(0,2*rows+1):
                if x%2 == 0 or y%2 == 0:
                    self.laby[y].append(cell(x,y,True))
                    if (x != 0) and (y!=0) and (x != rows*2) and (y != line*2):
                        if not (x%2==0 and y%2==0):
                            self.wall.append(self.laby[y][-1].id)
                else:
                    self.laby[y].append(cell(x, y))

    def buildWay(self):
        while self.valVerif():
            if len(self.wall):
                rand = random.randrange(0, len(self.wall))
            else:
                break
            x = list(map(lambda y:int(y),self.wall[rand].split(",")))
            del self.wall[rand]
            cell = self.laby[x[1]][x[0]]
            dic = cell.cellAdj(self.width,self.height)
            if not x[0]%2:
                vRigth = self.laby[x[1]][dic["right"]].numb
                vLeft = self.laby[x[1]][dic["left"]].numb
                if not (vRigth==vLeft):
                    cell.wall = False
                    if (vRigth > vLeft):
                        self.newVal(vRigth,vLeft)
                    else:
                        self.newVal(vLeft,vRigth)
            if not x[1]%2:
                vDown = self.laby[dic["down"]][x[0]].numb
                vTop =self.laby[dic["top"]][x[0]].numb
                if not (vDown == vTop):
                    cell.wall = False
                    if (vDown > vTop):
                        self.newVal(vDown,vTop)
                    else:
                        self.newVal(vTop,vDown)

    def newVal(self,val,nVal):
        for y in self.laby:
            for x in y:
                if x.numb == val:
                    x.numb = nVal

    def valVerif(self):
        for y in self.laby:
            for x in y:
                if x.numb != 0 or x.numb != -1:
                    return True
        return False

    def show(self):
        for j in self.laby:
            t = []
            for i in j:
                if i.wall:
                    t.append("■")
                else:
                    t.append("□")
            print("".join(t))



#print("■■■■■")
#print("■■▲■■")
l =  labyrinthe(5,10)
l.buildGrid()
l.buildWay()
l.show()
