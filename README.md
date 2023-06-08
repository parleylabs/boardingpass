# Boarding Pass
Boarding Pass

## Dependencies

Make sure you have docker installed and running
Docker: https://www.docker.com/

## Technology Stack
 
- Python
- Django
- PostgreSQL


## Getting Started

In the project directory, you can run:

## Local Set Up

1. Create environment variable config file
```
touch ./backend/.env
```

2. Set Up your environment variables in ./backend/.env
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_SCHEMA=
DB_PORT=
FIELD_ENCRYPTION_KEY=
```

You can either point to the container credentials in docker-compose.yml or a remote database

3. Build the contianers with 
`docker-compose build`

4. Run the contianers with 
`docker-compose up`

5. Apply migrations to database
 `make migrate`

6. Create a super User in django
`make createsuperuser`

7. Go to 
`http://127.0.0.1:8000/admin` Login with super user credentials

8. Create a user with username and password

9. Review Swagger Documentation
`http://127.0.0.1:8000/swagger/`

10. Go to `http://127.0.0.1:3000/` and sign in with your credentials

## AWS Set Up

1. Create EC2 Instance Ubuntu 
2. SSH into EC2 Instance https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html
3. Git clone repository
4. Run the following commands
```
sudo apt update & sudo apt upgrade    
sudo apt install python3-pip
python3 -m pip install --upgrade pip
```
5. cd into ```boardingpass/backend```
6. Run ```touch .env```
Add credentials for
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_SCHEMA=
DB_PORT=
FIELD_ENCRYPTION_KEY=
```
Note: You may need to spin up an RDS instance or point to remote database

7. Run ```pip install -r requirements.txt```
8. Run ```manage.py collectstatic```
9. Run ```gunicorn --workers 3 --bind 0.0.0.0:8000 api.wsgi:application```
10. Update AWS Security group to allow anywhere access to port 8000
11. View site at http://<ip_address>:8000/swagger/

