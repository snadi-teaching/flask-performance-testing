from flask import Flask
from flask_restx import Api
from api.student import api as students
from db.db import init_db
from flask_cors import CORS

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:8000"],  # Get origin from env with fallback
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True,
        }
    },
)


init_db(app)

# Initialize Flask-RESTx API and register the students namespace
api = Api(app)
api.add_namespace(students)  # Add the students namespace to the API

if __name__ == "__main__":
    app.run(debug=True)
