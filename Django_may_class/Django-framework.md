## Introduction

- Django is a python framework the make it easy to create web apis and website using
- it comes with boilerplate that makes it easy to create web applications

## Type of python framework

- Flask - lightweight application framework
- Django - robust framework
- fastAPI - for developing APIs
- sqlachedemy - datascience

### Other python frameworks

- openml
- tinyml
- NLP
- Tensorflow & TFlite

## How it works

- It works based on MVTU design principles
- M - MODEL: Django model provides data from the database using Object Relational Mapping ORM. ORM makes it easy to work with database. It must be written in a file called models.py
- V - VIEW: It is a method or function that uses http request as argument to fetch data from the models to the templates, or import the relevant models needed and send the requested data to the template. they are written in views.py. types of request or HTTP method are GET POST PUT PATCH and DELETE
- T - TEMPLATES: This is the file where you describe the result to be represented. They are often html file and saved in a template folder
- U - URLs: Django provides a way to navigate between different template. The configuration is done in the urls.py file. It helps you to decorate a template file to a standard url endpoint

- It also comes with sqlite3 database which is not suitable for production because it is temporary database

## How to set up venv [global pc]

- Go to cmd and type "pip install virtualenv"
- pip is a package manager in python that enables you install libraries
- Every project requires that you create a virtual environment before you begin to develop

## Creating your venv in your project

- type "virtualenv [name of virtual env (venv)]"
- Option 2: type "python -m venv venv"

## To activate

- type "venv\Scripts\activate" in your terminal

## In production mode

- always follow the production guidelines

## Others information

- cpanel is used for hosting wordpress website

## Assignment

Create a tictactoe game with python.

- show welcome to my tictactoe game
- select position
- x show be purple color and o should be yellow color

find the library to change color

compare 6 difference between flask Django and FastAPI

- Check what social media is using them
