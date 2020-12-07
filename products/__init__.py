from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "devices",
    "host": "mongodb://localhost/products",
}
db = MongoEngine(app)
api = Api(app)
CORS(app)


from .models import product_model
from .services import product_service
from .controllers import product_many_controller, product_one_controller
