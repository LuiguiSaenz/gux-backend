# GUX

## Dependencies:

### Common.in:

1. mysqlclient

    - Install `mysql` on your system

### Develop.in:

## Development

### Firt time

- `git clone REPOSITORY_LINK` # Clone the repository
- `cd gux`
- `virtualenv venv -p /path/to/python` # Create virtualenv
- `. venv/Scripts/activate` # Activate virtualenv
- `pip install -r requirements/develop.in`
- `cp .env-example .env`
- `nano .env` # Populate variables
- Set `ENVIRONMENT_MODULE` in `.env` file, alternatives are: `develop`, `testing`, `staging` and `production`.
- `./manage.py migrate`
- `./manage.py runserver`

### Update dependencies

- `pip install pip-tools` # Just in case
- `pip-compile -r requirements/develop.in -o requirements-DATE.develop` # Generates a requirements file with the latest version of the dependencies up to the current date.
- `pip-sync requirements-DATE.develop` # Synchronize the dependencies and versions of your virtual environment with those of the generated file. You might need to elevate your terminal

### Create apps

- `mkdir apps/APP_NAME`
- `./manage.py startapp --template=https://github.com/inspired-solutions/django-starter/archive/rest-app.zip APP_NAME apps/APP_NAME`

### Run tests and generate html coverage code report

- `coverage run --source='.' manage.py test && coverage html`
- `open htmlcov/index.html` # Opens in your browser

### Get Database graph 

- `brew install graphviz` # First
- `xcode-select --install` # Just in case
- If needed, re-create virtual environment
- `./manage.py graph_models -a -g -o database-DATE.png`
- `open database.png`

## Build & Deploy

- `pip-compile -r requirements/production.in -o requirements-DATE.production` # Generates a requirements file with the latest version of the dependencies up to the current date.
- `ssh user@server`
- `cd /path/to/folder`
- `./venv/lib/activate`
- `./manage.py migrate`
- `pip-sync requirements-DATE.production` # Synchronize the dependencies and versions of your virtual environment with those of the generated file. You might need to elevate your terminal
- `sudo apachectl restart`
