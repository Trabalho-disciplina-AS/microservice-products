from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "devices",
    "host": "mongodb+srv://denis:arq1104@cluster0.a3msk.mongodb.net/test",
}
db = MongoEngine(app)
api = Api(app)
CORS(app)


from .models import product_model
from .services import product_service
from .controllers import product_many_controller, product_one_controller
