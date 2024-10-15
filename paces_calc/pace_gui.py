from tkinter import mainloop
from customtkinter import *

import paces_calc.pace_math as pm


class Pace_Window(CTk):
    def __init__(self):
        super().__init__()

def window_main():
    Pace_Window().mainloop()
    exit(0)