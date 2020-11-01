from random import *


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

    def droite(self):
        self.passe(self.x,self.y)
        self.x += 1

    def gauche(self):
        self.passe(self.x,self.y)
        self.x -= 1

    def haut(self):
        self.passe(self.x,self.y)
        self.y += 1

    def bas(self):
        self.passe(self.x,self.y)
        self.y -= 1

    # def affPos(self):
    #   hero.update(setPosi)

    def choix_deplacement(self):
        decal = 0
        condi = True
        while condi:
            decal = int(input("appuyez sur 6 pour droite, 4 pour gauche, 2 pour bas et 8 pour haut puis ENTER "))
            if decal == 6 or decal == 4 or decal == 2 or decal == 8:
                condi = False

        # deci = int(decal)
        if decal == 6:
            self.droite()
        if decal == 8:
            self.haut()
        if decal == 4:
            self.gauche()
        if decal == 2:
            self.bas()


    def passe(self, lastx, lasty):
        self.lastx = lastx
        self.lasty = lasty


if __name__ == "__main__":
    pnj = hero()
    pnj.x = randint(1, 8)
    print(pnj.x)
    pnj.y = randint(1, 8)
    print(pnj.x, pnj.y, pnj.lastx, pnj.lasty)
    pnj.choix_deplacement()
    print(pnj.x, pnj.y, pnj.lastx, pnj.lasty)
