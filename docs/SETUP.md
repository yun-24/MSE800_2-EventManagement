# Setup Instructions

These instructions will help you set up the Django application .

## Prerequisites

- Python 3.x installed
- Virtual environment (conda)

## Set Up Steps

### Install Django

```shell
conda install django
```

### Create a Project

```shell
django-admin startproject event_management
cd event_management
```

### Create the Django apps

```shell
python manage.py startapp users
python manage.py startapp events
```

### Apply database migrations

```shell
python manage.py makemigrations users events
python manage.py migrate
```

### Run the development server

```shell
python manage.py runserver
```