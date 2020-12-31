# Pipeline to publish Python packages

## Status

Proposed.

## Context

Based on my experience over the last year using Python in a data science context, functionality typically begins life in a Jupyter notebook.  There then comes a point where some of that functionality will then be:

1. Promoted into a production environment, and/or;
1. Re-used across multiple projects within Jupyter to provide tooling in areas such as ingestion, wrangling / feature engineering or exploration / analysis.

There then comes the need to "productionise" the code - for example:

1. Encapsulation of code in appropriate project / class structure with a view to building core set of re-useable fucntionality;
1. Dependency management - including managing packages that are "dev only";
1. Automated unit tests / test coverage analysis;
1. Linting;
1. Publlishing as a Python package that can imported in multiple use cases : Jupter notebooks, Spark jobs and other operational processes as a first class citizen alongside 3rd party Python packages.

## Decision

Develop a best practice Azure DevOps pipeline (and associated documentation) that will enable a Python repository to be developed and deployed as an Azure DevOps Artefact.

Some of the key elements are set out here: [Build Python apps](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python?view=azure-devops)

But I think we can improve on that!

## Consequences

This has the following benefits:

- It will enable Endjin to productionise, package up and publish its own Python based IP;
- It is a stand alone set of tools / scritps / documentation that could be open sourced to help others adopt Azure DevOps successfully and attract wider community input / interest;
- It will become part of the tooling to support the Modern Data Platform - e.g. to enable clients to rapidly spin up repos / pipelines for their own Python based functions.
