import tkinter as tk
import datetime as dt


# import our parent class 
from windows.window import Window

class DebugWindow(Window):

    def __init__(self, window: tk.Tk):
        # set details in parent class - 
        super().__init__(window, "Developer Debug Window")

        # call render last
        self.render()


    
        