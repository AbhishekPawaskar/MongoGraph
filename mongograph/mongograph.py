import os
import sys
from database.database import DataBaseController

class MongoGraph:
    def __init__(self,connection_string:str):
        try:
            if (os.name != 'nt') and (os.name != 'posix'):
                raise OSError('UNSUITABLE OS ')

            self.__mongo_controller = DataBaseController(mongodb_url=connection_string)
                
        except Exception as initialization_error:
            raise RuntimeError('INITIALIZATION ERROR') from initialization_error
    