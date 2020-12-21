from flask import request
from products.services.product_service import (
    insert_product,
    get_products_by_criteria,
    get_products,
    update_qtd_stock,
)
from flask_restful import Resource
from products import app, api
import json
import requests
import random

"""
{
    "qtd_random": 3,
    "category": 'blabla',
    "discount": true,
}
"""


class ProductManyStockController(Resource):
    def post(self):
        print(request.json["id"], int(request.json["qtd_stock"]))
        update_qtd_stock(request.json["id"], int(request.json["qtd_stock"]))
        return {"msg": "ok"}, 200


class ProductManyController(Resource):
    def get(self):
        products = json.loads(get_products().to_json())

        return products, 200

    def post(self):
        data_json = {
            "name": request.values["name"],
            "price": request.values["price"],
            "category": request.values["category"],
            "discount": request.values["discount"],
            "discount_price": request.values["discount_price"],
        }
        product_id = insert_product(data_json, request.files["image"])
        return {"_id": product_id}, 200


class ProductManyVariedController(Resource):
    def get(self):
        # quantidade é obrigatória.
        params = dict(request.args)

        products = get_products_by_criteria(**params)
        products = json.loads(products.to_json())

        for product in products:
            product["_id"] = product["_id"]["$oid"]
            del product["created_at"]

        return products, 200


api.add_resource(ProductManyStockController, "/products/qtd_stock")
api.add_resource(ProductManyController, "/products")
api.add_resource(ProductManyVariedController, "/products_varied")
