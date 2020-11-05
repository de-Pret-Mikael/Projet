from random import *

from libs.labyrinthe import labyrinthe


class hero:

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__decal = 0
        self.lastx = 0
        self.lasty = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def decal(self):
        return self.__decal

    @x.setter
    def x(self, i):
        if not isinstance(i, int):
            raise ValueError("not integer")
        self.__x = i

    @y.setter
    def y(self, i):
        if not isinstance(i, int):
            raise ValueError("not integer")
        self.__y = i

    @decal.setter
    def decal(self, i):
        if not isinstance(i, int):
            raise ValueError("not integer")
        self.__decal = i

    def setPosi(self, x, y):
        self.x = x
        self.y = y

    def droite(self, laby):
        self.passe(self.x,self.y)
        if laby.get_cell(self.x+1,self.y).wall:
            print('fail')
        else:
            self.x += 1
            if laby.end == {"x": self.x, "y": self.y}:
                print('fiejufh')
            #self.end = {"x": x, "y": y}

    def gauche(self, laby):
        self.passe(self.x,self.y)
        if laby.get_cell(self.x-1,self.y).wall:
            print('fail')
        else:
            self.x -= 1
            return self.x, self.y

    def haut(self, laby):
        self.passe(self.x,self.y)
        if laby.get_cell(self.x,self.y-1).wall:
            print('fail')
        else:
            self.y -= 1
            return self.x, self.y

    def bas(self, laby):
        self.passe(self.x,self.y)
        if laby.get_cell(self.x,self.y+1).wall:
            print('fail')
        else:
            self.y += 1
            return self.x, self.y

    def pos(self, position):
        return self.laby[position[0]][position[1]] != -1
    # def affPos(self):
    #   hero.update(setPosi)

    def choix_deplacement(self,laby):
        decal = 0
        condi = True
        while condi:
            decal = int(input("appuyez sur 6 pour droite, 4 pour gauche, 2 pour bas et 8 pour haut puis ENTER "))
            if decal == 6 or decal == 4 or decal == 2 or decal == 8:
                condi = False

        # deci = int(decal)
        if decal == 6:
            self.droite(laby)
        if decal == 8:
            self.haut(laby)
        if decal == 4:
            self.gauche(laby)
        if decal == 2:
            self.bas(laby)


    def passe(self, lastx, lasty):
        self.lastx = lastx
        self.lasty = lasty

    def end(self, laby):
        if laby.end == self.droite() or laby.end == self.gauche() or laby.end == self.haut() or laby.end == self.bas():
            print('fini')


    #def end(self,x,y):
        #if set_end() self.gauche()
     #   print(self.x,self.y)


if __name__ == "__main__":
    l = labyrinthe(3,6)
    pnj = hero()
    pnj.x = randint(1, 8)
    pnj.y = randint(1, 8)
    print(pnj.x, pnj.y, pnj.lastx, pnj.lasty)
    pnj.choix_deplacement(l)
    print(pnj.x, pnj.y, pnj.lastx, pnj.lasty)


