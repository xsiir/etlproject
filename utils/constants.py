# -- C
CONNECTION_PROPERTIES = 'DRIVER={{{0}}};\
            SERVER={1};\
            DATABASE={2};\
            Trusted_Connection=no;\
            uid={3};\
            pwd={4}'

# -- CONSTANTS FOR PROPERTIES --- #
FILE_CONFIG_DOMAIN = "file_config"
FILE_PATHS_DOMAIN = "paths"
APPLICATION_PROPERTIES_DOMAIN = "app_properties"

UNIQUE_TRACKS_PATH = "unique_tracks_path"
PLAYLIST_HISTORY_PATH = "triplets_sample_path"
ENCODING_FORMAT_KEY = "encoding_format"
END_LINE_SIGN_KEY = "new_line_code"
FIELD_SEPARATOR_KEY = "field_separator"
BATCH_SIZE_KEY = "batch_size"
USE_BATCH = "use_batch"

DATABASE_CONFIG_DOMAIN = "db_config"
DATABASE_SERVER_NAME = "database_name"
DATABASE_SCHEMA = "database_schema"

TABLES_DETAILS_DOMAIN = "db_tables"
# -- First Table - ##
COVER_TABLE_NAME_KEY = "unique_tracks_table"
COVER_ID_COLUMN_NAME_KEY = "cover_id"
COVER_SONG_ID_COLUMN_NAME_KEY = "cover_song_id"
COVER_ARTIST_NAME_COLUMN_NAME_KEY = "cover_artist_name"
COVER_TITLE_NAME_COLUMN_NAME_KEY = "cover_song_title"
# -- Second Table --#
PLAYLIST_HISTORY_TABLE_NAME_KEY = "triplets_sample_table"
PLAYLIST_HISTORY_USER_ID_NAME_KEY = "playlist_history_user_id"
PLAYLIST_HISTORY_SONG_ID_COLUMN_NAME_KEY = "playlist_history_song_id"
PLAYLIST_HISTORY_DATE_COLUMN_NAME_KEY = "playlist_history_date"

# -- DATABASE QUERIES -- #
INSERT_INTO = "INSERT INTO {0} VALUES({1})"

##
# 1) How many rows should be shown
# 2) ServerName.Schema
# 3) Artist name column name
# 4) Source table
# 5) Join table
# 6) Song id column name from source table
# 7) Song id column name from join table
SELECT_MOST_POPULAR_BAND = """
SELECT TOP {0} covers.{2}, COUNT(*) FROM {1}.{3} covers
LEFT JOIN {1}.{4} history ON covers.{5} = history.{6}
GROUP BY covers.{2} ORDER BY COUNT(*) DESC
"""

CREATE_TABLE = "CREATE TABLE {}.{}({})"
COLUMN = "{} {}"

STANDARD_VARCHAR_COLUMN = "{} nvarchar(500)"
