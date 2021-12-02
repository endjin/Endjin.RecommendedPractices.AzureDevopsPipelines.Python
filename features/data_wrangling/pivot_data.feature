Feature: Preparing data
    As a member of the team preparing the data
    I want to be able to pivot the data
    So that I can work with it in more flexible way when performing analysis and building reports

    Background:
        Given we are working on the downloaded World Bank dataset

    Scenario: Pivoting the data
        Given we have the following input dataset
            | Country Name | Country Code | Series Name                  | Series Code       | Year | Metric           |
            | Afghanistan  | AFG          | GDP (current US$)            | NY.GDP.MKTP.CD    | 1960 | 537777811.111111 |
            | Afghanistan  | AFG          | GDP per capita (current US$) | NY.GDP.PCAP.CD    | 1960 | 59.7732337032148 |
            | Afghanistan  | AFG          | Population, female           | SP.POP.TOTL.FE.IN | 1960 | 4347394          |
        When we pivot the data
        Then we expect the resulting dataset to be
            | Country Name | Country Code | Year | GDP (current US$) | GDP per capita (current US$) | Population, female |
            | Afghanistan  | AFG          | 1960 | 537777811.111111  | 59.7732337032148             | 4347394            |
        And the resulting dataset should have 1 records