# Stakx python assignment

## Requirements
python 3.6+


## Installation

Clone the repository
```
git clone https://github.com/nithinmurali/stakx-assignment.git
cd stakx-assignment
```

Install all the requirements
```
pip install -r requirements.txt
```

Then create the configuration file

```
cp sample.env .env
```

Now put the configuration values in `.env` file and run the server.

```
python manage.py runserver 8080
```

## Testing

Run the tests using

```
pytest --cov-report term
```
