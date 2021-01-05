# Python dependency management approach

## Status

Proposed.

## Context

This ADR concerns a core element of [0001-pipeline-to-publish-python-packages](.\0001-pipeline-to-publish-python-packages.md)

There are two broad approaches for managing package dependencies with Python:

1. Work with low level building blocks: a combination of Python virtual environments and use of pip / requirements.txt file and setup.py file (if you are publishing the code as a package);
1. Higher order tooling - through use of tools such as tox or pipenv which attempts to combine the low level components above into a single integrated tool chain.

I have used the first option extensively and whilst it works, you can get tied in knots managing dependencies.  Whilst I have not used it in anger, my preference at the moment would be to use pipenv based on a look at the documentation and the fact that it is recommended by the offical Python.org site for dependency management.

My concern is that pipenv may be more difficult to get working on Azure DevOps given that most of the documentation I've seen is based on the first "low level" option above.

## Decision

Run a short spike to experiment with pipenv on Azure DevOps to prove whether it can be integrated successfully.

[As recommended by Python.org](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies)

[Pipenv documentation](https://pipenv.pypa.io/en/latest/)

[Good overview of issues with low level tooling approach and of pipenv](https://realpython.com/pipenv-guide/)

If this proves successful, adopt it as part of [0001-pipeline-to-publish-python-packages](.\0001-pipeline-to-publish-python-packages.md).

## Consequences

This has the following benefits:

- It will allow us to create deterministic builds in Python and mimic the tooling that comes out of the box for .NET;
- It is a key component of a pipeline in Azure DevOps for Python.
