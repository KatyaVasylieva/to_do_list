# To Do List

Django project for managing you work and life. Write out all to-do tasks you have, create special tags for grouping them by theme and start completing them one by one.


## Installation

A quick introduction of the minimal setup:

Python3 must be already installed.

```shell
git clone https://github.com/KatyaVasylieva/to_do_list
cd to_do_list
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Set environment variables:

```shell
export DJANGO_SECRET_KEY=<your SECRET_KEY>
export DATABASE_URL=<your DATABASE_URL>
```

Run Django server:
```shell
python manage.py runserver
```
