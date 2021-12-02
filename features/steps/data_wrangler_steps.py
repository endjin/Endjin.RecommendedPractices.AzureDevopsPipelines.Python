from pandas.testing import assert_frame_equal
from behave import given, when, then
from project_name.utilities import BehaveHelper
from worldbank_data.data_wrangler import DataWrangler

@given("we are working on the downloaded World Bank dataset")
def initialise_data_wrangler(context):
    context.data_wrangler = DataWrangler()

@given("we have the following input dataset")
def extract_dataset(context):
    context.input_dataset = BehaveHelper.table_to_dataframe(context.table)

@given("the data in the GDP per capita column is of type string")
def get_column(context):
    context.input_column = 'GDP per capita (current US$)'

@when("we assign NaN values to cells containing '..'")
def assign_NaN_values(context):
    context.result = context.data_wrangler.assign_nan_empty_metrics(context.input_dataset)

@when("we fill the empty cells using forward fill")
def forward_fill_cells(context):
    context.result = context.data_wrangler.fill_empty_cells(context.input_dataset)

@when("we standardise the format of the years")
def years_format(context):
    context.result = context.data_wrangler.clean_years(context.input_dataset)

@when("we unpivot the data")
def unpivot_data(context):
    context.result = context.data_wrangler.unpivot_data(context.input_dataset)

@when("we pivot the data")
def pivot_data(context):
    context.result = context.data_wrangler.pivot_data(context.input_dataset)

@when("we convert the data to a type of float")
def string_to_float(context):
    context.result = context.data_wrangler.convert_to_float(context.input_dataset, context.input_column)

@then("we expect the resulting dataset to be")
def compare_datasets(context):
    context.expected_result = BehaveHelper.table_to_dataframe(context.table)
    assert_frame_equal(context.result, context.expected_result, check_like=True, check_index_type=False)

@then('the resulting dataset should have {record_count:d} records')
def check_record_count(context, record_count):
    assert context.result.shape[0] == record_count

@then("the 'GDP per capita (current US$)' column is of type float")
def check_type_float(context):
    assert context.input_dataset[context.input_column].dtypes == float