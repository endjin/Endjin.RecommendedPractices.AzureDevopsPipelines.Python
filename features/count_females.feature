Feature: Gender equality
    As a memeber of the corporate and social responsibility team.
    I want to be able to count the number of females in a population.
    So that I can analyse gender equality metrics.

    Scenario: Counting females
        Given My employee records are
            | Name       | Title           | Gender |
            | Bob Smith  | Engineer        | Male   |
            | Liz Brown  | Project Manager | Female |
            | Alex White | Analyst         | Female |

        When I count female employees

        Then I expect a count of 2
