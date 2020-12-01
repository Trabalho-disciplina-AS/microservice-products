from flask import request
from products.services.product_service import insert_product, get_products_by_criteria
from flask_restful import Resource
from products import app, api
import json
 

'''
{
    "qtd_random": 3,
    "category": 'blabla',
    "discount": true,
}
'''

class ProductManyController(Resource):
    def get(self):
        params = {
            "qtd": request.args["qtd"],
            "category": request.args["category"],
            "discount": request.args["discount"],
        }

        get_products_by_criteria(**params)       

        
        return {"msg": "OK"}, 200

    def post(self):
        #import ipdb; ipdb.set_trace()
        data_json = {
            "name": request.values["name"],
            "price": request.values["price"],
            "category": request.values["category"],
            "discount": request.values["discount"],
            "discount_price": request.values["discount_price"]
        }
        product_id = insert_product(data_json, request.files["image"])
        return {"_id": product_id}, 200

api.add_resource(ProductManyController, "/products")
