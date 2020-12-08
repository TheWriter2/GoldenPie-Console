import sys
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
            "help":"self.help",
            "runpython":"self.runpy"
        }

        self.comhelp = {
            "listdir":"Prints all folders present in the specified directory.",
            "listfile":"Prints all files present in the specified directory.",
            "main.exit":"Exits the console.",
            "text.write":"Prompts to write a text document with a specified name and text(1000 Lines Maximum).",
            "dirgo":"Goes to a directory.",
            "main.about":"Shows the about text.",
            "createdir":"Creates a folder in the current directory.",
            "text.read":"Prints the specified .txt file.",
            "deletedir":"Deletes a empty folder.",
            "help":"Shows the help text.",
            "runpython": "Runs a python command."
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
        pth = input("Type dir to search:")
        if os.path.isdir(pth):
            with os.scandir(pth + "/") as self.ents:
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
        pdir = input("Type the directory to which you want to go:")
        if os.path.isdir(pdir):
            os.chdir(pdir)
        return

    def about(self):
        print("GoldenPie Console")
        print("Version 1.0 - Build 3/06.12.11")
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
        f = input("Type the name of the file:")
        self.f_t = [""]
        if os.path.isfile(f):
            self.f = open(f + ".txt", "r+")
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

    def help(self):
        for i in self.coms.keys():
            print(i + " - " + self.comhelp[i])
        return

    def runpy(self):
        print("Note:Python commands can cause problems with the script execution, a wrong command will crash the console.")
        pycom = input("Type the python command:")
        pycom.isidentifier()
        eval(pycom)
        return

a = Program()
a.command()