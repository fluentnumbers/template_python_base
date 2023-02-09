# Welcome to the repository

## Overview

1. [CONTRIBUTING.md](./CONTRIBUTING.md)
2. [CHANGELOG.md](./CHANGELOG.md)
3. [MAINTAINERS](./MAINTAINERS.md)
4. [LICENSE](./LICENSE)

## Getting Started
- Clone the repo
- Have base Python 3.x.x installation on your system (e.g. from https://www.python.org/ftp/python/)
Required version is set up in the [Pipfile](https://github.com/philips-internal/template_python_algorithm/blob/main/Pipfile) under 
```
[requires]
python_version = "3.9"
```
  - with pipenv package: ``pip install pipenv`` (be done with `pip` after that and use `pipenv` instead)
  - run ``pipenv install`` inside the top-level directory
- More about using pipenv [here](https://pipenv.pypa.io/en/latest/)


## Pre-commit hooks
The repo is configured to run some pre-commit hooks every time you try to commit some changes to Git.
These include controlling and changing code formatting, checking that no large files are being committed, etc.
Full list of hooks is in the `.pre-commit-config.yaml` file.

If changes are made by pre-commit hooks or some errors are detected, you need to re-commit again.

Optionally, you can run `pre-commit run --all-files` in the cmd inside the repo to run pre-commit hooks without actually committing anything to Git yet.
This will allow to first make sure everything is ready for committing.


### Black
[Black](https://black.readthedocs.io/en/stable/?badge=stable) is an autoformatting tool, part of the pre-commit hooks.
You can also run it separately from everything else:
  To first see potential changes run `black src/ --check`
  To manually run autoformat for all code run `black src/`

  Autoformatting rules can be calibrated, but for easy solution to ignore a multiline piece of code use:
```
# fmt: off
   your code that you don't want to be touched by Black
# fmt: on
```
