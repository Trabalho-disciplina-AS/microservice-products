from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS
import os
import dns


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "products",
    "host": "mongodb+srv://denis:arq1104@cluster0.a3msk.mongodb.net/test"
}

db = MongoEngine(app)
api = Api(app)
CORS(app)

# mongodb+srv://adrilene:arq2201@cluster0.a3msk.mongodb.net/test?retryWrites=true&w=majority&replicaSet=atlas-2nqljv-shard-0&ssl=true&authSource=admin
#f"mongodb+srv://{os.environ['MONGODB_USERNAME']}:{os.environ['MONGODB_PASSWORD']}@{os.environ['MONGODB_HOSTNAME']}/{os.environ['MONGODB_DATABASE']}?ssl=false"


from .models import product_model
from .services import product_service
from .controllers import product_many_controller, product_one_controller
