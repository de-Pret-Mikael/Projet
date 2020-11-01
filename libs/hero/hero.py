from random import *
class hero:

    def __init__(self):
        self.x=0
        self.y=0
        self.decal = 0
    def depPosi(self):
        x = randint()
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
        self.decal = input("appuyez sur 6 pour droite, 4 pour gauche, 2 pour bas et 8 pour haut puis ENTER")
        if decal == 6:


hero.x = randint(1, 8)
hero.y = randint(1, 8)
hero.choix_deplacement(0)
