# HR Employee System

## Employee management system for HRs

## Usage

-   run the server and hit http://localhost:8000/admin/ to the login page
-   enter username:'root', password:'root'

### Requirements

you should have python3.7.2 and PostgreSQL installed.

## Installation

-   clone the repo and cd /path/to/repo
-   pip install pipenv
-   pipenv install
-   python manage.py makemigrations
-   python manage.py migrate

### Configuration

-   after installing postgres you should create a database with the same name as in repo/settings.py in "DATABASE"
