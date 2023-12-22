# DR_project

# Data Representation Project

## This repository contains all files relating to my Data Representation Project

### Author: Jarlath Scarry

### Repository contains 

                templates folder
                venv folder
                server.py
                carDAO.py
                csoDAO.py
                dbconfig.py
                car_db1.sql
                requirements.txt
                .gitignore
                .env
                Readme
                              

# Web application project overview: 
The projects consists of files to support the running of a flask server that supports a webpage. On the webpage the user can view a database of cars on a html table. The database holds data on each car. The viewer can create, read, update, view and delete (CRUD) entries one at a time.   

The server also links to a 3rd party API. 
(https://data.cso.ie/  datasets "TEM20" "New Private Cars Licensed for the First Time")
The user can search this database by a search form on the webpage. It allows the user to filters data by year and month.

The project repository contains all the files required to allow the viewer to carry out these operations. The operations are seperated into the following:
        A Flask server 
        REST API (to perform CRUD operations)
        A mysql database with a table.
        Accompanying web interface, using AJAX calls, to perform these CRUD operations


## Instructions to run the application:

The running of this web application will require a number of packages.

First, to run the `server.py` python will be required. It also requires some python packages. A list of Python packages required to run all labs and assignments is included in the requirements.txt file. When you have setup python and a virtual environment to run the files the required extra packages can be installed by running the command: `pip install -r requirements.txt`

Next to support accessing the database `car_db1` mysql is required. The application has been configured to access the `car_db1` database with the username and password `root`. The `car_db1.sql` is included in the repository.


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

The server is now running on your machine in local mode! 

## Accessing the web page

From your web browser search the adderss: http://127.0.0.1:5000

## Login

A `Sign in` prompt will appear when you try to launch the webpage. You must sign in to view it.

                Username = user

                Password = pass

The cars webpage should now be visible.
From there you can view and carryout CRUD operations on the `car_db1`.


## Server debug mode is on! 
You can watch the requests in your cmd window as you browse the web page.
Here is an example of a delete request:

                127.0.0.1 - - [19/Dec/2023 11:31:56] "GET /cars HTTP/1.1" 200 -
                delete done
                127.0.0.1 - - [19/Dec/2023 11:32:05] "DELETE /cars/32 HTTP/1.1" 200 -

## Using the page
Browse and carryout CRUD operations by the buttons on the table.
Search cso.ie resource by the search search function.
Some features:
        A list of cars in the database is scrolled acress the top of the page, under the nav bar.
        Random car picked from the table is displayed as "Manager's Pick". Updates when page is refreshed.
        Bootstrap styling to adapt page for screen size.
        Search cso.ie database of car registrations.

## Stopping the server
To stop the server running: Go to your cmd and press `ctrl` and  `C` together.

## References and Acknowledgements
Acknowledgment to Lecturer Andrew Beatty for guidance through the 23-24: DATA REPRESENTATION module.
Specific references throughout the code.

### End


