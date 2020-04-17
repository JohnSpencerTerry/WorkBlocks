import tkinter as tk

# base class for all windows - holds any common functionality we identify 
class Window:
    def __init__(self, window: tk.Tk, title: str = "Work Blocks"): # default title
        self.__window = window
        self.__window.title(title)
        
    def render(self):
        self.__window.mainloop()

    # close the current window - basically "quits" the GUI portion of the application
    def close(self) -> None:
        self.__window.quit
