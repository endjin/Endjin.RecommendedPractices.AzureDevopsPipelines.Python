Feature: Preparing data
    As a member of the team preparing the data
    I want to be able to log the GDP per capita
    So that I can work with it in more flexible way when performing analysis and building reports

    Background:
        Given we are working on the downloaded World Bank dataset

    Scenario: Computing the log10 of the data
        Given we have the following input dataset
            | Country Name | Country Code | Year | GDP per capita (current US$) |
            | Afghanistan  | AFG          | 1960 | 59.7732337032148             |
            | Afghanistan  | AFG          | 1961 | 59.8608999923829             |
        When we compute the log10 of the data
        Then the 'log10 GDP per capita (current US$)' is the log10 of the 'GDP per capita (current US$)'