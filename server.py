# server.py	Flask application with routes to perform CRUD operations.
			#>A RESTful API built with Flask for managing car data stored in a database
			#>Also authentication using the @auth_required

#Sign in =      Username: user
#               Password: pass

from flask import Flask, render_template, jsonify, request, abort
from dotenv import load_dotenv
from carDAO import carDAO
from utils import auth_required
import os
import json

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='.')
    app.config.from_prefixed_env()

    @app.route('/')
    @auth_required  # authentication required here before running the index() function
    def index():        
        return render_template('car.html')  #render the car.html (after authentication passed)

    #curl "http://127.0.0.1:5000/cars"
    @app.route('/cars')
    @auth_required                      #authentication # ref1 (youtube.com, Login System in Flask: HTTP Basic Auth, Dec 2023) 
    def getAll():
        results = carDAO.getAll()
        return jsonify(results)

    #curl "http://127.0.0.1:5000/cars/2"
    @app.route('/cars/<int:id>')
    @auth_required                      #authentication 
    def findById(id):
        foundCar = carDAO.findByID(id)

        return jsonify(foundCar)

    #curl  -i -H "Content-Type:application/json" -X POST -d "{\"make\":\"Audi\",\"model\":\"A1\",\"registration\":\"11D11\",\"price\":123}" http://127.0.0.1:5000/cars
    @app.route('/cars', methods=['POST'])
    @auth_required                      #authentication 
    def create():
        
        if not request.json:
            abort(400)
        cars = {
            "make": request.json['make'],
            "model": request.json['model'],
            "registration": request.json['registration'],
            "price": request.json['price'],
        }
        values =(cars['make'],cars['model'],cars['registration'],cars['price'])
        newId = carDAO.create(values)
        cars['id'] = newId
        return jsonify(cars)

    #curl  -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Audi\",\"model\":\"A1\",\"registration\":\"11D11\",\"price\":1000}" http://127.0.0.1:5000/cars/1
    @app.route('/cars/<int:id>', methods=['PUT'])
    @auth_required                      #authentication 
    def update(id):
        foundCar = carDAO.findByID(id)
        if not foundCar:
            abort(404)
        
        if not request.json:
            abort(400)
        reqJson = request.json
        if 'price' in reqJson and type(reqJson['price']) is not int:
            abort(400)

        if 'make' in reqJson:
            foundCar['make'] = reqJson['make']
        if 'model' in reqJson:
            foundCar['model'] = reqJson['model']
        if 'registration' in reqJson:
            foundCar['registration'] = reqJson['registration']
        if 'price' in reqJson:
            foundCar['price'] = reqJson['price']
        values = (foundCar['make'],foundCar['model'],foundCar['registration'],foundCar['price'],foundCar['id'])
        carDAO.update(values)
        return jsonify(foundCar)
            
    @app.route('/cars/<int:id>' , methods=['DELETE'])
    @auth_required                      #authentication 
    def delete(id):
        carDAO.delete(id)
        return jsonify({"done":True})
    
    return app

if __name__ == '__main__' :
    app = create_app()  #call the function to creates instance of a flask
    app.run(debug=True)  #start the Flask application using the run() method


## ref1 (youtube.com, Login System in Flask: HTTP Basic Auth, Dec 2023) 
                ##retreived from: https://www.youtube.com/watch?v=8VmpH2f1jOk