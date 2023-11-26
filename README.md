# DR_project

# Data Representation Project

## This repository contains all files relating to my Data Representation Project

### Author: Jarlath Scarry

### Repository contains 

                server folder
                db_calls folder
                db_work folder
                requirements.txt
                .gitignore
                Readme
                              

# Web application project overview: 
The projects consists of files to support the running of a flask server that supports a webpage. On the webpage the user can view a database of cars. The database holds a data on each car. The viewer can create, read, update and delete (CRUD) entries one at a time.   

The project repository contains all the files required to allow the viewer to carry out these operations. The operations are seperated into the following:
        A Flask server 
        REST API, (to perform CRUD operations)
        A mysql database with a table
        Accompanying web interface, using AJAX calls, to perform these CRUD operations


## Instructions to run the application:

The running of this web application will require a number of packages.

First, to run the `server.py` python will be required. It also requires some python packages. A list of Python packages required to run all labs and assignments is included in the requirements.txt file. When you have setup python and a virtual environment to run the files the required extra packages can be installed by rinning the command `pip install -r requirements.txt`

Next to support accessing the database `car_DB1` mysql is required. The application has been configured to access the `car_db1` database with the username and password `root`. 


## Starting the server
Navigate to the project folder and run the `server.py` file with the `python server.py` command. 
It should give the following output:

λ python server.py
* Serving Flask app 'server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 168-648-133

The server is now running.


## Accessing the web page

From your web browser search the adderss: http://127.0.0.1:5000
This should open the cars web page. From there you can view and carryout CRUD operations on the `car_db1`.


### End


