[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=stellardropthebeat_swe&metric=coverage)](https://sonarcloud.io/summary/new_code?id=stellardropthebeat_swe)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=stellardropthebeat_swe&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=stellardropthebeat_swe)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=stellardropthebeat_swe&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=stellardropthebeat_swe)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=stellardropthebeat_swe&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=stellardropthebeat_swe)

# Vending Machine Manager Application
This application can basically perform CRUD on Vending Machine and its stock

## Prerequisites
- Docker
- Database(Mariadb)
- Poetry
- Pytest
- IDE with python installed

### Installing software and launch application
Step 1: Install Docker, MariaDB, Poetry and finish the set-up.

Step 2: Clone this GitHub to your repository.

Step 3: Make sure your current workspace is in directory ***swe***

Step 4: run this command in terminal `docker compose up --build`

Step 5: It will take a couple while to run all the stuffs.

Step 6: Then, you can now access it via [http://localhost:5000](http://localhost:5000)

Step 7: After you finish visiting, don't forget to ***crtl+c*** in terminal to terminate the program.

Step 8: To finish all stuff in docker, just run `docker compose down`, and we are done.

### Running the tests

Step 1: Make sure you are in directory ***swe***

Step 2: Have Poetry installed

Step 3: Run `poetry install` to install all the dependencies

Step 4: Run `poetry run pytest` to run all the tests

Step 5: If you want to run specific test, run `poetry run pytest -k <test_name>`

## Authors
Nutchapol Isariyapruit ID: 6281454
