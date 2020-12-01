from flask import request
from products.services.product_service import insert_product
from flask_restful import Resource
from products import app, api
import json
 

'''
{
    "qtd_random": 3,
    "only_discount": true
}
'''

class ProductManyController(Resource):
    def get(self):
        return {"msg": "OK"}, 200

    def post(self):
        data_json = {
            "name": request.form["name"],
            "category": request.form["category"],
        }
        product_id = insert_product(data_json, request.files["image"])
        return {"_id": product_id}, 200

api.add_resource(ProductManyController, "/products")

def get_product_by_id():
    pass

def get_product_by_category():
    pass
