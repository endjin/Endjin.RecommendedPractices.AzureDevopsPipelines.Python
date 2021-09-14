# Endjin.RecommendedPractices.AzureDevopsPipelines.Python

Repository to capture best practice tooling for Python based developments.

## Installation on a vanilla Windows device

Getting my initial thoughts down here about a manual process for setting up an environment using best practice approach.  The idea being that it can then be migrated into a best practice pipeline for Azure DevOps.

### Install Python

Install Python, the latest version can be downloaded from [python.org](https://www.python.org/downloads/)

Note - during the installation process choose the "Add Python X.X to PATH" option.

Check the installation by opening a terminal and running the following command:

`python --version`

### Install Git

Download and install Git from [the official Git web site](https://git-scm.com/downloads).

Check the installation of Git by running the following command:

`git --version`

There are some steps you need to take to [get started with Git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

The core ones being setting your git user and email address, this is required for pushing changes to a remote repository:

`git config --global user.name "John Doe"`
`git config --global user.email johndoe@example.com`

### Pull down repository from GitHub

Clone the template project from GitHub.  From a local directory where we you want to host your repos, such as `%HOMEPATH%\repos` run the following command:

`git clone <URL path to the repository>`

### Set up environment

Change directory into root of the cloned repo.

Use 'pip' (package installer for Python) to upgrade to the latest version of pip and pipenv:

`python -m pip install --upgrade pip pipenv`

Now lauch 'pipenv' shell - this will auotmatically create virtual environment:

`pipenv shell`

Now install dependencies using the `--dev` extensions so that development packages such as pytest, flake8 and the packaing tools are included.  This installs the packages defined in the Pipfile and Pipfile.lock files.

`pipenv install --dev`

The following commands are useful to visualise the packages that are installed and the dependencies between them:

`pipenv graph`
`pipend graph --reverse`

### Installing new packages

For packages required in production use:

`pipenv install <package name>`

For packages only required for development use:

`pipenv install <package name> --dev`

## Pre-installed packages

The following tools are pre-packaged with this template project:

### Packaging tools

Install setuptools which is used to prepare a Python package:
`pipenv install --dev setuptools`

Install pipenv-setup which enables the the creation and management of setup.py file that governs how the Python code is packaged using setuptools:
`pipenv install --dev pipenv-setup`

To ensure the setup.py file is synchronized with the pipfile, issue the following command:
`pipenv-setup sync`

To create a packaged installation, run the following command:
`pipenv run python setup.py sdist bdist_wheel`

Install wheel which is used to zip up the package ready for deployment:
`pipenv install --dev wheel keyring artifacts-keyring`

There are some pre-requisites to the following command, such as setting up environemnt variables containing credentials - see https://twine.readthedocs.io/en/latest/.

Publish the wheel artefact:
`pipenv run twine upload dist/* --non-interactive`

### Linting

Use flake8 to check the code meets consistent standards.  Also recommend installing this as a Python linting plug-in for VS Code.

`pipenv install flake8 --dev`

Note : see entry in `setup.cfg` for linting configuration.

To run linting tests:

`pipenv run flake8`

### Testing

Use pytest for automated testing:

`pipenv install pytest --dev`

Note : see entry in `setup.cfg` for test configuration.  Current assumption is that tests will reside in `.\test` folder.

To run the tests:

`pipenv run pytest`

Add the following tooling to measure test coverage:

`pipenv install pytest-cov --dev`

The `pytest-cov` tool is governed by the following file `.coveragerc` file.

### Packaging

The following command will package up the Python package so that it can be published:

`pipenv run python setup.py sdist bdist_wheel`

### Publishing

The following command uses Twine to publish the package to the Azure Devops Artefacts repository so that it can be consumed by Python package installer `pip` or `pipenv`.

`pipenv run twine upload dist/* --repository-url <Azure DevOps Artefect Repository URL>`

### Pre-commit : not sure about this!

See the configuration file `.pre-commit-config.yaml`.  This will run a bunch of tests and checks before allowing code to be committed.

### Black : not sure about this!

### isort : ditto not sure about this either!

