# Endjin.RecommendedPractices.AzureDevopsPipelines.Python

Repository to capture best practice tooling for Python based developments.

## Installation on a vanilla Windows device

Getting my initial thoughts down here about a manual process for setting up an environment using best practice approach.  The idea being that it can then be migrated into a best practice pipeline for Azure DevOps.

### Install Python

Install Python, the latest version can be downloaded from [python.org](https://www.python.org/downloads/)

Note - during the installation process choose the "Add Python X.X to PATH" option.

Check the installation by opening a terminal and running the following command:

`python --version`

### Pull down repository from GitHub

Clone the template project from GitHub.

### Set up environment

Use 'pip' (pacakge installer for Python) to upgrade to the latest version of pip:

`python -m pip install --upgrade pip`

Now install 'pipenv':

`pip install pipenv`

Now lauch 'pipenv' shell - this will auotmatically create virtual environment:

`pipenv shell`

Now install dependencies using the `--dev` extensions so that development packages such as pytest, flake8 and the packaing tools are included.

`pipenv install --dev`

The following commands are useful to visualise the packages that are installed and the dependencies between them:

`pipenv graph`
`pipend graph --reverse`

## Installing new packages

For packages required in production use:

`pipenv install <package name>`

For packages only required for development use:

`pipenv install <package name> --dev`

## Pre-installed packages

The following tools are pre-packaged with this template project:

### Packaging tools

Install setuptools which is used to prepare a Python package:
`pipenv install --dev setuptools`

Install wheel which is used to zip up the package ready for deployment:
`pipenv install --dev wheel`

Install pipenv-setup which enables the the creation and management of setup.py file that governs how the Python code is packaged using setuptools:
`pipenv install --dev pipenv-setup`

To ensure the setup.py file is synchronized with the pipfile, issue the following command:
`pipenv-setup sync`

### Linting

Use flake8 to check the code meets consistent standards.  Also recommend installing this as a Python linting plug-in for VS Code.

`pipenv install flake8 --dev`

Note : see entry in `setup.cfg` for linting configuration.

To run linting tests:

`pipenv run flake8`

## Testing

Use pytest for automated testing:

`pipenv install pytest --dev`

Note : see entry in `setup.cfg` for test configuration.  Current assumption is that tests will reside in `.\test` folder.

To run the tests:

`pipenv run pytest`

Add the following tooling to measure test coverage:

`pipenv install pytest-cov --dev`

The `pytest-cov` tool is governed by the following file `.coveragerc` file.

## Pre-commit

See the configuration file `.pre-commit-config.yaml`.  This will run a bunch of tests and checks before allowing code to be committed.

## Black : not sure about this!

## isort : ditto not sure about this either!

