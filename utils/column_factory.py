from . import constants


def create_standard_varchar_column(column_name):
    return constants.STANDARD_VARCHAR_COLUMN.format(column_name, constants.STANDARD_VARCHAR_COLUMN)


def create_columns(columns):
    merged_columns = ''
    for i in range(0, len(columns)):
        if i == len(columns) - 1:
            merged_columns = merged_columns + columns[i]
        else:
            merged_columns = merged_columns + columns[i] + ','
    return merged_columns
