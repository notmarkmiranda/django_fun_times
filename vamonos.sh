#!/bin/bash

echo HERE WE GO!
pip3 install pipenv
pipenv run pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py runserver