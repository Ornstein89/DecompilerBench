virtualenv venv

: activate the virtual environment

./venv/scripts/activate

: source bin/activate

pip3 install django djangorestframwork celery redis keras

: install Redis server :
: for linux : sudo apt-get update -y && sudo apt-get install redis
: start a django project
: django-admin startproject MyApp