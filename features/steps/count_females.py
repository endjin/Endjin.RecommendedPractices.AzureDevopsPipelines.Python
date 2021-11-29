from behave import given, when, then
from pandas import DataFrame
from project_name.utilities import BehaveHelper
from project_name.dataframe_operations import DataframeOperations


@given("My employee records are")
def extract_employee_records(context):
    context.employee_records = BehaveHelper.table_to_dataframe(context.table)
    assert isinstance(context.employee_records, DataFrame)

@when("I count female employees")
def get_count_of_females(context):
    context.result = DataframeOperations.count_females(context.employee_records)


@then("I expect a count of {expected_result:d}")
def check_result(context, expected_result):
    assert isinstance(expected_result, int)
    assert expected_result == context.result
