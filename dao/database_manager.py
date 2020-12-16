import pyodbc
from utils import constants
from decorator.singleton import Singleton
from utils.properties_util import get_property


class DatabaseManager(metaclass=Singleton):

    def __init__(self):
        self.__cnxn = pyodbc.connect(self.getConnectionDetails())
        self.__crsr = self.__cnxn.cursor()
        self.__crsr.fast_executemany = True

    def __del__(self):
        self.__crsr.close()
        self.__cnxn.close()

    def commit(self):
        self.__cnxn.commit()

    def executeMany(self, sql, data):
        self.__crsr.executemany(sql, data)

    def select(self, sql):
        return self.__crsr.execute(sql)

    def getConnectionDetails(self):
        return constants.CONNECTION_PROPERTIES.format(
            get_property('db_config', 'driver'),
            get_property('db_config', 'server_name'),
            get_property('db_config', 'database_name'),
            get_property('db_config', 'username'),
            get_property('db_config', 'password')
        )
