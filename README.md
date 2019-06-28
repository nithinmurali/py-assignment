# Stakx python assignment

[![codecov](https://codecov.io/gh/nithinmurali/py-assignment/branch/master/graph/badge.svg?token=lvSyyYICy3)](https://codecov.io/gh/nithinmurali/py-assignment)

## Requirements
python 3.6+


## Installation

Clone the repository
```
git clone git@github.com:nithinmurali/stakx-assignment.git
cd stakx-assignment
```

Install all the requirements (preferably in a virtual env)
```
pip install -r requirements.txt
```

Then create the configuration file

```
cp sample.env .env
```

Now put the configuration values in `.env` file.

Now apply the migrations and run the server.

```
python manage.py migrate
python manage.py runserver 8080
```

## Testing

Run the tests using

```
pytest --cov-report term
```
