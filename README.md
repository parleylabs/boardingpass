# boardingpass
Boarding Pass

## Dependencies

Make sure you have docker installed and running
Docker: https://www.docker.com/

## Getting Started

In the project directory, you can run:

## Set Up

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

9. Go to `http://127.0.0.1:3000/` and sign in with your credentials

