from behave.model import Table
from pandas import DataFrame, to_datetime, to_numeric


class BehaveHelper:
    
    @staticmethod
    def table_to_dataframe(table: Table) -> DataFrame:

        list_of_records = []
        for row in table:
            list_of_records.append(dict(zip(row.headings, row.cells)))
        return DataFrame.from_records(list_of_records)

    # Used this super useful article:
    # https://stackoverflow.com/questions/15891038/change-column-type-in-pandas
    @staticmethod
    def column_to_numeric(column_name: str, df: DataFrame) -> DataFrame:

        df[column_name] = to_numeric(df[column_name], errors='coerce')
        return df

    @staticmethod
    def column_to_datetime(column_name: str, df: DataFrame) -> DataFrame:

        df[column_name] = to_datetime(df[column_name], errors='coerce')
        return df

