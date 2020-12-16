from dao.database_manager import DatabaseManager
from utils.properties_util import get_property
from decorator.time_counter import time_counter
from utils import constants


class FileLoader:
    __BATCH_SIZE = int(get_property(constants.APPLICATION_PROPERTIES_DOMAIN, constants.BATCH_SIZE_KEY))

    def __init__(self, encoding_format, column_separator):
        self.__database_manager = DatabaseManager()
        self.__item_processed = 0
        self.__inMemoryRecords = []
        self.__encoding_format = encoding_format
        self.__column_separator = column_separator

    @time_counter
    def to_database_from_file(self, file_path, table, columns):

        print("Zaczynam wczytywanie...")
        with open(file_path, encoding=self.__encoding_format) as fileContent:
            for line in fileContent:
                if self.__if_use_batch() and self.__if_records_in_memory_equals_to_batch_size():
                    self.__insert_items_to_database(table, columns)
                    self.__clear_precessed_items()
                self.__inMemoryRecords.append(self.__getColumnsPerRecord(line))
                self.__item_processed = self.__item_processed + 1
        self.__insert_items_to_database(table, columns)
        self.__clear_precessed_items()

        print("Koncze wczytywanie...")
        pass

    def __get_prepared_insert_statement(self, table, columns):

        values_gaps = ""
        for i in range(columns):
            if i == columns - 1:
                values_gaps += "?"
            else:
                values_gaps += "?,"

        statement = constants.INSERT_INTO.format(table, values_gaps)
        return statement

    def __if_use_batch(self):
        return bool(get_property(constants.APPLICATION_PROPERTIES_DOMAIN, constants.USE_BATCH))

    def __if_records_in_memory_equals_to_batch_size(self):
        return self.__item_processed == FileLoader.__BATCH_SIZE

    def __insert_items_to_database(self, table, columns):
        prepared_insert_statement = self.__get_prepared_insert_statement(table, columns)
        self.__database_manager.executeMany(prepared_insert_statement, self.__inMemoryRecords)
        self.__database_manager.commit()

    def __clear_precessed_items(self):
        self.__inMemoryRecords = []
        self.__item_processed = 0
        pass

    def __getColumnsPerRecord(self, textLine):
        # Remove \n from the end of line
        line_without_end_line_sign = textLine.rstrip('\n')
        return line_without_end_line_sign.split(self.__column_separator)
