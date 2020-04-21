
# handles storing work blocks

import datetime as dt

import pickle as pk

# a block of time the user has scheduled - may represent future block or a block in the past
class WorkBlock:

    def __init__(self, startTime: dt.datetime, endTime: dt.datetime, checkList: dict = None):
        self.startTime = startTime
        self.endTime = endTime

        # checklist can be more involved over time but for now, just a dictionary of "taskname" as keys, True/False as values (depending on completion status)  
        self.checkList = {}
        
        if(checkList is not None):
            self.checkList = checkList



class WorkBlockStorageService:

    def __init__(self):
        # https://ianlondon.github.io/blog/pickling-basics/
        # TODO - decide how want to store work blocks - pickle, database 
        # if we're just gonna pickle a file, we can write that logic in this class - discuss this

        self.__ensureStorageAvailability()

    def getBlocksForDate(self, date: dt.date) -> []:
        # TODO - implement get blocks from data store - should get all blocks for the date being passed
        filename = self.__getFileForBlock(date)
        with open(filename, 'rb') as f:
            return pk.load(f)


    def addBlock(self, workBlock: WorkBlock) -> None:
        # TODO - add a single block to a date and save to the storage location
        filename = self.__getFileForBlock(workBlock.startTime)
        with open(filename, 'wb') as f:
            pk.dump(workBlock, f)




    def __ensureStorageAvailability(self) -> None:
        # TODO - make sure the storage location exists - if it doesn't, create it here
        pass
    
    def __getFileForBlock(self, workBlockStartTime: dt.datetime) -> str:
        #%W (week number of year Monday = first day)
        weeknumber = workBlockStartTime.strftime('%W') 
        return 'workblockstore_week{0}.pickle'.format(weeknumber)


class WorkBlockStorageServiceTest:
    def __init__(self):
        self.service = WorkBlockStorageService()
        self.dataset = []
        self.dataset.append(WorkBlock(dt.datetime(2020,4,21,7,0),dt.datetime(2020,4,21,8,0)))
        self.dataset.append(WorkBlock(dt.datetime(2020,4,21,9,0),dt.datetime(2020,4,21,9,0)))
        self.dataset.append(WorkBlock(dt.datetime(2020,4,21,11,0),dt.datetime(2020,4,21,12,0)))
        self.dataset.append(WorkBlock(dt.datetime(2020,4,21,13,0),dt.datetime(2020,4,21,14,30)))
        self.dataset.append(WorkBlock(dt.datetime(2020,4,21,15,0),dt.datetime(2020,4,21,16,45)))
    
    def addsingleblock(self):
        blocktosave = self.dataset[0]
        print(blocktosave)
        self.service.addBlock(blocktosave)
        blocksfromstorage = self.service.getBlocksForDate(dt.date (2020,4,21))
        print(blocksfromstorage)

    def addtwoblocks(self):
        firstblocktosave = self.dataset[0]
        print(firstblocktosave)
        secondblocktosave = self.dataset[0]
        print(secondblocktosave)
        self.service.addBlock(firstblocktosave)
        self.service.addBlock(secondblocktosave)
        blocksfromstorage = self.service.getBlocksForDate(dt.date (2020,4,21))
        print(blocksfromstorage)


test = WorkBlockStorageServiceTest()
test.addsingleblock()
# test.addtwoblocks()