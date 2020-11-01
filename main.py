from libs.labyrinthe import *
from libs.hero import *

if __name__ == "__main__":
    l =labyrinthe(3,6)
    png = hero()
    png.x = 1
    png.y = 1
    l.popHero(png.x,png.y)
    l.show()
    png.choix_deplacement()
    heroPos = {"lastx":png.lastx,"lasty":png.lasty,"newx":png.x,"newy":png.y}
    print(heroPos)
    l.heroMove(**heroPos)
    l.show()