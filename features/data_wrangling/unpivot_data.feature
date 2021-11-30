Feature: Preparing data
    As a member of the team preparing the data
    I want to be able to unpivot the raw data
    So that I can work with it in more flexible way when performing analysis and building reports

    Background:
        Given we are working on the downloaded World Bank dataset

    Scenario: Unpivoting the data
        Given we have the following input dataset
            | Country Name | Country Code | Series Name        | Series Code       | 1960    | 1961    |
            | Afghanistan  | AFG          | Population, female | SP.POP.TOTL.FE.IN | 4347394 | 4439156 |
            | Albania      | ALB          | Population, male   | SP.POP.TOTL.MA.IN | 827031  | 853181  |
        When we unpivot the data
        Then we expect the resulting dataset to be
            | Country Name | Country Code | Series Name        | Series Code       | Year | Metric  |
            | Afghanistan  | AFG          | Population, female | SP.POP.TOTL.FE.IN | 1960 | 4347394 |
            | Albania      | ALB          | Population, male   | SP.POP.TOTL.MA.IN | 1960 | 827031  |
            | Afghanistan  | AFG          | Population, female | SP.POP.TOTL.FE.IN | 1961 | 4439156 |
            | Albania      | ALB          | Population, male   | SP.POP.TOTL.MA.IN | 1961 | 853181  |
        And the resulting dataset should have 4 records