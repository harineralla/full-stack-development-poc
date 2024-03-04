import time
import json
from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://localhost:27017")
db = client['fullstack']

CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Full Stack API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# @app.route('/swagger.json')
# def swagger():
#     with open('/static/swagger.json', 'r') as f:
#         return jsonify(json.load(f))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


class UserAnalysis(Resource):
    def get(slef):
        # breakpoint()
        users_data = list(db['users'].find())
        json_data = []
        for doc in users_data:
            fn = doc["First Name"]
            ln = doc["Last Name"]
            email = doc["Email"]
            password = doc["Password"]
            json_data.append({
                "First Name": fn,
                "Last Name": ln,
                "Email": email,
                "Password": password
            })
        return jsonify({"total number of users": len(users_data)}, json_data)

    def post(self):
        request_data = request.json
        first_name = request_data.get("First Name")
        last_name = request_data.get("Last Name")
        email = request_data.get("email")
        password = request_data.get("password")

        db['users'].insert_one({
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "Password": password
        })

        return jsonify({
            'status': 'Succesfully stored the data in MongoDB!',
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'password': password})


api.add_resource(UserAnalysis, '/users')
