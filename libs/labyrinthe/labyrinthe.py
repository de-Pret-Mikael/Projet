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
            self.numb = 0


class labyrinthe:
    def __init__(self):
        self.laby = []
        self.wall = []

    def buildGrid(self,line,rows):
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
        rand = random.randrange(0,len(self.wall))
        return rand

    def valVerif(self):
        for y in self.laby:
            for x in y:
                if x.numb != 1:

        return
    def show(self):
        for j in self.laby:
            t = []
            for i in j:
                if i.wall:
                    t.append("■")
                else:
                    t.append("□")
            print("".join(t))

l =  labyrinthe()
l.buildGrid(3, 3)
#l.show()
#print(l.wall)
#print("■■■■■")
#print("■■▲■■")

print(l.buildWay())