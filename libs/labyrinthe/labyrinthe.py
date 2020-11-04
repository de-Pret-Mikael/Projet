#▲▶▼◀■□●
import random
class cell:
    count = 0
    def __init__(self,x,y,wall=False):
        self.__id = "{},{}".format(x,y)
        self.__x = x
        self.__y = y
        self.wall = wall
        self.hero = False
        self.end = False
        if not self.wall:
            self.numb = self.__class__.count
            self.__class__.count +=1
        else:
            self.numb = -1
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def id(self):
        return self.__id

    def cellAdj(self, xMax, yMax):
        """
        :param xMax: valeur max de x
        :param yMax: valeur max de y
        :return envoie un dictionnaire de dictionnnaire composé des cellule adjacente
        """
        dic = {}
        xMax = 2 * xMax
        yMax = 2 * yMax
        if self.y - 1 >= 0:
            dic["top"] = {"x": self.x, "y": self.y - 1}
        if self.x + 1 <= xMax:
            dic["right"] = {"x": self.x + 1, "y": self.y}
        if self.y + 1 <= yMax:
            dic["down"] = {"x": self.x, "y": self.y + 1}
        if self.x - 1 >= 0:
            dic["left"] = {"x": self.x - 1, "y": self.y}
        return dic

class labyrinthe:
    def __init__(self,height=3,width=3):
        self.__height = round(height)
        self.__width = round(width)
        self.start = {"x":None,"y":None}
        self.end = {"x":None,"y":None}
        self.laby = []
        self.wall = []
        self.buildGrid()
        self.buildWay()
        self.startAndEnd()

    @property
    def height(self):
        return self.__height
    @property
    def width(self):
        return self.__width

    def get_cell(self, x, y):
        return self.laby[y][x]

    def buildGrid(self):
        """"""
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
        """"""
        while self.valVerif():
            if len(self.wall):
                rand = random.randrange(0, len(self.wall))
            else:
                break
            coord = list(map(lambda y: int(y), self.wall[rand].split(",")))
            del self.wall[rand]
            cell = self.get_cell(coord[0], coord[1])
            dic = cell.cellAdj(self.width, self.height)
            if not coord[0] % 2:
                vRigth = self.get_cell(**dic["right"]).numb
                vLeft = self.get_cell(**dic["left"]).numb
                if not (vRigth == vLeft):
                    cell.wall = False
                    if (vRigth > vLeft):
                        self.newVal(vRigth, vLeft)
                    else:
                        self.newVal(vLeft, vRigth)
            if not coord[1] % 2:
                vDown = self.get_cell(**dic["down"]).numb
                vTop = self.get_cell(**dic["top"]).numb
                if not (vDown == vTop):
                    cell.wall = False
                    if (vDown > vTop):
                        self.newVal(vDown, vTop)
                    else:
                        self.newVal(vTop, vDown)

    def newVal(self,val,nVal):
        """"""
        for y in self.laby:
            for x in y:
                if x.numb == val:
                    x.numb = nVal

    def valVerif(self):
        """"""
        for y in self.laby:
            for x in y:
                if x.numb != 0 or x.numb != -1:
                    return True
        return False

    def heroMove(self,lastx,lasty,newx,newy):
        self.get_cell(lastx,lasty).hero = False
        self.get_cell(newx,newy).hero = True

    def popHero(self,x,y):
        self.get_cell(x,y).hero = True

    def startAndEnd(self):
        listOfCell = []
        for y in self.laby:
            for x in y:
                if not x.wall:
                    listOfCell.append(x)
        rand = random.randrange(0, len(listOfCell))
        self.set_start(listOfCell[rand].x,listOfCell[rand].y)
        del listOfCell[rand]
        rand = random.randrange(0, len(listOfCell))
        listOfCell[rand].end = True
        self.set_end(listOfCell[rand].x,listOfCell[rand].y)

    def set_start(self,x,y):
        self.start = {"x":x,"y":y}

    def set_end(self,x,y):
        self.end = {"x":x,"y":y}


    def show(self):
        """"""
        for j in self.laby:
            t = []
            for i in j:
                if i.wall:
                    t.append("■")
                elif i.hero:
                    t.append("●")
                elif i.end:
                    t.append("▼")
                else:
                    t.append("□")
            print("".join(t))

    def wallaround(self, x, y):
        list = []
        dic = self.get_cell(x, y).cellAdj(self.width, self.height)
        for i in dic:
            if self.get_cell(**dic[i]).wall:
                list.append(i)
        return list


if __name__ == "__main__":
    l =  labyrinthe(3,6)
    l.popHero(**l.start)
    l.show()