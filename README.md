![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome SRay-2020,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## REQUIREMENTS

pip3 install -r requirements.txt


------



## Creating New Apps

python3 manage.py startapp 'name'

Add to INSTALLED APPS in Settings.py


------

## Setting Up Django Project

1. pip3 install django 

2. django-admin startproject boutique_ado . - Creates files we'll need (settings.py, urls.py etc.)

3. touch .gitignore (create our git ignore file)

4. python3 manage.py runserver (Run project)

5. python3 manage.py migrate - To run migrations

6. python3 manage.py createsuperuser - To create admin user (sray1990, s.r.ray@gmail, Password1990) (newguy1 newdawn2021) starkillerbase - starwars1) ( yoda2021 1withtheforce)

7. Initial Commit


------

## Django-Allauth for authorisation 

1. pip3 install django-allauth==0.41.0

2. Add allauth additional settings to settings and urls.py fils (see video Allauth Setup 1)

3. Navigate to admin of site - open port 8000 /admin + login details

4. Migrate app for new additions (python3 manage.py migrate)


------

## Migrations 

1. python3 manage.py makemigrations --dry-run

2. python3 manage.py makemigrations 

3. python3 manage.py migrate --plan

4. python3 manage.py migrate 

------

## Loading Data

1. python3 manage.py loaddata categories

2. python3 manage.py loaddata products

------

## Quickstart for project

1. pip3 install -r requirements.txt

2. python3 manage.py makemigrations --dry-run

3. python3 manage.py makemigrations 

4. python3 manage.py migrate --plan

5. python3 manage.py migrate 

6. python3 manage.py loaddata categories

7. python3 manage.py loaddata products

8. export STRIPE_SECRET_KEY=sk_test_51JYSDEAQb6q0x2KwYN4xfF2sbuhyLr1PP3L75QVtfa54AHeOZKL4LtABmw8R5CrElDKq6kDnLfsrMiGvQnmk7SuC00Che5f4US

9. export STRIPE_PUBLIC_KEY=pk_test_51JYSDEAQb6q0x2KwgVMPWeio4ynVOjfeAOYiTKJY5j1PuNt9fq5ydDkuAeave2L5qf5YqBphC2KCkmhqzVQ0yQxA00dRAxgEED

10. python3 manage.py runserver 

------
