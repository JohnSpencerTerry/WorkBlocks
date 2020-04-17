
# responsible for navigating to various application windows 

import tkinter as tk
import datetime as dt

# import windows - these are the various UIs we're providing - each one has a cooresponding method below
from windows.debugWindow import DebugWindow
from windows.setBlocksWindow import SetBlocksWindow
from windows.reminderWindow import ReminderWindow


class AppNavigationService:
    
    def __init__(self, window: tk.Tk):
        self.__window = window

    def launchDebugWindow(self):
        DebugWindow(self.__window)
    
    def launchSetBlocksWindow(self, date: dt.date):
        SetBlocksWindow(self.__window, date)

    def launchReminderWindow(self, date: dt.date):
        ReminderWindow(self.__window, date)