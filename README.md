# GUX

- `git clone REPOSITORY_LINK` # Clone the repository
- `cd gux-backend`
- `virtualenv venv -p /path/to/python` # Create virtualenv
- `. venv/Scripts/activate` # Activate virtualenv
- `pip install -r requirements/develop.in`
- `cp .env-example .env`
- `nano .env` # Populate variables
- Set `ENVIRONMENT_MODULE` in `.env` 
- `python manage.py migrate`
- `python manage.py runserver`

# BBDD
- La base de datos es PosgreSQL, alojada en elephantSQL, si desean acceder desde un gestor de bbdd las credenciales se
  encuentran en el archivo .env