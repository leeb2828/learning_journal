# learning_journal
Written in HTML, CSS, and Django. User can signup, login, or logout of their account. They can create, update, or delete their entries.

## How to use this Project

From your terminal, download the files using
```
$ git clone https://github.com/leeb2828/learning_journal.git
```
<br />

A virtual environment is a tool that helps to keep dependencies required by
different projects separate from each other by using isolated virtual environments.
Create and activate your virtual environment using pipenv or venv:
<br />
First option:
```
$ pipenv install
$ pipenv shell
```
You will notice that a Pipfile and a Pipfile.lock appeared.

<br />
Second option is to create and activate your virtual environment using venv. The venv module comes 
pre installed with Python 3.5 + versions:

```
$ python3 -m venv env
$ source env/bin/activate
```

Install all dependencies from the requirements.txt file
```
$ pip install -r requirements.txt
```

<br />
<br />

Before running the server and viewing the project, you need to create the database.
```
python manage.py migrate
```
Inside of the learning_journal_app/migrations folder, if there is no 0001_initial.py file, you will first 
need to run the python manage.py makemigrations command.

<br />

Run the server
```
$ python manage.py runserver
```
You can specify the port number 8000 with python manage.py runserver 8000.
In your browser, navigate to http://localhost:8000/ 
<br />
User can log in after registering for an account:
![Project Image](project_images/login.png)

After logging in, the user is redirected to the home page:
![Project Image](project_images/home_page.png)

Click on an individual post to view it:
![Project Image](project_images/post.png)

The user has the option to modify an entry (so long as they are the author):
![Project Image](project_images/modify_post.png)



<br />

Quit the server with CONTROL-C.
To deactivate the pipenv virtual environment, use the "exit" command.
For the venv virtual environment, use "deactivate".
