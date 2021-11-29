Feature: Salary operations
    As a memeber of the HR team.
    I want to be able to sum up employees salaries.
    So that I can understand the total payroll for the firm.

    Scenario: Sum salaries
        Given My employee records are
            | Name       | Title           | Salary |
            | Bob Smith  | Engineer        | 35000  |
            | Liz Brown  | Project Manager | 55000  |
            | Alex White | Analyst         | 42000  |
        And The "Salary" column is numeric

        When I sum the salaries

        Then I expect a result of 132000
