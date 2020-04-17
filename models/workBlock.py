import datetime as dt

# a block of time the user has scheduled - may represent future block or a block in the past
class WorkBlock:

    def __init__(self, startTime: dt.datetime, endTime: dt.datetime, checkList: dict = None):
        self.startTime = startTime
        self.endTime = endTime

        # checklist can be more involved over time but for now, just a dictionary of "taskname" as keys, True/False as values (depending on completion status)  
        self.checkList = {}
        
        if(checkList is not None):
            self.checkList = checkList
