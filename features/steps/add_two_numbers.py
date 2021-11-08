from behave import *
from project_name.sample_module import SampleClass


@given("My first number is {first_number:d}")
def check_first_number(context, first_number):
    context.first_number = first_number
    assert isinstance(first_number, int)

@given("My second number is {second_number:d}")
def check_second_number(context, second_number):
    context.second_number = second_number
    assert isinstance(second_number, int)

@when("I add those numbers")
def call_simple_method(context):
    context.result = SampleClass.sample_method(context.first_number, context.second_number)

@then("I expect a result of {expected_result:d}")
def check_result(context, expected_result):
    assert isinstance(expected_result, int)
    assert expected_result == context.result
