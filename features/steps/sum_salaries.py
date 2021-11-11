from behave import given, when, then
from pandas import DataFrame
from project_name.utilities import BehaveHelper
from project_name.dataframe_operations import DataframeOperations


@given('The "{column_name}" column is numeric')
def make_column_numeric(context, column_name):
    context.employee_records = BehaveHelper.column_to_numeric(column_name, context.employee_records)
    assert isinstance(column_name, str)

@when("I sum the salaries")
def get_count_of_females(context):
    context.result = DataframeOperations.sum_salaries(context.employee_records)

@then("I expect a result of {expected_result:d}")
def check_result(context, expected_result):
    assert isinstance(expected_result, int)
    assert expected_result == context.result
