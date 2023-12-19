#utils.py	Utility functions to support authentication
			#>decorator function that wraps authentication functions in Flask routes
			#>Basic authentication for the routes with @auth_required in a Flask
			#>Adds a layer of security to specific routes by requiring 
			#>users to input valid authentication credentials before accessing those routes.

from functools import wraps
from flask import make_response, request, current_app
                            #  utils.py utility functions to support authentication

def auth_required(f):       #decorated function around the original function (f). (function that takes in a function)
    @wraps(f)           
    def decorated(*args, **kwargs):
        auth = request.authorization 
        if auth and auth.username == current_app.config["SITE_USER"] and auth.password == current_app.config["SITE_PASS"]: #after username and password are entered for authentication they are saved in the brower session.
            return f(*args, **kwargs) #calls the original f function if auth conditions are met. #TypeError: create_app.<locals>.update() got an unexpected keyword argument 'id'
        return make_response("<h1>Access Denied!</h1>", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'}) #headder with message and response if auth failed
    return decorated        #the auth_requires() function returns decorated if login conditions are met

##references

## ref1 (youtube.com, Login System in Flask: HTTP Basic Auth, Dec 2023) 
                ##retreived from: https://www.youtube.com/watch?v=8VmpH2f1jOk