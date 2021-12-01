import pandas as pd
import numpy as np
from pathlib import Path
import csv
    
class DataWrangler:
    def __init__(
        self,
        input_folder_path="./data_input",
        output_folder_path="./data_output",
        # master_data_file_path="./data_input/master_data/master_data.xlsx",,
    ):

        self.input_folder_path = Path(input_folder_path)
        self.output_folder_path = Path(output_folder_path)

    def load_mapping(self, mapping_file):
        mapping = self.load_raw_data_from_excel(mapping_file)
        return mapping.loc[:, ['Code', 'Region']]


    def load_and_apply_mapping(self, df, filename):
        mapping = self.load_mapping(filename)
        # df = df.map(mapping)
        df = df.merge(mapping, left_on = "Country Code", right_on = "Code", how='left')
        return df


    def load_raw_data_from_excel(self, filename):
        return pd.read_csv(
            Path(self.input_folder_path, filename)).iloc[:-5]

    def unpivot_data(self, df):

        # var_columns = self.get_list_of_data_columns(df)
        id_vars = ['Country Name', 'Country Code', 'Series Name', 'Series Code']
        var_name = 'Year'
        value_name = 'Metric'

        return df.melt(
            id_vars=id_vars,
            var_name=var_name,
            value_name=value_name
        )

    def clean_years(self, df):
        df['Year'] = df['Year'].str[:4]
        return df

    def assign_nan_empty_metrics(self, df):
        df['Metric'] = df['Metric'].replace('..', np.nan)
        return df

    def fill_empty_cells(self, df):
        df['Metric'] = df.groupby(['Country Name', 'Series Name'])['Metric'].ffill()
        return df

    def data_to_log(self, df, columnname):
        df[columnname] = np.log10(df[columnname])
        return df

    def convert_to_float(self, df, columnname):
        df[columnname] = df[columnname].astype(float)
        return df
