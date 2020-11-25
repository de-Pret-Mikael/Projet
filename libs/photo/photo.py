import subprocess
import tkinter
from PIL import ImageTk,Image


class photo:
    def __init__(self, path, sizetup=(32,32),photo=False):
        self.path = path
        self.photo = photo
        self.sizetup = sizetup
        self.buildDict()

    def buildPhoto(self, name,):
        path = "{}/{}".format(self.path, name)
        img = Image.open(path)
        img = img.resize(self.sizetup,Image.ANTIALIAS)
        if self.photo:
            photo = ImageTk.PhotoImage(img)
            return photo
        else:
            return img

    def buildDict(self):
        lname = self.takeName()
        dic = {}
        for i in lname:
            name = "".join(i.split(".png"))
            dic[name] = self.buildPhoto(i)
        self.__dict__ = dic

    def takeName(self):
        chemin = "\\".join(self.path.split("/"))
        dir = subprocess.run(["dir", chemin], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
        find = subprocess.run('find "png"', shell=True, input=dir.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              universal_newlines=True)
        name = []
        for i in find.stdout.split():
            if "png" in i:
                name.append(i)
        return name


if __name__ == "__main__":
    myapp = tkinter.Tk()
    p = photo("../../testimg/dungeon")
    print(p.__dict__)
    # print(p.wallH)
