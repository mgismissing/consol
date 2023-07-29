import colorama
import sys
import tkinter
import time

# Init
colorama.init(autoreset=False)

# Variables
class fore:
    BLACK = colorama.Fore.BLACK
    BLUE = colorama.Fore.BLUE
    CYAN = colorama.Fore.CYAN
    GREEN = colorama.Fore.GREEN
    MAGENTA = colorama.Fore.MAGENTA
    RED = colorama.Fore.RED
    RESET = colorama.Fore.RESET
    WHITE = colorama.Fore.WHITE
    YELLOW = colorama.Fore.YELLOW
class back:
    BLACK = colorama.Back.BLACK
    BLUE = colorama.Back.BLUE
    CYAN = colorama.Back.CYAN
    GREEN = colorama.Back.GREEN
    MAGENTA = colorama.Back.MAGENTA
    RED = colorama.Back.RED
    RESET = colorama.Back.RESET
    WHITE = colorama.Back.WHITE
    YELLOW = colorama.Back.YELLOW
class color:
    RESET_ALL = colorama.Style.RESET_ALL

class ext:
    class tkinter:
        window = None

# Configuration Variables
class settings:
    class text:
        forecolor = ""
        backcolor = ""
        textstyle = ""

# Functions
class text:
    def show(text: str = "", fore: color | str = "", back: color | str = "", style: color | str = ""):
        print(settings.text.forecolor + settings.text.backcolor + settings.text.textstyle + fore + back + style + text + colorama.Style.RESET_ALL + settings.text.forecolor + settings.text.backcolor + settings.text.textstyle)
class status:
    def error(code: int = 0, type = "Default", desc = "No Description", color = True, exit = False):
        print(settings.text.forecolor + settings.text.backcolor + settings.text.textstyle + colorama.Fore.RED * color + f"{type}Error: {desc}. [{code}]" + colorama.Style.RESET_ALL * color + settings.text.forecolor + settings.text.backcolor + settings.text.textstyle)
        if exit: sys.exit(code)
    def warn(code: int = 0, type = "Default", desc = "No Description", color = True):
        print(settings.text.forecolor + settings.text.backcolor + settings.text.textstyle + colorama.Fore.YELLOW * color + f"{type}Warning: {desc}. [{code}]" + colorama.Style.RESET_ALL * color + settings.text.forecolor + settings.text.backcolor + settings.text.textstyle)
class window:
    def new(xsize: int = 0, ysize = 0, xpos = 0, ypos = 0, backcolor = "#ffffff"):
        ext.tkinter.window = tkinter.Tk()
        ext.tkinter.window.geometry(f"{xsize}x{ysize}")
        ext.tkinter.window.geometry(f"+{xpos}+{ypos}")
        ext.tkinter.window.config(background=backcolor)
        ext.tkinter.window.mainloop()
    class position:
        def set(xpos: int, ypos):
            ext.tkinter.window.geometry(f"+{xpos}+{ypos}")
        def change(xpos: int, ypos):
            ext.tkinter.window.geometry(f"+{ext.tkinter.window.winfo_x + xpos}+{ext.tkinter.window.winfo_y + ypos}")
    def loop():
        ext.tkinter.window.mainloop()
    def create(xsize: int = 0, ysize = 0, xpos = 0, ypos = 0, backcolor = "#ffffff"):
        ext.tkinter.window = tkinter.Tk()
        ext.tkinter.window.geometry(f"{xsize}x{ysize}")
        ext.tkinter.window.geometry(f"+{xpos}+{ypos}")
        ext.tkinter.window.config(background=backcolor)
class variable:
    def __init__(self):
        self.value = None
    def set(self, value: int | str | list | dict | tuple):
        self.value = value
    def get(self):
        return self.value
    def getType(self):
        if type(self.value) == int:
            return int
        if type(self.value) == str:
            return str
        if type(self.value) == list:
            return list
        if type(self.value) == dict:
            return dict
        if type(self.value) == tuple:
            return tuple
        if type(self.value) == variable:
            return variable

# Configuration [.cnc] CoNsol Configuration
