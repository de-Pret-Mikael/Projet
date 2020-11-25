from random import randrange
from PIL import ImageGrab, ImageTk, Image
import tkinter
from libs.photo import photo
from libs.labyrinthe import Labyrinthe
from libs.application.application import app
from libs.hero import *

def interDungeon(size, width, height, laby, pDun):
    img_w = (width * 2 + 1) * size
    img_h = (height * 2 + 1) * size
    dungeon = Image.new("RGB", (img_w, img_h))
    for y in laby.laby:
        for x in y:
            xImg = x.x * size
            yImg = x.y * size
            if x.wall:
                list = laby.wall_around(x.x, x.y)
                top = "top" in list
                down = "down" in list
                left = "left" in list
                right = "right" in list
                if down and left and right:
                    dungeon.paste(pDun.wallT, (xImg, yImg))
                elif down and left and top:
                    dungeon.paste(pDun.wallHR, (xImg, yImg))
                elif down and right and top:
                    dungeon.paste(pDun.wallHL, (xImg, yImg))
                elif right and left:
                    dungeon.paste(pDun.wallH, (xImg, yImg))
                elif top and left:
                    dungeon.paste(pDun.wallDR, (xImg, yImg))
                elif top and right:
                    dungeon.paste(pDun.wallDL, (xImg, yImg))
                elif top and down:
                    dungeon.paste(pDun.wallV, (xImg, yImg))
                elif down and left:
                    dungeon.paste(pDun.wallHR, (xImg, yImg))
                elif down and right:
                    dungeon.paste(pDun.wallHL, (xImg, yImg))
                elif top:
                    dungeon.paste(pDun.wallE, (xImg, yImg))
                elif down:
                    dungeon.paste(pDun.wallV, (xImg, yImg))
                elif left:
                    dungeon.paste(pDun.wallH, (xImg, yImg))
                elif right:
                    dungeon.paste(pDun.wallH, (xImg, yImg))
            else:
                rand = randrange(0, 2)
                if rand:
                    dungeon.paste(pDun.ground1, (xImg, yImg))
                else:
                    dungeon.paste(pDun.ground2, (xImg, yImg))
                if laby.get_cell(x.x, x.y).end:
                    dungeon.paste(pDun.trap, (xImg, yImg))
    dungeon = ImageTk.PhotoImage(dungeon)
    return dungeon

def interHero(app, hero, pPng, soldier=True):
    xCan = hero.x * size +2
    yCan = hero.y * size +2
    if soldier:
        app.drawImg(xCan, yCan, anchor="nw", img=pPng.soldier)
    else:
        app.drawImg(xCan, yCan, anchor="nw", img=pPng.mage)

def move(event):
    l = event.widget.laby
    png = event.widget.hero
    if event.char == "e" and (l.end == {"x": png.x, "y": png.y}):
        myapp.quit()
        print("vous avez trouver la sortie")
    png.move(event.char,laby=l)
    heroPos = {"lastx": png.lastx, "lasty": png.lasty, "newx": png.x, "newy": png.y}
    l.heroMove(**heroPos)
    myapp.updateCan(anchor="nw")
    interHero(myapp, png, pPng,soldier=False)
    myapp.update()

def new():
    myapp.laby = Labyrinthe(height, width)
    l = myapp.laby
    png = myapp.hero
    png.setPosi(**l.start)
    myapp.saveCan(interDungeon(size,width,height,l,pDun))
    myapp.updateCan(anchor="nw")
    interHero(myapp, png, pPng,soldier=False)
    myapp.update()
    pass

if __name__ == "__main__":
    height, width = 5,5
    size = 32
    # application
    name = "students's dungeon"
    minsize = ((width * 2 + 1) * size, (height * 2 + 1) * size)
    myapp = app(title=name, minSize=minsize, laby=Labyrinthe(height, width), hero=hero())
    myapp.buildCan(height=(height * 2 + 1) * size - 2, width=(width * 2 + 1) * size - 2, bg="black")
    # image
    pDun = photo("img/dungeon",(size,size))
    pPng = photo("img/player/blue",(size,size),photo=True)
    # menu
    mainmenu = tkinter.Menu(myapp)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="new", command=new)
    first_menu.add_command(label="quitter", command=myapp.quit)

    mainmenu.add_cascade(label="jeu", menu=first_menu)
    myapp.configure(menu=mainmenu)
    tupleSequence = ("<KeyPress-z>", "<KeyPress-q>", "<KeyPress-s>", "<KeyPress-d>", "<KeyPress-e>")
    myapp.event_add("<<move>>", *tupleSequence)
    myapp.addBind("<<move>>", move)
    myapp.launch()

    # myapp.resizable(width=False,height=False)
