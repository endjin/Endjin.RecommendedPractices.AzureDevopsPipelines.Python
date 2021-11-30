from behave.model import Table
from pandas import DataFrame, to_datetime, to_numeric
import numpy as np


class BehaveHelper:

    @classmethod
    def table_to_dataframe(cls, table: Table) -> DataFrame:

        list_of_records = []
        for row in table:
            list_of_records.append(dict(zip(row.headings, row.cells)))
        df = DataFrame.from_records(list_of_records)
        return cls.parse_nan_strings(df)

    @staticmethod
    def parse_nan_strings(df: DataFrame) -> DataFrame:
        return df.replace(to_replace='NaN', value=np.nan)

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

