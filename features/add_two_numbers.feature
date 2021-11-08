Feature: Adding up numbers
    As a memeber of the accounts team.
    I want to be able to add up numbers.
    So that I can calculate account balances.

    Scenario: Adding two numbers
        Given My first number is 1
        And My second number is 2

        When I add those numbers

        Then I expect a result of 3
