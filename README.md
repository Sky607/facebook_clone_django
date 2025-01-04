# facebook_clone_django

## Documentation

## Introduction

This projects  is developed with the latest version of python and its framework Django of latest version. To run this project first install all the pacakages mention in the requirement.txt under this  project

## Installation
To load the above project from github run the following command in your cmd
```sh
git clone https://github.com/Sky607/facebook_clone_django.git
```
# Note 
The above command only works if git is installed in your environment
```sh
pip install -r requirement.txt
```
By running above command in your cmd all the dependencies or required modules are downloaded in your system and you are ready to serve th project


# Note
This command only works when you are in the same folder where your project folder and manage.py folder you extracted

# Execution

Before starting the project please follow the below steps
- First run the migration in the cmd by using following commands
```sh
python manage.py makemigrations <app-name> or python manage.py makemigrations
python manage.py migrate
```
To serve the above project run the below command 
```sh
python manage.py runserver
```
In your browser type this url and you can see the project running 
http://127.0.0.1:8000/

# Admin
To access the admin panel first create a super user from cmd 
```sh
python manage.py createsuperuser
```
After creating your username and password from the above code in your  cmd restart the server

```sh 
python manage.py runserver
```
In your browser under the url section type http://127.0.0.1:8000/admin and press enter, your admin page ask you for username and password enter which your created in your cmd before.Now you can access your admin panel from where you can see all the details.
