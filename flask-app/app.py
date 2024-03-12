import time
import json
from flask import Flask, render_template, jsonify, request, make_response
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)


def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://mongodb:27017")
        # client = MongoClient("mongodb://localhost:27017")
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        time.sleep(1)  # Retry after 1 second
    return client


client = connect_to_mongodb()
db = client['fullstack'] if 'fullstack' in client.list_database_names() else None


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
    def get(self):
        if db is not None:
            try:
                
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
                # breakpoint()
                return {"total number of users": len(users_data), "users": json_data}, 200
            except Exception as e:
                # breakpoint()
                # print("hitting here")
                return {"error": str(e)}, 500
        else:
            return {"error": "MongoDB is not initialized."}, 500

    def post(self):
        if db is not None:
            try:
                request_data = request.json
                first_name = request_data.get("First Name")
                last_name = request_data.get("Last Name")
                email = request_data.get("Email")
                password = request_data.get("Password")

                db['users'].insert_one({
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Email": email,
                    "Password": password
                })

                return {
                    'status': 'Successfully stored the data in MongoDB!',
                    'firstName': first_name,
                    'lastName': last_name,
                    'email': email,
                    'password': password}, 200
            except Exception as e:
                return {"error": str(e)}, 500
        else:
            return {"error": "MongoDB is not initialized."}, 500


api.add_resource(UserAnalysis, '/users')
