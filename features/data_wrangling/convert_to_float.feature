Feature: Preparing data
    As a member of the team preparing the data
    I want to be able to convert the data from a string to a float
    So that I can work with it in more flexible way when performing analysis and building reports

    Background:
        Given we are working on the downloaded World Bank dataset

    Scenario: Converting the data to a float
        Given we have the following input dataset
            | Country Name | Country Code | Year | GDP per capita (current US$) |
            | Afghanistan  | AFG          | 1960 | 59.7732337032148             |
            | Afghanistan  | AFG          | 1961 | 59.8608999923829             |
        And the data in the GDP per capita column is of type string
        When we convert the data to a type of float
        Then the 'GDP per capita (current US$)' column is of type float
