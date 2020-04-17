import tkinter as tk
import datetime as dt


from services.appService import AppService


# app service controls the application services like displaying windows 
# 
#  we will also create an orchestrator once we have this piece down
# for now we just want to test the various pages

app = AppService()

# uncomment any of the following to test pages

# app.navigationService.launchDebugWindow()

app.navigationService.launchReminderWindow(dt.date.today())
