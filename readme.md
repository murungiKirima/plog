# Flask Blog.
#### By Murungi Kirima.
This is a blog web application made using flask.

## Description.
This is an application that users can log in, view various blogs by authors and shere post to their blogs.

## Usage.
You can click this link (https://flask-plog.herokuapp.com/) to launch the app in your browser.

### Prerequisites.
1. Language; You need to install python3.6
* Run the following individual commands to install python3.6
```
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6
```
* To confirm python3.6 installation, Run the
following command on your console:
```
$ python3.6

Python 3.6.0 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
...
>>>exit()
```
2. Virtual environment.
* Run the following individual commands on your console.
```
$ sudo apt-get install python3.6-venv
```
3. Database.
* Run the following individual commands on your console to install postgres.
```
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

* Now your ready to launch the app for development.

### Source Code and development.
1. Activate virtual env.
* Create the virtual environment in your application folder, Run the following in your console
```
$ cd <app folder>
$ python3.6 -m venv virtual
```
* Activate virtual environment by running
```
$ source virtual/bin/activate
```

2. Install requirements.
* Install requirements from requirements.txt file by running
```
$ pip install -r requirements.txt
```

3. Setup the db.
```
$ sudo -u postgres createuser --superuser $USER
```

4. Create the database for the blog.
```
$ sudo -u postgres createdb $USER
```

5. Run app for development.
* Run the following command on your terminal to run the app in developement
```
$ python manage.py server
```

## Technologies Used.
* Python3.6 as the development language. 
* Flask as the framework.
* Bootstrap for the styling. 
* Postgres for the DATABASE. 
* heroku for hosting the application. 

## Further help.
For additions, submit a pull request and once approved you can make contributions at will. Alternatively contact me at: murungikirima@gmail.com

## License.
MIT ©2017
