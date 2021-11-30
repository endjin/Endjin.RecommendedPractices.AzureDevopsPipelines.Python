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

@then("we expect the resulting dataset to be")
def compare_datasets(context):
    context.expected_result = BehaveHelper.table_to_dataframe(context.table)
    assert_frame_equal(context.result, context.expected_result, check_like=True, check_index_type=False)

@then('the resulting dataset should have {column_count:d} columns')
def check_column_count(context, column_count):
    assert context.result.shape[1] == column_count