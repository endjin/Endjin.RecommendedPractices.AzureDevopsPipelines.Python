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

The goal is to enable a user to create a best practice Python development environment from first principles in a few simple steps:

- Follow documentation to check / install a few prerequisites such as Python, Git and VS Code;
- Pull down and configure the template project;
- Then run a setup script so that within 5 minutes they have a new repo set up with all of the core development tools in place, an automated CICD pipeline configured and an IDE with all of the productivity tools activated.

## Decision

Develop a best practice Azure DevOps pipeline (and associated documentation) that will enable a Python repository to be developed and deployed as an Azure DevOps Artefact.

Some of the key elements are set out here: [Build Python apps](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python?view=azure-devops)

But I think we can improve on that!

Here are some of the short

Candidates that I think should be considered as improvements to the current approach documented by Microsoft:

- Use of Python.org's recommended approach for managing dependencies - a tool called pipenv.  For more information, this [article](https://realpython.com/pipenv-guide/) explains the problems that it addresses.  Microsoft do apply pipenv in other Python examples but not in this documentation;

- Setting up a comprehensive setup.py template which is the script that governs how the code is packaged and the meta data for the published package such as links to documentation;

- Potentially look at use of pipenv-setup which helps to take out some of the manual steps / risk in creating the setup.py file above;

- Creating a project template that can be downloaded and easily configured to bootstrap a new Python repo with all of the best practice elements such as .yaml file for pipeline in place from day one.  Python has a tool called [cookiecutter](https://github.com/cookiecutter/cookiecutter) to enable this, but there may be more generic approaches;

- Automate some of the manual steps - eg creating the Azure DevOps Artefact into which the Python package can be published;

- Some decisions to be made around operating systems to use for build servers - this in turn can impact the approach taken to managing dependencies using pipenv as some lower level dependencies are operating system specific;

- Rolling in other tools to the template - eg use of [black](https://pypi.org/project/black/) for implementing consistent code formatting over and above the linting;

- Adding badges for version, test coverage etc.

- Clear documentation that walks a developer through the simple steps to set this up from first principles : thinking here about enabling a client to onboard their team with Python for the first time as part of a wider MDP project.

## Consequences

This has the following benefits:

- It will enable Endjin to productionise, package up and publish its own Python based IP;
- It is a stand alone set of tools / scripts / documentation that could be open sourced to help others adopt Azure DevOps successfully and attract wider community input / interest;
- It will become part of the tooling to support the Modern Data Platform - e.g. to enable clients to rapidly spin up repos / pipelines for their own Python based functions.
