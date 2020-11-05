from libs.labyrinthe import *
from libs.hero import *
import os
if __name__ == "__main__":
    l =labyrinthe(2,3)
    png = hero()
    print(l.start)
    png.setPosi(**l.start)
    l.show()
    k = 0
    while k<10:
        png.choix_deplacement(l)
        heroPos = {"lastx":png.lastx,"lasty":png.lasty,"newx":png.x,"newy":png.y}
        l.heroMove(**heroPos)
        l.show()
        k +=1