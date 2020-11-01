from random import *
class hero:

    def __init__(self):
        self.x=0
        self.y=0
        self.decal = 0
    def setPosi(self,x,y):
        self.x=x
        self.y=y
    def droite(self):
        self.x += 1

    def gauche(self):
        self.x -= 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def affPos(self):
        hero.update(setPosi)


    def choix_deplacement(self):
        decal=0
        self.decal = int(input("appuyez sur 6 pour droite, 4 pour gauche, 2 pour bas et 8 pour haut puis ENTER"))
        while decal == 6 or decal == 4 or decal == 2 or decal == 8:
           # deci = int(decal)
            if decal == 6:
                droite(hero)
            if decal == 8:
                haut(hero)
            if decal == 4:
                gauche(hero)
            if decal == 2:
                bas(hero)


if __name__ == "__main__":
    pnj=hero()
    pnj.x = randint(1, 8)
    pnj.y = randint(1, 8)
    pnj.choix_deplacement()


