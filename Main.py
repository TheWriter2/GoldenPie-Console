import sys
import random
import os
import platform

class Program:
    def __init__(self):
        self.coms = {
            "listdir":"self.search",
            "listfile":"self.search_file",
            "main.exit":"self.exit",
            "text.write":"self.write",
            "dirgo":"self.godir",
            "main.about":"self.about",
            #"main.win.about":"self.aboutwin",
            "createdir":"self.dirmake",
            "text.read":"self.textread",
            "deletedir":"self.dirdel",
            "runfile":"self.runpy"
        }

    def command(self):
        self.inp = input("Type the command:")
        if self.inp in self.coms:
            eval(self.coms[self.inp] + "()")
            self.command()
        else:
            input("Wrong or unknown command, enter to continue")
            self.command()

    def search(self):
        self.finp = input("Type dir to search:")
        if self.finp == "self":
            with os.scandir(os.path.abspath(os.getcwd())) as self.lt:
                for i in self.lt:
                    if os.path.isdir(i):
                        print(i)
                else:
                    return
        else:
            with os.scandir(self.finp + "/") as self.ents:
                for ent in self.ents:
                    if os.path.isdir(ent):
                        print(ent)
                else:
                    return

    def search_file(self):
        with os.scandir(input("Type dir to search:") + "/") as self.ents:
            for ent in self.ents:
                if os.path.isfile(ent):
                    print(ent.name)
            else:
                return

    def exit(self):
        input("Thanks for using(Enter to continue)")
        sys.exit()

    def write(self):
        self.f = open(input("Type the name of the file:") + ".txt", "w+")
        for i in range(1000):
            self.l = input("(:") + "\n"
            if self.l == "///stop\n":
                return
            else:
                self.f.write(self.l)

    def godir(self):
        os.chdir(input("Type the directory to which you want to go:"))
        return

    def about(self):
        print("GoldenPie Console")
        print("Version 1.0 - Build 2/24.11.19")
        input("Enter to continue")
        return

    def aboutwin(self):
        if platform.system() == "Windows":
            os.startfile("C:\Program Files (x86)\GoldenPie\gpabtwin.vbs")
            input("Enter to continue")
            return
        else:
            return

    def dirmake(self):
        os.mkdir(input("Type the name of the folder:") + "/")
        return

    def textread(self):
        x = 0
        self.f_t = [""]
        self.f = open(input("Type the name of the file:") + ".txt", "r+")
        self.f_l = self.f.readlines()
        for i in self.f_l:
            self.f_t.insert(x, i)
            x += 1
        else:
            for i in self.f_t:
                print(i)
            return

    def dirdel(self):
        pth = input("Type the name of the folder:")
        if os.path.isdir(pth) and len(os.listdir(pth)) == 0:
            os.rmdir(pth)
            return
        else:
            print("Path is not a folder or is not empty.")
            return

    def runpy(self):
        script = open(str(input("Type the name of the script:")) + ".txt", "r+")
        script_l = script.readlines()
        for i in script_l:
            exec(i)
        else:
            return

a = Program()
a.command()