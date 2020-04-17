import tkinter as tk
import datetime as dt


# import our parent class 
from windows.window import Window
from windows.setBlocksWindow import SetBlocksWindow


class ReminderWindow(Window):

    def __init__(self, window: tk.Tk, date: dt.date):
        # set details in parent class - 
        super().__init__(window, "Don't forget to set your blocks")
        
        # date
        self.__date = date

        # create our buttons here
        self.setNow_button = tk.Button(window, text="Set Now", command=lambda: self.setNow_button_clicked())
        self.remindLater_button = tk.Button(window, text="Set For Week", command=lambda: self.remindLater_button_clicked())

        # TODO - figure out how to make these buttons look good - https://www.geeksforgeeks.org/python-add-style-to-tkinter-button/
        self.setNow_button.grid(columnspan=5, ipadx=70, ipady=50)
        self.remindLater_button.grid(columnspan=5, ipadx=100, ipady=50)

        # call render last
        self.render()
        

    def setNow_button_clicked(self):
        # close this window and go to the 
        self.close()
        SetBlocksWindow(self.__window, self.__date)
        
    def remindLater_button_clicked(self):
        # TODO - add some "queue reminder functionality here we can use"
        # for now, we'll just close this window
        self.close()