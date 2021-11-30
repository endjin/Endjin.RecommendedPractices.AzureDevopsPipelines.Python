Feature: Prepare data
    As a member of the team preparing the data
    I want to be able to standardise the format of the years in the raw data
    So that I can work with it in more flexible way when performing analysis and building reports

    Background:
        Given we are working on the downloaded World Bank dataset
        
    Scenario: Standardise the format of the values in the Years column
        Given we have the following input dataset
            | Country Name | Country Code | Series Name        | Series Code       | Year          | Metric  |
            | Afghanistan  | AFG          | Population, female | SP.POP.TOTL.FE.IN | 1960 [YR1960] | 4347394 |
            | Afghanistan  | AFG          | Population, female | SP.POP.TOTL.FE.IN | 1961 [YR1961] | 4439156 |
        When we standardise the format of the years
        Then we expect the resulting dataset to be
            | Country Name | Country Code | Series Name        | Series Code       | Year | Metric  |
            | Afghanistan  | AFG          | Population, female | SP.POP.TOTL.FE.IN | 1960 | 4347394 |
            | Afghanistan  | AFG          | Population, female | SP.POP.TOTL.FE.IN | 1961 | 4439156 |