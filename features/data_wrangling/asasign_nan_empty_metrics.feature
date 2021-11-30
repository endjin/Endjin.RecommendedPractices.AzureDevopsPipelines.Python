Feature: Preparing data
    As a member of the team preparing the data
    I want to be able to assign the value NaN to the values showing as ".." in the raw data
    So that I can work with it in more flexible way when performing analysis and building reports

    Background:
        Given we are working on the downloaded World Bank dataset

    Scenario: Assign NaN values to cells containg '..''
        Given we have the following input dataset
            | Country Name | Country Code | Series Name                                         | Series Code       | Year          | Metric  |
            | Albania      | ALB          | Life expectancy at birth, total (years)             | SP.DYN.LE00.IN    | 1960 [YR1960] | 62.283  |
            | Albania      | ALB          | Current health expenditure per capita (current US$) | SH.XPD.CHEX.PC.CD | 1960 [YR1960] | ..      |
            | Albania      | ALB          | GDP per capita (current US$)                        | NY.GDP.PCAP.CD    | 1960 [YR1960] | ..      |
            | Algeria      | DZA          | Population, female                                  | SP.POP.TOTL.FE.IN | 1960 [YR1960] | 5499822 |
        When we assign NaN values to cells containing '..'
        Then we expect the resulting dataset to be
            | Country Name | Country Code | Series Name                                         | Series Code       | Year          | Metric  |
            | Albania      | ALB          | Life expectancy at birth, total (years)             | SP.DYN.LE00.IN    | 1960 [YR1960] | 62.283  |
            | Albania      | ALB          | Current health expenditure per capita (current US$) | SH.XPD.CHEX.PC.CD | 1960 [YR1960] | nan     |
            | Albania      | ALB          | GDP per capita (current US$)                        | NY.GDP.PCAP.CD    | 1960 [YR1960] | nan     |
            | Algeria      | DZA          | Population, female                                  | SP.POP.TOTL.FE.IN | 1960 [YR1960] | 5499822 |