## MTT project frontend

## Installation requirements:

Postgres
Homebrew

## First time installation:

```
brew install pyenv
brew install pipenv
pyenv install 3.11
pyenv local 3.11
```

## setup database:

```
createdb -T template1 mtt -U postgres -W
```

## setup:

```
pipenv shell
pipenv install
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
