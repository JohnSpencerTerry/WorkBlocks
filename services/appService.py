import tkinter as tk

from services.appNavigationService import AppNavigationService

# holds data that needs to be shared throughout the app 

class AppService:  
    def __init__(self):
        self.window = tk.Tk()
        self.navigationService = AppNavigationService(self.window)
    
    def openDebugWindow(self):
        self
    
