# django BootCamp

## Envrionment Setup

    python3 -m venv <myenvname>
    source <myenvname>/bin/activate
    pip intall django

## Start Project

make sure that file directory must be right

    django-admin startproject <myenvname>
    python3 manage.py runserver


## Make First App

    python3 manage.py startapp <appname>

## View

View means **request and response in a website or request handler or action**. In django, they called view.

## Make two app

for store app
    python3 manage.py startapp store
for tags app
    python3 manage.py startapp tags