
# handles storing work blocks

import datetime as dt

from models.workBlock import WorkBlock

class WorkBlockStorageService:

    def __init__(self):
        
        # TODO - decide how want to store work blocks - pickle, database 
        # if we're just gonna pickle a file, we can write that logic in this class - discuss this

        self.__ensureStorageAvailability()

    def getBlocksForDate(self, date: dt.date) -> []:
        # TODO - implement get blocks from data store - should get all blocks for the date being passed
        return [] # dummy list for now

    def addBlock(self, workBlock: WorkBlock) -> None:
        # TODO - add a single block to a date and save to the storage location
        pass

    def __ensureStorageAvailability(self) -> None:
        # TODO - make sure the storage location exists - if it doesn't, create it here
        pass