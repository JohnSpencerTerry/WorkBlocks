import tkinter as tk
import datetime as dt


# import our parent class 
from windows.window import Window

# import the storage service where we'll save any changes the user makes / get the 
from services.workBlockStorageService import WorkBlockStorageService

from models.workBlock import WorkBlock

class SetBlocksWindow(Window):

    def __init__(self, window: tk.Tk, date: dt.date):
        # set details in parent class - 
        super().__init__(window, "Set Blocks")
        
        # init our storage service
        self.__storageService = WorkBlockStorageService()

        # date
        self.__date = date

        # local list of work blocks for the day - this is an "unsaved" list until set for day/week is clicked to sync to the storage service
        self.__blocksForDate = self.__storageService.getBlocksForDate(date)

        # create buttons here
        self.seeWeek_button = tk.Button(window, text="See Week", command=lambda: self.seeWeek_button_clicked())
        self.setForWeek_button = tk.Button(window, text="Set For Week", command=lambda: self.setForWeek_button_clicked())
        self.setForDay_button = tk.Button(window, text="Set For Day", command=lambda: self.setForDay_button_clicked())
        self.addBlock_button = tk.Button(window, text="Set For Day", command=lambda: self.setForDay_button_clicked())

        # TODO - create blocks table with last column being input field (if supported)

        # TODO - add see week button to bottom right

        # TODO - add set for today / week buttons to bottom left

        # call render last
        self.render()

    def seeWeek_button_clicked(self):
        # TODO - navigate to the week view
        pass

    def setForWeek_button_clicked(self):
        # TODO - apply the current blocksForDate to the week using storage service
        pass

    def setForDay_button_clicked(self):
        # TODO - apply the current blocksForDate to the week using storage service
        pass
    
    def addBlock_button_clicked(self):
        # TODO - pass the work block created in the UI to the local list
        pass

    def removeBlock(self, workBlock: WorkBlock):
        # TODO - remove block from the local list - this will be called by the remove block button on the row
        pass

    def addBlock(self, workBlock: WorkBlock):
        # TODO - add block to the local list - this will be called by 
        pass