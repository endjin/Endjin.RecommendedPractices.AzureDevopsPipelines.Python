Feature: Preparing data
    As a member of the team preparing the data
    I want to be able to assign the value to the empty cells in the raw data
    So that I can work with it in more flexible way when performing analysis and building reports

    Background:
        Given we are working on the downloaded World Bank dataset

    Scenario: Fill empty cells
        Given we have the following input dataset
            | Country Name | Country Code | Series Name                  | Series Code    | Year | Metric           |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1990 | 948.338177965671 |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1991 | NaN              |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1992 | NaN              |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1993 | NaN              |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1994 | 251.078348367302 |
        When we fill the empty cells using forward fill
        Then we expect the resulting dataset to be
            | Country Name | Country Code | Series Name                  | Series Code    | Year | Metric           |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1990 | 948.338177965671 |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1991 | 948.338177965671 |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1992 | 948.338177965671 |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1993 | 948.338177965671 |
            | Angola       | AGO          | GDP per capita (current US$) | NY.GDP.PCAP.CD | 1994 | 251.078348367302 |