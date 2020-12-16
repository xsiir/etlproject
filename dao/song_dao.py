from dao.database_manager import DatabaseManager
from utils.properties_util import get_property
from utils import constants


class SongDAO:

    def __init__(self):
        self.__database_manager = DatabaseManager()

    def find_most_popular_artists(self, count):
        artist_column_name = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_ARTIST_NAME_COLUMN_NAME_KEY),
        result = self.__database_manager.select(self.__find_most_popular(count, artist_column_name))
        return result

    def find_most_popular_tiles(self, count):
        title = get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_TITLE_NAME_COLUMN_NAME_KEY),
        result = self.__database_manager.select(self.__find_most_popular(count, title))
        return result

    def __find_most_popular(self, count, searched_column_name):
        database_name = get_property(constants.DATABASE_CONFIG_DOMAIN, constants.DATABASE_SERVER_NAME)
        database_schema = get_property(constants.DATABASE_CONFIG_DOMAIN, constants.DATABASE_SCHEMA)
        table_origin = '{}.{}'.format(database_name, database_schema)

        query = constants.SELECT_MOST_POPULAR_BAND.format(
            count,
            table_origin,
            searched_column_name[0],
            get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_TABLE_NAME_KEY),
            get_property(constants.TABLES_DETAILS_DOMAIN, constants.PLAYLIST_HISTORY_TABLE_NAME_KEY),
            get_property(constants.TABLES_DETAILS_DOMAIN, constants.COVER_SONG_ID_COLUMN_NAME_KEY),
            get_property(constants.TABLES_DETAILS_DOMAIN, constants.PLAYLIST_HISTORY_SONG_ID_COLUMN_NAME_KEY)
        )
        return query
