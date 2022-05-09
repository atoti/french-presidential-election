# atoti Project Adaptation

This project shows how we can translate the atoti notebook - [French presidential election 2022](https://github.com/atoti/notebooks/blob/master/notebooks/french-presidential-election) - into an actual project, ready for deployment into Heroku.

It is adapted from the [atoti project template](https://github.com/atoti/project-template).

On top of the `atoti` package, it comes with:

- Dependency management with [Poetry](https://python-poetry.org/)
- Settings management with [pydantic](https://pydantic-docs.helpmanual.io/usage/settings/)
- Testing with [pytest](https://docs.pytest.org/)
- Type checking with [mypy](http://mypy-lang.org/)
- Formatting with [Black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/)
- Linting with [Pylint](https://www.pylint.org/)
- Continuous testing with [GitHub Actions](https://github.com/features/actions)

## Usage

### Installation

- [Install `poetry`](https://python-poetry.org/docs/#installation)
- Install the dependencies:

  ```bash
  poetry install
  ```

### Commands

To get a list of the commands that can be executed to interact with the project, run:

```bash
poetry run app --help
```

A few examples:

- Start the app:

  ```bash
  poetry run app start
  ```

- Reformat the code:

  ```bash
  poetry run app format
  ```

## Atoti+

This version includes [the modifications](https://github.com/atoti/project-template/compare/atoti-plus) for Atoti+ in order to turn on authentication.  
Authentication is required in order to control access to the web application and prevent overwriting of dashboards by unauthorised personnel.  
Refer to [create_users.py](app/create_users.py) for the authorised users and their access rights.

### Required environment variables

- `POETRY_HTTP_BASIC_ATOTI_PLUS_USERNAME` and `POETRY_HTTP_BASIC_ATOTI_PLUS_PASSWORD` to install the `atoti-plus` plugin.
- A valid `ATOTI_LICENSE` to start the application.

## Deploy to Heroku

This project also includes [the modifications](https://github.com/atoti/project-template/compare/deploy-to-heroku) required to deploy it to Heroku.

Click on the button below to deploy this project to Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

_Note_: to deploy a project started from this template, remember to change the `repository` value in [app.json](app.json).
