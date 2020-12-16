import pyodbc
from utils import constants
from decorator.singleton import Singleton
from utils.properties_util import get_property
from utils.column_factory import create_standard_varchar_column, create_columns


class DatabaseManager(metaclass=Singleton):

    def __init__(self):
        self.__cnxn = pyodbc.connect(self.getConnectionDetails())
        self.__crsr = self.__cnxn.cursor()
        self.__crsr.fast_executemany = True
        self.__initialize_covers_database()
        self.__initialize_playlist_history_database()

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

    def __initialize_covers_database(self):
        cover_id = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_ID_COLUMN_NAME_KEY)
        cover_song_id = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_SONG_ID_COLUMN_NAME_KEY)
        artist_name = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_ARTIST_NAME_COLUMN_NAME_KEY)
        title = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_TITLE_NAME_COLUMN_NAME_KEY)

        table_name = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_TABLE_NAME_KEY)

        self.__execute_create_table_query([cover_id, cover_song_id, artist_name, title], table_name)


    def __initialize_playlist_history_database(self):
        user_id = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_ID_COLUMN_NAME_KEY)
        song_id = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_SONG_ID_COLUMN_NAME_KEY)
        play_date = get_property(constants.TABLES_DETAILS_DOMAIN, constants.PLAYLIST_HISTORY_DATE_COLUMN_NAME_KEY)

        table_name = get_property(constants.TABLES_DETAILS_DOMAIN, constants.PLAYLIST_HISTORY_TABLE_NAME_KEY)

        self.__execute_create_table_query([user_id, song_id, play_date], table_name)

    def __execute_create_table_query(self, column_names, table_name):

        columns = []
        for column_name in column_names:
            columns.append(create_standard_varchar_column(column_name))

        merged_columns = create_columns(columns)
        database_name = get_property(constants.DATABASE_CONFIG_DOMAIN, constants.DATABASE_SERVER_NAME)
        database_schema = get_property(constants.DATABASE_CONFIG_DOMAIN, constants.DATABASE_SCHEMA)
        table_origin = '{}.{}'.format(database_name, database_schema)

        query = constants.CREATE_TABLE.format(table_origin, table_name, merged_columns)
        print(query)
        self.__crsr.execute(query)
