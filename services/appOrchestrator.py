
from services.appService import AppService

# this class is responsible for handling some of the common user flows

class AppOrchestrator:

    def __init__(self, appService: AppService):
        self.__appService = appService

    