# boardingpass_backend
Boarding Pass Backend

## Table of Contents
* [Introduction](#intoduction)
* [Set Up](#set-up)

## Introduction
Backend for using AWS Lambda.

## Set Up
Create a virtual environment at the root of the project
```
python3 -m venv ./venv
```

Activate the virtual environment
```
source venv/bin/activate
```

Install PostgreSQL
```
brew install postgresql  
```

Install Django Packages & Dependencies
```
pip install -r requirements.txt
```

Create environment variable config file
```
touch .env
```

Set Up your environment variables
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_SCHEMA=
```

Run Migrate
```
./manage.py migrate  
```

Run the Server
```
./manage.py runserver
```

Navigate to API
```
http://127.0.0.1:8000/users/
```
