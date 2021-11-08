from behave import *
import pandas as pd
from project_name.dataframe_operations import DataframeOperations


@given("My employee records are")
def extract_employee_records(context):
    list_of_records = []
    for row in context.table:
        list_of_records.append(dict(zip(row.headings, row.cells)))
    context.employee_records = pd.DataFrame.from_records(list_of_records)


@when("I count female employees")
def get_count_of_females(context):
    context.result = DataframeOperations.count_females(context.employee_records)


@then("I expect a count of {expected_result:d}")
def check_result(context, expected_result):
    assert isinstance(expected_result, int)
    assert expected_result == context.result
